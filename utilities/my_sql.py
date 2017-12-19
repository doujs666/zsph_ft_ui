# coding=UTF-8
import db


# 获取customer_id
def select_customer(name):
    detail = db.execute("SELECT id,mobile1,card_no,annual_income,email,apply_state FROM zsph_customer where name = %s ",
                        params=name)
    return detail


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


def clear_customer(customer_id):
    db.execute("DELETE FROM zsph_job where customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_linkman where customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_loan where customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_risk_warning where customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_customer where id = %s ", params=customer_id)


# 清除信用报告
def clear_credit_report(customer_id):
    db.execute("DELETE FROM zsph_credit_report where customer_id = %s ", params=customer_id)


# 清除电核，网核信息
def clear_info_verify(customer_id):
    db.execute("DELETE FROM zsph_info_verify where customer_id = %s ", params=customer_id)


# 更新信审专员信审结论
def update_contract_form(customer_id):
    db.execute(
        "UPDATE zsph_loan SET audit_type = null, audit_cycle = null, audit_rate = null, remarks = null, autid_actual_quota = null where customer_id = %s",
        params=customer_id)
    db.execute("UPDATE zsph_customer SET apply_state=15 WHERE id=%s", params=customer_id)


# 获取信审专员信审结论
def get_contract_form(customer_id):
    detail = db.execute(
        "SELECT audit_type,audit_cycle,audit_rate,autid_actual_quota FROM zsph_loan where customer_id = %s ",
        params=customer_id)
    return detail


# 获取信审主管信审结论
def get_manager_contract_form(customer_id):
    detail = db.execute("SELECT type,cycle,rate,actual_quota,remarks FROM zsph_contract where customer_id = %s ",
                        params=customer_id)
    return detail


# 更新信审主管信审结论
def update_manager_contract_form(customer_id):
    db.execute(
        "UPDATE zsph_contract SET type = null, cycle = null, rate = null, remarks = null, actual_quota = null, governor_id=null, decision_date=null where customer_id = %s",
        params=customer_id)
    db.execute("UPDATE zsph_customer SET apply_state=20 WHERE id=%s", params=customer_id)


# 清除contract数据
def clear_contract(customer_id):
    db.execute("DELETE FROM zsph_contract where customer_id = %s ", params=customer_id)


# 清除合同信息
def clear_sign_page(customer_id):
    db.execute("UPDATE zsph_contract SET bank_account ='' WHERE customer_id = %s ", params=customer_id)
    db.execute("DELETE FROM zsph_contract_child where customer_id='' %s", params=customer_id)
    db.execute("UPDATE zsph_contract SET sign_flag =0 WHERE customer_id = %s ", params=customer_id)
    db.execute("UPDATE zsph_customer SET apply_state =25 WHERE id = %s ", params=customer_id)


# 获取sign_flow
def get_sign_flag(customer_id):
    sign_flag = db.execute("SELECT sign_flag FROM zsph_contract  WHERE customer_id = %s ", params=customer_id)
    return sign_flag


# 获取loan_id
def get_loan_id(customer_id):
    loan_id = db.execute("SELECT id FROM zsph_loan  WHERE customer_id = %s ", params=customer_id)
    return loan_id


# clear员工账号
def clear_user_account(login_name):
    db.execute("delete FROM sys_user where login_name= %s", params=login_name)
