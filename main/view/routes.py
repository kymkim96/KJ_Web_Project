from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
from ..controller import OriginController


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
    a = OriginController.get_data()
    for items in a:
        for index, item in enumerate(items):
            result[columns[index]] = item
    print(result)
    return jsonify(result)

