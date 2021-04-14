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
    # data = PlotlyController.get_test_data()
    return render_template('home.jinja2', active={
        'model': 'active',
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, test_list=['first', 'second', 'third', 'forth', 'fifth'])

@app.route('/trd')
def trd():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': 'active',
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('화주', 'TRD_NAME_2'),
        ('화주 국적', 'TRD_COUNTRY_2'),
        ('화주 주소', 'TRD_ADDR_2'),
        ('신고번호', 'CUS_REF_NO_7'),
        ('장소 및 날짜', 'IMP_DATE_OF_DECLARATION_54')
    ]), sub_index_list=[], init_list=['화주', 'TRD_NAME_2'],
        country_list=[('AE', 'UAE'), ('AF', 'Afghanistan'), ('AT', 'Austria'), ('BE', 'Belgium'),
                      ('BY', 'Belarus'), ('CN', 'China'), ('EE', 'Estonia'), ('FR', 'France'),
                      ('GE', 'Georgia'), ('HR', 'Croatia'), ('IN', 'India'), ('IR', 'Iran'),
                      ('IT', 'Italy'), ('KG', 'Kyrgyzstan'), ('KR', 'Korea'), ('KZ', 'Kazakhstan'),
                      ('LT', 'Lithuania'), ('LV', 'Latvia'), ('NO', 'Norway'), ('PK', 'Pakistan'),
                      ('PT', 'Portugal'), ('RO', 'Romania'), ('RU', 'Russia'), ('TR', 'Turkey'),
                      ('UZ', 'Uzbekistan')])

@app.route('/total')
def total():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': 'active',
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('총수량', 'CUS_TOTAL_NUMBER_OF_ITEMS_5'),
        ('총중량', 'CUS_TOTAL_NUMBER_OF_PACKAGES_6')
    ]), sub_index_list=[], init_list=['총수량', 'CUS_TOTAL_NUMBER_OF_ITEMS_5'],
        country_list=[])

@app.route('/con')
def con():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': 'active',
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('수령인', 'CON_NAME_8'),
        ('수령인 국적', 'CON_COUNTRY_8'),
        ('수령인 주소 ', 'CON_ADDR_8'),
        ('수입자납세자식별번호', 'CON_TIN_8')
    ]), sub_index_list=[0], init_list=['수령인', 'CON_NAME_8'],
        country_list=[('AF', 'Afghanistan'), ('CN', 'China'),
                      ('KG', 'Kyrgyzstan'), ('TJ', 'Tajikistan')])

@app.route('/currency')
def currency():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': 'active',
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('총거래금액 (타직화폐기준)', 'VAL_FINANCIAL_VALUE_12'),
        ('화폐단위 (타직화폐)', 'VAL_CURRENCY_12'),
        ('화물총액 (계약통화기준)', 'TOT_FINANCIAL_VALUE_22'),
        ('화폐단위', 'TOT_CURRENCY_22'),
        ('환율', 'IMP_EXCHANGE_RATE_23'),
        ('계산된 세액', 'PAM_FINANCIAL_VALUE_47'),
        ('납부수단', 'CAL_METHOD_OF_PAYMENT_47')

    ]), sub_index_list=[], init_list=['총거래금액 (타직화폐기준)', 'VAL_FINANCIAL_VALUE_12'],
        country_list=[])

@app.route('/dnt')
def dnt():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': 'active',
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('수입자납세자식별번호', 'DNT_TIN_14'),
        ('신고자 / 대표자 국적', 'DNT_COUNTRY_14'),
        ('신고자 / 대표자 주소', 'DNT_ADDR_14')
    ]), sub_index_list=[], init_list=['수입자납세자식별번호', 'DNT_TIN_14'],
        country_list=[('TJ', 'Tajikistan')]
        )

@app.route('/delivery')
def delivery():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': 'active',
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('컨테이너', 'IMP_CONTAINER_FLAG_19'),
        ('운송조건', 'DEL_DELIVERY_TERM_CODE_20'),
        ('운송장소', 'DEL_PLACE_OF_DELIVERY_20'),
        ('국경에서의 운송 수단', 'IMP_INLAND_TRANSPORT_MODE_25'),
        ('국내 교통 수단', 'IMP_TRANSPORT_MODE_AT_BODR_26')
    ]), sub_index_list=[], init_list=['컨테이너', 'IMP_CONTAINER_FLAG_19'],
        country_list=[])


