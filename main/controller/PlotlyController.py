from ..model.config import conn_mysqldb
import pandas as pd


def get_data(name, description):
    conn = conn_mysqldb()
    # cursor = conn.cursor()
    sql = f"select * from {name}_{description}"
    # cursor.execute(sql)
    data = pd.read_sql(sql, conn)
    # data = cursor.fetchall()
    conn.close()
    return data

def create_table():
    conn = conn_mysqldb()
    cursor = conn.cursor()
    columns_str = [
        'IMP_TYPE_OF_DECLARATION_1',
       'TRD_NAME_2', 'TRD_COUNTRY_2', 'TRD_ADDR_2',
       'CUS_REF_NO_7', 'CON_TIN_8',
       'CON_NAME_8', 'CON_COUNTRY_8', 'CON_ADDR_8', 'PER_TIN_9', 'PER_NAME_9',
       'PER_COUNTRY_9', 'PER_ADDR_9']
    columns_int = [
        'CUS_TOTAL_NUMBER_OF_ITEMS_5', 'CUS_TOTAL_NUMBER_OF_PACKAGES_6'
    ]
    for col in columns_str:
        sql = f"""
        create table {col}_ill_count (
            {col} TEXT,
            count int
        )
        """
        cursor.execute(sql)
    for col in columns_int:
        sql = f"""
        create table {col}_ill_count (
            {col} TEXT,
            count int
        )
        """
        cursor.execute(sql)