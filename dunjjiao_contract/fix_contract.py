# coding=UTF-8

from contract import BaseContract, get_date
from db_contract import DbContract


def main():
    # 修改逾期
    # date开始逾期的日期
    print(u'开始')
    rate = input(u'输入月利率')
    cycle = input(u'输入期数')
    contract = input(u'输入到手金额')
    start_period_no = input(u'开始逾期期数')
    over_period_no = input(u'结束逾期期数')
    date = '2018-10-09'
    customer_id = '00302cf5aee24cfd91ceaf248d23753a'
    base_contract = BaseContract(cycle, rate, contract)
    # 剩余本金
    remain_principal = base_contract.sum_remain_principal()
    # 应还款额
    monthly_repay = base_contract.monthly_repay()
    # repayment_id
    repayment_ids = DbContract().select_repayment_id(customer_id)
    # 开始期逾期日期
    count = range(start_period_no, over_period_no + 1)
    fix_date = get_date(date, len(count))[0]
    for i in count:
        DbContract().update_repayment(fix_date[i - start_period_no], monthly_repay, remain_principal[i],
                                      repayment_ids[i-1]['id'])

    print(u'结束')


if __name__ == '__main__':
    main()
