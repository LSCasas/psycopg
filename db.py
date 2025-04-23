import psycopg

CONN_STRING = "dbname=dvdrental user=postgres password=postgres host=localhost"

def select(columns, table, where=None):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            column_list = ", ".join(columns)
            
            
            where_string = f"WHERE {where[0]} {where[1]} {where[2]}" if where else ""
            query = f"SELECT {column_list} FROM {table} {where_string};"
            cur.execute(query)
            result = cur.fetchall()
    return result

def delete(table, where=None):
    conn = psycopg.connect(CONN_STRING)

    
    with conn.cursor() as cur:
        where_string = f"WHERE {where[0]} {where[1]} {where[2]}" if where else ""
        query = f"DELETE FROM {table} {where_string};"
        cur.execute(query)
        result = cur.fetchall()  
    
    cur.execute()
    conn.close()
    return result

def insert(table, columns, values: list):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            columns = str(tuple(columns))
            data = ", ".join([str(v) for v in values])
            query = f"INSERT INTO {table}{columns} VALUES{data}"

def update():
    table = "customer"
    column = "first_name"
    valor = "Pedro"
    value = f"'{valor}'" if isinstance(valor, str) else valor
    where = " ".join(('customer_id', "=", "3"))
    return f"UPDATE {table} SET {column} = {value} WHERE {where}"