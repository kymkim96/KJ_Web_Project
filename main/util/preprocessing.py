import pandas as pd

## 레이블 및 스케일링
def inv_df(df):
    import warnings
    import pickle
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import StandardScaler

    warnings.filterwarnings(action="ignore")

    le = LabelEncoder()
    sc = StandardScaler()

    col_list = ['id', 'CUS_TOTAL_NUMBER_OF_ITEMS_5', 'IMP_DATE_OF_DECLARATION_54',
                'CUS_TOTAL_NUMBER_OF_PACKAGES_6', 'TRD_NAME_2', 'IMP_EXCHANGE_RATE_23',
                'ACCEPTANCE_DATE', 'CUS_REF_NO_7', 'TOT_FINANCIAL_VALUE_22',
                'VAL_FINANCIAL_VALUE_12', 'GEND_REFERENCE_54', 'GEND_ISSUE_DATE_54',
                'COV_CUST_VALUE_METHOD', 'CON_ADDR_8', 'PERSON_POSITION_54',
                'TRD_ADDR_2', 'DEL_PLACE_OF_DELIVERY_20', 'LOC_LOCATION_NAME_30',
                'IMP_TRADING_COUNTRY_11']
    df = df[col_list]

    # 날짜 변수 문자열 변환 후 슬라이싱
    date_col = ["IMP_DATE_OF_DECLARATION_54", "GEND_ISSUE_DATE_54", "ACCEPTANCE_DATE"]
    for i in date_col:
        if i == "ACCEPTANCE_DATE":
            df[i] = df[i].astype("str").map(lambda x: x[3:5])
            df[i] = df[i].astype(int)
        else:
            df[i] = df[i].astype("str").map(lambda x: x[4:6])
            df[i] = df[i].astype(int)

    # 변수 이름 담을 리스트 생성
    le_col = []
    sc_col = []
    # id 빼면 1, 아니면 0
    for i in range(0, len(df.columns)):
        if (df[df.columns[i]].dtype == "object") | (i == 0):
            le_col.append(df.columns[i])

        else:
            sc_col.append(df.columns[i])

    # 변수명과 매핑하여 경로에 맞는 인코딩 모델 불러오기
    le_df = df[le_col]
    for i in le_df.columns:
        if i == 'id':
            continue
        with open("./main/static/model/final_le/le_date_{}.model".format(i), "rb") as f:
            le_model = pickle.load(f)
        # 레이블 인코딩 트랜스
        le_df[i] = le_model.transform(le_df[i])

    #
    sc_df = df[sc_col]
    for i in sc_df.columns:
        if i == 'id':
            continue
        with open("./main/static/model/final_sc/sc_date_{}.model".format(i), "rb") as f:
            sc_model = pickle.load(f)
        # 스케일링 트랜스
        sc_df[i] = sc_model.transform(sc_df[i].to_frame())

    con_df = pd.concat([le_df, sc_df], axis=1)
    con_df = con_df[col_list]

    return con_df
