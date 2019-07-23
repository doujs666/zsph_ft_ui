# coding=UTF-8
import math
from dateutil.relativedelta import relativedelta
import datetime


class BaseContract(object):
    """趸交合同金额计算类"""

    def __init__(self, cycle, rate, contract):
        self.cycle = cycle
        self.rate = rate / 100
        self.contract = contract
        self.base_a = (self.rate * self.cycle * self.contract + self.contract) / self.cycle / (0.1 / 12)
        self.base_b = (1 + 0.1 / 12) ** self.cycle

    def contract_money(self):
        # 合同金额
        contract_monkey = hundred_float_up(self.base_a / self.base_b * (self.base_b - 1))
        return contract_monkey

    def total_server(self):
        # 服务费
        total_server = self.contract_money() - self.contract
        return total_server

    def mid_charge(self):
        # 融贝服务费
        if self.cycle == 48:
            mid_charge = self.contract_money() * 0.07
        elif self.cycle == 36:
            mid_charge = self.contract_money() * 0.055
        elif self.cycle == 12:
            mid_charge = self.contract_money() * 0.03
        else:
            mid_charge = self.contract_money() * 0.04
        return mid_charge

    def ask_charge(self):
        # 普惠咨询费
        if self.cycle == 12:
            ask_charge = self.contract_money() * 0.01
        else:
            ask_charge = self.contract_money() * 0.06
        return ask_charge

    def daihou_manager(self):
        # 知了蝉鸣贷后管理费
        if self.cycle == 12:
            daihou_manager = self.contract_money() * 0.08
        else:
            daihou_manager = self.contract_money() * 0.1
        return daihou_manager

    def manage_charge(self):
        # 普惠还款管理费
        manage_charge = self.total_server() - self.mid_charge() - self.ask_charge() - self.daihou_manager()
        return manage_charge

    def overdue_one_day(self):
        # 逾期一天
        overdue_one_day = export_result(self.contract_money() * 0.00039 + self.liquidated_damages()) + 0.01
        return overdue_one_day

    def overdue_seven_day(self):
        # 逾期七天
        overdue_seven_day = export_result(self.contract_money() * 0.00039 * 7 + self.liquidated_damages()) + 0.01
        return overdue_seven_day

    def base_money_d(self):
        # 剩余本金
        base_d = []
        for i in range(1, self.cycle + 1):
            a = self.contract_money() * 0.1 / 12
            b = (1 + 0.1 / 12) ** (i - 1)
            c = ((1 + 0.1 / 12) ** self.cycle - 1)
            d = a * (b / c)
            base_d.append(d)
        return base_d

    def sum_remain_principal(self):
        # 剩余本金
        remain_principal = self.contract_money()
        lists = []
        for i in range(self.cycle - 1):
            d = self.base_money_d()[i]
            remain_principal = remain_principal - d
            new_remain_principal = export_result(remain_principal) + 0.01
            lists.append(new_remain_principal)
        lists.append(0.00)
        return lists

    def monthly_repay(self):
        # 应还款额
        monthly_repay = export_result(self.contract_money() * self.base_b * (0.1 / 12) / (self.base_b - 1)) + 0.01
        return monthly_repay

    def interest(self):
        # 利息
        monthly_repay = self.monthly_repay()
        lists = []
        base_money_d = self.base_money_d()
        for i in range(self.cycle):
            interest = monthly_repay - base_money_d[i]
            lists.append(interest)
        return lists

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
        liquidated_damages = export_result(self.monthly_repay() * 0.05) + 0.01
        return liquidated_damages

    def year_rate(self):
        # 告知书的综合资金成本（年费率
        # 总咨询费+总服务费+总还款管理费+总贷后管理费+每一期的利息之和）/合同金额/借款年限
        sum_money = self.ask_charge() + self.mid_charge() + self.manage_charge() + self.daihou_manager() + sum(
            self.interest())
        contract_money = self.contract_money()
        cycle = float(self.cycle) / float(12)
        year_rate = sum_money / contract_money / cycle
        return year_rate


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
    # print(base_contract.interest_penalty(1, 1, '2018-10-23'))
    # print(base_contract.liquidated_damages())
    print(base_contract.year_rate())
    print(u'告知函: {0}'.format(str(base_contract.year_rate())))
    print(u'合同金额: {0}'.format(str(base_contract.contract_money())))
    print(u'应还款额: {0}'.format(str(base_contract.monthly_repay())))
    print(u'违约金: {0}'.format(str(base_contract.liquidated_damages())))
    print(u'服务费: {0}'.format(str(base_contract.total_server())))
    print(u'融贝服务费: {0}'.format(str(base_contract.mid_charge())))
    print(u'普惠咨询费: {0}'.format(str(base_contract.ask_charge())))
    print(u'知了蝉鸣贷后管理费: {0}'.format(str(base_contract.daihou_manager())))
    print(u'普惠还款管理费: {0}'.format(str(base_contract.manage_charge())))
    print(u'逾期1天: {0}'.format(str(base_contract.overdue_one_day())))
    print(u'逾期7天: {0}'.format(str(base_contract.overdue_seven_day())))


if __name__ == '__main__':
    main()
