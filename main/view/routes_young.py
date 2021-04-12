from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
import pickle
from ..controller import PlotlyController


@app.route('/currency')
def currency():
    return render_template('layout_young.html', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': 'active',
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('총거래금액 (타직화폐기준)', 'VAL_FINANCIAL_VALUE_12'),
        ('화폐단위 (타직화폐)', 'VAL_CURRENCY_12'),
        ('화물총액 (계약통화기준)', 'TOT_FINANCIAL_VALUE_22'),
        ('화폐단위', 'TOT_CURRENCY_22'),
        ('환율', 'IMP_EXCHANGE_RATE_23'),
        ('계산된 세액', 'PAM_FINANCIAL_VALUE_47'),
        ('납부수단', 'CAL_METHOD_OF_PAYMENT_47')

    ]), sub_index_list=[], init_list=['총거래금액 (타직화폐기준)', 'VAL_FINANCIAL_VALUE_12'])

@app.route('/dnt')
def dnt():
    return render_template('layout_young.html', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': 'active',
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('수입자납세자식별번호', 'DNT_TIN_14'),
        ('신고자 / 대표자 국적', 'DNT_COUNTRY_14'),
        ('신고자 / 대표자 주소', 'DNT_ADDR_14')
    ]), sub_index_list=[], init_list=['수입자납세자식별번호', 'DNT_TIN_14'])
