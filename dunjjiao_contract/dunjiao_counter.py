# -*- coding: utf-8 -*-
from contract import BaseContract


def main():
    # 计算器
    contract = input(u'输入到手金额')
    cycle = input(u'输入期数')
    rate = input(u'输入月利率')

    base_contract = BaseContract(cycle, rate, contract)
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
