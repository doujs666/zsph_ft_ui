# coding=UTF-8
import db


def select_customer(name):
    detail = db.execute("SELECT id,mobile1,card_no,annual_income,email FROM zsph_customer where name = %s ",
               params=name)
    return detail

# def clear_customer(id):
#     db.execute("DELETE FROM zsph_customer where id = %s ",
#                params=id)


def customer_amount():
    amount = db.execute("select count(*) from zsph_customer where create_by='f91cd39638354270a71fc6189270d34d'")
    return amount['count(*)']


def customer_job(customer_id):
    detail = db.execute("SELECT name, addr, tel_zone, tel, department, position FROM zsph_job where customer_id = %s ",
                        params=customer_id)
    return detail


def customer_linkman(customer_id):
    detail = db.execute("SELECT name, tel, addr, position, work_unit FROM zsph_linkman where customer_id = %s ",
                        params=customer_id)
    return detail


def customer_loan(customer_id):
    detail = db.execute("SELECT type, repayment_quota, cycle, apply_quota FROM zsph_loan where customer_id = %s ",
                        params=customer_id)
    return detail


# loan数量
def loan_amount():
    amount = db.execute("select count(*) from zsph_loan where create_by='f91cd39638354270a71fc6189270d34d'")
    return amount['count(*)']



