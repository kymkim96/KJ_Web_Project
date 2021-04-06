from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
from controller import TestController


@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/data1?key=id')
def data1():
    columns = [
        'COM_COMBINED_NOMENCLATURE_33',
        'COM_COMBINED_NOMENCLATURE_33_ratio',
        'CON_ADDR_8',
        'CON_ADDR_8_ratio',
        'CON_NAME_8',
        'CON_NAME_8_ratio',
        'CUS_TOTAL_NUMBER_OF_ITEMS_5',
        'CUS_TOTAL_NUMBER_OF_ITEMS_5_ratio',
        'GDS_GROSS_MASS_35',
        'GDS_GROSS_MASS_35_ratio',
        'PERSON_NAME_54',
        'PERSON_NAME_54_ratio',
        'STC_FINANCIAL_VALUE_46',
        'STC_FINANCIAL_VALUE_46_ratio',
        'id',
        'y'
    ]
    result = {}
    a = TestController.get_data()
    for items in a:
        for index, item in enumerate(items):
            result[columns[index]] = item
    print(result)
    return jsonify(result)


@app.route("/plotly-test")
def plotly_test():
    columns = [
        'COM_COMBINED_NOMENCLATURE_33',
        'COM_COMBINED_NOMENCLATURE_33_ratio',
        'CON_ADDR_8',
        'CON_ADDR_8_ratio',
        'CON_NAME_8',
        'CON_NAME_8_ratio',
        'CUS_TOTAL_NUMBER_OF_ITEMS_5',
        'CUS_TOTAL_NUMBER_OF_ITEMS_5_ratio',
        'GDS_GROSS_MASS_35',
        'GDS_GROSS_MASS_35_ratio',
        'PERSON_NAME_54',
        'PERSON_NAME_54_ratio',
        'STC_FINANCIAL_VALUE_46',
        'STC_FINANCIAL_VALUE_46_ratio',
        'id',
        'y'
    ]
    result = {}
    data = TestController.get_data()
    # for items in a:
    #     for index, item in enumerate(items):
    #         result[columns[index]] = item

    # df = pd.DataFrame(data)
    # contain_df = data.y.value_counts()
    # fig = px.pie(contain_df, values=contain_df, names=["미적발", "적발"],
    #              title="위법물 건발률")
    data.set_index('origin_country', inplace=True)
    data.sort_values('IDG_COUNTRY_OF_ORIGIN_34', ascending=False, inplace=True)
    print(data.values)
    fig = px.bar(data, title="원산지 별 적발 건수",
                 labels={'value': '적발건수', 'index': '품목의 원산지'})
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json
