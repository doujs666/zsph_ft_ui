import db

def select_customer(name):
    detail = db.execute("SELECT id,mobile1,card_no,annual_income,email FROM zsph_customer where name = %s ",
               params=name)

    return detail

def clear_customer(id):
    db.execute("DELETE FROM zsph_customer where id = %s ",
               params=id)

def customer_amount():
    amount = db.execute("select count(*) from credit_test.zsph_customer where create_by='f91cd39638354270a71fc6189270d34d'")
    return amount['count(*)']
