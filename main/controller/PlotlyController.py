from ..model.config import conn_mysqldb
import pandas as pd


def get_data(name, description):
    conn = conn_mysqldb()
    # cursor = conn.cursor()
    sql = f"select * from {name}_{description}"
    # cursor.execute(sql)
    error_ = None
    try:
        data = pd.read_sql(sql, conn)
    except:
        data = "잘못된 접근입니다"
    # data = cursor.fetchall()
    conn.close()
    return data

def get_proba(id):
    conn = conn_mysqldb()
    # sql = f"select * from test_set where id={id}"
    data = pd.read_sql(sql, conn)
    conn.close()
    return data

def get_map():
    conn = conn_mysqldb()
    sql = f"select * from maps"
    data = pd.read_sql(sql, conn)
    conn.close()
    return data