from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
import pickle
from ..controller import PlotlyController


@app.route('/')
def home():
    # with open("./main/static/model/최종모델.model", 'rb') as f:
    #     data = pickle.load(f)
    #     print(data.feature_importances_)
    return render_template('layout_si.jinja2', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': 'active',
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('발송국가/수출국가 코드', 'IMP_CNT_OF_DISPATCH_EXP_CD_15'),
        ('원산지', 'IMP_COUNTRY_OF_ORIGIN_16'),
        ('상품의 위치', 'LOC_LOCATION_NAME_30'),
        ('상품의 위치 코드', 'OFF_CODE_30'),
        ('거래국가코드', 'IMP_TRADING_COUNTRY_11')
    ]), sub_index_list=[], init_list=['발송국가/수출국가 코드', 'IMP_CNT_OF_DISPATCH_EXP_CD_15'])

@app.route('/location')
def location():
    return render_template('layout_si.jinja2', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': 'active',
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('발송국가/수출국가 코드', 'IMP_CNT_OF_DISPATCH_EXP_CD_15'),
        ('원산지', 'IMP_COUNTRY_OF_ORIGIN_16'),
        ('상품의 위치', 'LOC_LOCATION_NAME_30'),
        ('상품의 위치 코드', 'OFF_CODE_30'),
        ('거래국가코드', 'IMP_TRADING_COUNTRY_11')
    ]), sub_index_list=[], init_list=['발송국가/수출국가 코드', 'IMP_CNT_OF_DISPATCH_EXP_CD_15'])

@app.route('/rep')
def rep():
    return render_template('layout_si.jinja2', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': 'active',
        'person': None
    }, classification_list=enumerate([
        ('관세사 식별번호', 'REP_TIN_54'),
        ('관세사 이름', 'PERSON_NAME_54'),
    ]), sub_index_list=[1], init_list=['관세사 식별번호', 'REP_TIN_54'])
