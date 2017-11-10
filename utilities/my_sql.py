# coding=UTF-8
import db


# 获取customer_id
def select_customer(name):
    detail = db.execute("SELECT id,mobile1,card_no,annual_income,email FROM zsph_customer where name = %s ",
               params=name)
    return detail


def clear_customer(customer_id):
    db.execute("DELETE FROM zsph_job where customer_id = %s ", params=customer_id)
    # db.execute("DELETE FROM zsph_linkman where customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_loan where customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_risk_warning where customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_customer where id = %s ", params=customer_id)


# 获取customer_amount数量
def customer_amount():
    amount = db.execute("select count(*) from zsph_customer where create_by='f91cd39638354270a71fc6189270d34d'")
    return amount['count(*)']


# customer_job详情
def customer_job(customer_id):
    detail = db.execute("SELECT name, addr, tel_zone, tel, department, position FROM zsph_job where customer_id = %s ",
                        params=customer_id)
    return detail


# customer_linkman详情
def customer_linkman(customer_id):
    detail = db.execute("SELECT name, tel, addr, position, work_unit FROM zsph_linkman where customer_id = %s ",
                        params=customer_id)
    return detail


# customer_loan详情
def customer_loan(customer_id):
    detail = db.execute("SELECT type, repayment_quota, cycle, apply_quota FROM zsph_loan where customer_id = %s ",
                        params=customer_id)
    return detail


# loan数量
def loan_amount():
    amount = db.execute("select count(*) from zsph_loan where create_by='f91cd39638354270a71fc6189270d34d'")
    return amount['count(*)']




