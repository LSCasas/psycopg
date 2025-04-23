import db

def get_all_customers():
    columns = ["customer_id", "first_name","email", "active",  "last_name"]
    return db.select(columns, "customer")
    

def get_customers(ids):
    table = "customer"
    columns = ["customer_id", "first_name","email", "active",  "last_name"]
    where = ("customer_id", "in", str(tuple(ids)))
    return db.select(columns, "customer", where )

def get_customer(customer_id):
    table = "customer"
    columns = ["customer_id", "first_name","email", "active",  "last_name"]
    where = ("customer_id", "=", customer_id)
    return db.select(columns, "customer", where )


def get_customers_by_status(status = True):
    table = "customer"
    columns = ["customer_id", "first_name","email", "active",  "last_name"]
    where = ("active", "=", int(status))
    return db.select(columns, "customer", where )

    