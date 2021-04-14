from ..model.config import conn_mysqldb
from ..util import TestData
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

# 검증 데이터 생성
def get_test_data():
    conn = conn_mysqldb()
    sql = "select * from test_set"
    data = pd.read_sql(sql, conn)

    # 레이블 인코딩 및 스케일링
    with open("./main/static/model/le.model", 'rb') as f:
        # TODO: 레이블 인코딩
        pass
    with open("./main/static/model/sc.model", 'rb') as f:
        # TODO: 스케일링
        pass

    # 파생변수 추가
    sql = "select * from pasang"
    pasang = pd.read_sql(sql, conn)
    # TODO: 전처리 데이터에 파생변수 추가

    conn.close()
    return data

def get_proba(id):
    conn = conn_mysqldb()
    sql = f"select * from test_set where id={id}"
    data = pd.read_sql(sql, conn)
    conn.close()
    return data

def get_map():
    conn = conn_mysqldb()
    sql = f"select * from maps"
    data = pd.read_sql(sql, conn)
    conn.close()
    return data