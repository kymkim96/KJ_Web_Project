from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
import pickle
from ..controller import PlotlyController


@app.route('/delivery')
def delivery():
    return render_template('layout_bong.html', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': 'active',
        'location': None,
        'item': None,
        'rep': None,
        'person': None
    }, classification_list=enumerate([
        ('컨테이너', 'IMP_CONTAINER_FLAG_19'),
        ('운송조건', 'IMP_COUNTRY_OF_ORIGIN_16'),
        ('운송장소', 'DEL_PLACE_OF_DELIVERY_20'),
        ('국경에서의 운송 수단', 'IMP_INLAND_TRANSPORT_MODE_25'),
        ('국내 교통 수단', 'IMP_TRANSPORT_MODE_AT_BODR_26')
    ]), sub_index_list=[], init_list=['컨테이너', 'IMP_CONTAINER_FLAG_19'])

@app.route('/person')
def person():
    return render_template('layout_bong.html', active={
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': "active"
    }, classification_list=enumerate([
        ('대리인', 'PERSON_POSITION_54'),
        ('참조 대리인', 'GEND_REFERENCE_54'),
        ('발행일 ','GEND_ISSUE_DATE_54'),
        ('접수일자','ACCEPTANCE_DATE')
    ]), sub_index_list=[], init_list=['대리인', 'PERSON_POSITION_54'])
