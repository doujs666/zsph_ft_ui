# coding=UTF-8
import math
from dateutil.relativedelta import relativedelta
import datetime
import numpy


class BaseContract(object):
    """期缴合同金额计算类"""

    def __init__(self, cycle, rate, contract):
        self.cycle = cycle
        self.rate = rate / 100
        self.contract = contract

    def pmt(self, rate, cycle, contract_monkey):
        pmt = numpy.pmt(rate, cycle, -contract_monkey)
        return pmt

    def ppmt(self, rate, i, cycle, contract_monkey):
        ppmt = numpy.ppmt(rate, i, cycle, -contract_monkey)
        return ppmt

    def contract_money(self):
        # 合同金额
        contract_monkey = hundred_float_up(self.contract / (1 - 0.03))
        return contract_monkey

    def total_interest(self):
        # 总还利息
        # (合同金额×月利率×(1＋月利率)＾期数〕÷〔(1＋月利率)＾期数 - 1〕*期数 - 合同金额
        # 200000 * (9 % / 12) * (1 + 9 % / 12) ^ 180 / [(1 + 9 % / 12) ^ 180 - 1] = 2028.533168

        base_a = self.contract_money() * (0.1 / 12) * ((1 + 0.1 / 12) ** self.cycle)
        base_b = ((1 + 0.1 / 12) ** self.cycle - 1)
        total_interest = export_result(base_a / base_b * self.cycle - self.contract_money()) + 0.01
        return total_interest

    def month_principal_interest(self):
        # 月还本息
        base_a = self.contract_money() * (0.1 / 12) * ((1 + 0.1 / 12) ** self.cycle)
        base_b = ((1 + 0.1 / 12) ** self.cycle - 1)
        month_principal_interest = export_result(base_a / base_b) + 0.01
        return month_principal_interest

    def ask_charge(self):
        # 普惠咨询费
        ask_charge = self.contract_money() - self.contract
        return ask_charge

    def mouth_mid_charge(self):
        # 融贝月服务费
        mouth_mid_charge = export_result(
            self.pmt(0.14 / 12, self.cycle, self.contract_money()) - self.pmt(0.1 / 12, self.cycle,
                                                                              self.contract_money())) + 0.01
        return mouth_mid_charge

    def mid_charge(self):
        # 融贝总服务费
        mid_charge = self.mouth_mid_charge() * self.cycle
        return mid_charge

    def mouth_daihou_manager(self):
        # 知了蝉鸣月贷后管理费
        if self.cycle == 12:
            mouth_daihou_manager = export_result(self.pmt(0.14 / 12, self.cycle, self.contract_money() * 0.08)) + 0.01
        else:
            mouth_daihou_manager = export_result(self.pmt(0.14 / 12, self.cycle, self.contract_money() * 0.1)) + 0.01
        return mouth_daihou_manager

    def daihou_manager(self):
        # 知了蝉鸣贷后管理费
        daihou_manager = self.mouth_daihou_manager() * self.cycle
        return daihou_manager

    def mouth_total_server(self):
        # 月应还服务费
        mouth_total_server = export_result((
                                                   self.contract * self.rate * self.cycle - self.ask_charge() - self.total_interest()) / self.cycle) + 0.01
        return mouth_total_server

    def total_server(self):
        # 总应还服务费
        total_server = self.mouth_total_server() * self.cycle
        return total_server

    def mouth_manage_charge(self):
        # 普惠月还款管理费
        mouth_manage_charge = self.mouth_total_server() - self.mouth_mid_charge() - self.mouth_daihou_manager()
        return mouth_manage_charge

    def manage_charge(self):
        # 普惠总还款管理费
        manage_charge = self.mouth_manage_charge() * self.cycle
        return manage_charge

    def mouth_repay(self):
        # 月应还款额
        mouth_repay = self.mouth_total_server() + self.month_principal_interest()
        return mouth_repay

    def month_principal(self):
        # 月还本金
        lists = []
        for i in range(1, self.cycle + 1):
            month_principal = export_result(self.ppmt(0.1 / 12, i, self.cycle, self.contract_money())) + 0.01
            lists.append(month_principal)
        return lists

    def sum_interest(self):
        # 月还利息
        sum_interest = 0
        for i in range(1, self.cycle + 1):
            sum_interest += numpy.ipmt(0.1 / 12, i, self.cycle, -self.contract_money())
        new_sum_interest = export_result(sum_interest) + 0.01
        return new_sum_interest

    def overdue_one_day(self):
        # 逾期一天
        overdue_one_day = export_result(self.contract_money() * 0.00039 + self.liquidated_damages()) + 0.01
        return overdue_one_day

    def overdue_seven_day(self):
        # 逾期七天
        overdue_seven_day = export_result(self.contract_money() * 0.00039 * 7 + self.liquidated_damages()) + 0.01
        return overdue_seven_day

    def sum_remain_principal(self):
        # 剩余本金
        remain_principal = self.contract_money()
        lists = []
        for i in range(self.cycle - 1):
            remain_principal = remain_principal - self.month_principal()[i]
            new_remain_principal = export_result(remain_principal) + 0.01
            lists.append(new_remain_principal)
        lists.append(0.00)
        return lists

    def year_rate(self):
        # 告知书的综合资金成本（年费率）
        sum_money = \
            self.ask_charge() + self.mid_charge() + self.manage_charge() + self.daihou_manager() + self.sum_interest()
        contract_money = self.contract_money()
        cycle = float(self.cycle) / float(12)
        year_rate = sum_money / contract_money / cycle
        return year_rate

    # def interest(self):
    #     # 利息
    #     monthly_repay = self.monthly_repay()
    #     lists = []
    #     base_money_d = self.base_money_d()
    #     for i in range(self.cycle):
    #         interest = monthly_repay - base_money_d[i]
    #         lists.append(interest)
    #     return lists

    def interest_penalty(self, start_period_no, over_period_no, date):
        # 罚息
        # date传期数
        lists = []
        overdue_count = range(start_period_no, over_period_no + 1)
        count_day = get_date(date, len(overdue_count))[1]
        for i in overdue_count:
            interest_penalty = export_result(
                self.sum_remain_principal()[i - 1] * 0.00039 * int(count_day[i - start_period_no])) + 0.01
            lists.append(interest_penalty)
        return lists

    def liquidated_damages(self):
        # 违约金
        liquidated_damages = export_result(self.month_principal_interest() * 0.05) + 0.01
        return liquidated_damages


