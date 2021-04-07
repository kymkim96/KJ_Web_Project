from ..model.config import conn_mysqldb
import pandas as pd


def get_data():
    conn = conn_mysqldb()
    # cursor = conn.cursor()
    sql = "select * from origin_ill_count"
    # cursor.execute(sql)
    data = pd.read_sql(sql, conn)
    # data = cursor.fetchall()
    conn.close()
    return data
