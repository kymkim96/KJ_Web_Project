from ..model.config import conn_mysqldb
from ..util import preprocessing
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

# 검증 데이터의 원본 출력
def get_test_data(id):
    conn = conn_mysqldb()
    sql = f"select * from basedata where id={id}"
    data = pd.read_sql(sql, conn)

    conn.close()
    return data

# 검증 데이터 생성
def get_proba(id):
    conn = conn_mysqldb()
    sql = f"select * from basedata where id={id}"
    data = pd.read_sql(sql, conn)

    # 레이블 인코딩 및 스케일링
    df = preprocessing.inv_df(data)

    # 파생변수 추가
    sql = f"select * from pasang where id={id}"
    pasang = pd.read_sql(sql, conn)

    lgbm_df = df.merge(pasang, how="inner", on="id")

    conn.close()
    return lgbm_df

def get_map(table):
    conn = conn_mysqldb()
    sql = f"select * from {table}"
    data = pd.read_sql(sql, conn)
    conn.close()
    return data