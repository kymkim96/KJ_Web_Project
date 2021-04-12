from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
import pickle
from ..controller import PlotlyController


@app.route('/trd')
def trd():
    return render_template('layout_ji.html', active={
        'trd': 'active',
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('화주', 'TRD_NAME_2'),
        ('화주 국적', 'TRD_COUNTRY_2'),
        ('화주 주소', 'TRD_ADDR_2'),
        ('신고번호', 'CUS_REF_NO_7'),
        ('장소 및 날짜', 'IMP_DATE_OF_DECLARATION_54')
    ]), sub_index_list=[], init_list=['화주', 'TRD_NAME_2'])

@app.route('/total')
def total():
    return render_template('layout_ji.html', active={
        'trd': None,
        'total': 'active',
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('총수량', 'CUS_TOTAL_NUMBER_OF_ITEMS_5'),
        ('총중량', 'CUS_TOTAL_NUMBER_OF_PACKAGES_6')
    ]), sub_index_list=[1], init_list=['총수량', 'CUS_TOTAL_NUMBER_OF_ITEMS_5'])

@app.route('/con')
def con():
    return render_template('layout_ji.html', active={
        'trd': None,
        'total': None,
        'con': 'active',
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('수령인', 'CON_NAME_8'),
        ('수입자납세자식별번호', 'CON_TIN_8'),
        ('수령인 국적', 'CON_COUNTRY_8'),
        ('수령인', 'CON_ADDR_8'),
        ('수령인 주소', 'CON_TIN_8')
    ]), sub_index_list=[1], init_list=['수령인', 'CON_NAME_8'])