@app.route('/location')
def location():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': 'active',
        'item': None,
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('발송국가/수출국가 코드', 'IMP_CNT_OF_DISPATCH_EXP_CD_15'),
        ('원산지', 'IMP_COUNTRY_OF_ORIGIN_16'),
        ('상품의 위치', 'LOC_LOCATION_NAME_30'),
        ('상품의 위치 코드', 'OFF_CODE_30'),
        ('거래국가코드', 'IMP_TRADING_COUNTRY_11')
    ]),
       sub_index_list=[],
       init_list=['발송국가/수출국가 코드', 'IMP_CNT_OF_DISPATCH_EXP_CD_15'],
       country_list=[('AE', 'UAE'), ('AF', 'Afghanistan'), ('AT', 'Austria'), ('BE', 'Belgium'),
                     ('BY', 'Belarus'), ('CN', 'China'), ('EE', 'Estonia'), ('FR', 'France'),
                     ('GE', 'Georgia'), ('HR', 'Croatia'), ('IN', 'India'), ('IR', 'Iran'),
                     ('IT', 'Italy'), ('KG', 'Kyrgyzstan'), ('KR', 'Korea'), ('KZ', 'Kazakhstan'),
                     ('LT', 'Lithuania'), ('LV', 'Latvia'), ('NO', 'Norway'), ('PK', 'Pakistan'),
                     ('PT', 'Portugal'), ('RO', 'Romania'), ('RU', 'Russia'), ('TR', 'Turkey'),
                     ('TJ', 'Tajikistan'), ('UZ', 'Uzbekistan')])

@app.route('/item')
def item():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': 'active',
        'rep': None,
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('HS코드', 'COM_COMBINED_NOMENCLATURE_33'),
        ('해당품목의 원산지코드', 'IDG_COUNTRY_OF_ORIGIN_34'),
        ('품목의 순서번호', 'GDS_ITEM_NUMBER_32'),
        ('절차1', 'IDG_PROCEDURE_REQUESTED_37'),
        ('절차2', 'IDG_PREVIOUS_PROCEDURE_37'),
        ('절차3', 'IDG_ADD_NATIONAL_PROC_37'),
        ('해당품목의 관세부과방법', 'COV_CUST_VALUE_METHOD'),
        ('해당품목의 순중량 (kg)', 'IDG_NET_MASS_38'),
        ('해당품목의 총중량 (kg)', 'GDS_GROSS_MASS_35'),
        ('해당품목의 금액 (TJS)', 'COR_FINANCIAL_VALUE'),
        ('해당품목의 금액 단위', 'COR_CURRENCY'),
        ('화물장치공간 및 화물설명', 'GDS_GOODS_DESCRIPTION_31')
    ]), sub_index_list=[2,3], init_list=['화물장치공간 및 화물설명', 'GDS_GOODS_DESCRIPTION_31'],
        country_list=[('AE', 'UAE'), ('AT', 'Austria'), ('BE', 'Belgium'), ('BY', 'Belarus'),
                      ('CN', 'China'), ('DE', 'Germany'), ('FR', 'France'),
                      ('GE', 'Georgia'), ('HR', 'Croatia'), ('HU', 'Hungary'), ('IN', 'India'),
                      ('IR', 'Iran'), ('IT', 'Italy'), ('JP', 'Japan'), ('KG', 'Kyrgyzstan'),
                      ('KR', 'Korea'), ('KZ', 'Kazakhstan'), ('LT', 'Lithuania'), ('LV', 'Latvia'),
                      ('NO', 'Norway'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PT', 'Portugal'),
                      ('RO', 'Romania'), ('RU', 'Russia'), ('TR', 'Turkey'), ('TJ', 'Tajikistan'),
                      ('UZ', 'Uzbekistan')])

@app.route('/rep')
def rep():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': 'active',
        'person': None,
        'nation': None
    }, classification_list=enumerate([
        ('관세사 식별번호', 'REP_TIN_54'),
        ('관세사 이름', 'PERSON_NAME_54'),
    ]), sub_index_list=[1], init_list=['관세사 식별번호', 'REP_TIN_54'],
        country_list=[])

@app.route('/person')
def person():
    return render_template('layout_si.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': "active",
        'nation': None
    }, classification_list=enumerate([
        ('대리인', 'PERSON_POSITION_54'),
        ('참조 대리인', 'GEND_REFERENCE_54'),
        ('발행일 ','GEND_ISSUE_DATE_54'),
        ('접수일자','ACCEPTANCE_DATE')
    ]), sub_index_list=[], init_list=['대리인', 'PERSON_POSITION_54'],
        country_list=[])

@app.route('/nation')
def nation():
    return render_template('country.jinja2', active={
        'model': None,
        'trd': None,
        'total': None,
        'con': None,
        'currency': None,
        'dnt': None,
        'delivery': None,
        'location': None,
        'item': None,
        'rep': None,
        'person': None,
        'nation': 'active'
    })
