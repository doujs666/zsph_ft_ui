# coding=UTF-8
from utilities import db


class DbContract(object):

    # 获取repayment_id
    def select_repayment_id(self, customer_id):
        repayment_id = db.execute(
            "SELECT id FROM zsph_repayment where customer_id = %s ",
            params=customer_id, is_fetchone=False)
        return repayment_id

    # 更新repayment
    def update_repayment(self, date, monthly_repay, remain_principal, repayment_id, ):
        value = (date, monthly_repay, remain_principal, repayment_id)
        db.execute(
            "UPDATE zsph_repayment SET due_date=%s, monthly_repay=%s, remain_principal=%s, repayment_status='2' WHERE ID=%s",
            params=value)