def export_result(num):
    # 保留2位不上浮小数
    num_x, num_y = str(num).split('.')
    num = float(num_x + '.' + num_y[0:2])
    return num


def hundred_float_up(num):
    # 百位上浮
    num = math.ceil(num / 100) * 100
    return num


def get_date(date, count):
    # 返回日期,天数
    date_list = []
    day_list = []
    now = datetime.datetime.now()
    now.strftime('%Y-%m-%d')
    for i in range(count):
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        fix_date = input_date + relativedelta(months=i)
        get_fix_date = fix_date.strftime('%Y-%m-%d')
        get_day = now - fix_date
        date_list.append(get_fix_date)
        day_list.append(repr(get_day.days))
    return date_list, day_list


def main():
    rate = input(u'输入月利率')
    cycle = input(u'输入期数')
    contract = input(u'输入到手金额')
    base_contract = BaseContract(cycle, rate, contract)
    print(u'告知函: {0}'.format(str(base_contract.year_rate())))
    print(u'合同金额: {0}'.format(str(base_contract.contract_money())))
    print(u'总还利息: {0}'.format(str(base_contract.total_interest())))
    print(u'月还本息: {0}'.format(str(base_contract.month_principal_interest())))
    print(u'剩余本金: {0}'.format(str(base_contract.sum_remain_principal())))
    print(u'应还款额: {0}'.format(str(base_contract.mouth_repay())))
    print(u'融贝服务费: {0}'.format(str(base_contract.mouth_mid_charge())))
    print(u'融贝总服务费: {0}'.format(str(base_contract.mid_charge())))
    print(u'普惠咨询费: {0}'.format(str(base_contract.ask_charge())))
    print(u'知了蝉鸣月贷后管理费: {0}'.format(str(base_contract.mouth_daihou_manager())))
    print(u'知了蝉鸣贷后管理费: {0}'.format(str(base_contract.daihou_manager())))
    print(u'月应还服务费: {0}'.format(str(base_contract.mouth_total_server())))
    print(u'总应还服务费: {0}'.format(str(base_contract.total_server())))
    print(u'普惠月还款管理费: {0}'.format(str(base_contract.mouth_manage_charge())))
    print(u'普惠总还款管理费: {0}'.format(str(base_contract.manage_charge())))
    print(u'逾期1天: {0}'.format(str(base_contract.overdue_one_day())))
    print(u'逾期7天: {0}'.format(str(base_contract.overdue_seven_day())))
    print(u'逾期7天: {0}'.format(str(base_contract.overdue_seven_day())))
    print(u'违约金: {0}'.format(str(base_contract.liquidated_damages())))
    print(u'罚息: {0}'.format(str(base_contract.interest_penalty(1, 1, '2018-11-08'))))


if __name__ == '__main__':
    main()
