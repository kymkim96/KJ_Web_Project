from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
import pickle
from ..controller import PlotlyController


@app.route('/item')
def item():
    return render_template('layout_seo.html', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': 'active',
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('화물장치공간 및 화물설명', 'GDS_GOODS_DESCRIPTION_31'),
        ('품목의 순서번호', 'GDS_ITEM_NUMBER_32'),
        ('HS코드', 'COM_COMBINED_NOMENCLATURE_33'),
        ('해당품목의 원산지코드', 'IDG_COUNTRY_OF_ORIGIN_34'),
        ('해당품목의 총중량 (kg)', 'GDS_GROSS_MASS_35'),
        ('절차1', 'IDG_PROCEDURE_REQUESTED_37'),
        ('절차2', 'IDG_PREVIOUS_PROCEDURE_37'),
        ('절차3', 'IDG_ADD_NATIONAL_PROC_37'),
        ('해당품목의 순중량 (kg)', 'IDG_NET_MASS_38'),
        ('해당품목의 금액 (TJS)', 'COR_FINANCIAL_VALUE'),
        ('해당품목의 금액 단위', 'COR_CURRENCY'),
        ('해당품목의 관세부과방법', 'COV_CUST_VALUE_METHOD')
    ]), sub_index_list=[2,3], init_list=['발송국가/수출국가 코드', 'IMP_CNT_OF_DISPATCH_EXP_CD_15'])
#
# @app.route('/rep')
# def rep():
#     return render_template('layout_si.jinja2', active={
#         'trd': None,
#         'total': None,
#         'con': None,
#         'currency': None,
#         'dnt': None,
#         'delivery': None,
#         'location': None,
#         'item': None,
#         'rep': 'active',
#         'person': None
#     }, classification_list=enumerate([
#         ('관세사 식별번호', 'REP_TIN_54'),
#         ('관세사 이름', 'PERSON_NAME_54'),
#     ]), sub_index_list=[1], init_list=['관세사 식별번호', 'REP_TIN_54'])
