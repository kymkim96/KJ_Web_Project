from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import numpy as np
import plotly.express as px
import plotly
import json
import pickle
from ..controller import PlotlyController


@app.route("/plotly")
def plotly_test():
    name = request.args.get('name')
    description = request.args.get('description')
    title = request.args.get('title')
    value = request.args.get('value')
    index = request.args.get('index')

    title = f'{title}별 {value}'

    data = PlotlyController.get_data(name, description)

    if (str(type(data)) == "<class 'str'>"):
        if (data == "잘못된 접근입니다"):
            return data;

    column_name = data.columns[1]
    data.set_index(name, inplace=True)
    data.sort_values(column_name, ascending=False, inplace=True)

    # df_cumsum = data.cumsum()
    # baseline = df_cumsum.iloc[-1, -1] * 0.9
    # # print(data)
    # df_cumsum.loc[df_cumsum[column_name] <= baseline]

    fig = px.bar(data[:30], title=title,
                 labels={'value': value, 'index': index}, width=800, height=400)
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json

@app.route("/plotly-predict")
def plotly_predict():
    id = request.args.get('id')

    plot_json = ''

    with open("./main/static/model/re_lgbm_model.model", 'rb') as f:
        model = pickle.load(f)

        data = PlotlyController.get_proba(id)
        proba_list = data.iloc[:, 1:].to_numpy()
        df = model.predict_proba(proba_list)
        df = pd.DataFrame(df)
        df = df.T
        df['class'] = ['위법 아님', '위법']
        df.rename({0: 'proba'}, axis=1, inplace=True)
        fig = px.pie(df, values='proba', names='class', title='위법물 예측')
        plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return plot_json


@app.route("/plotly-map")
def plotly_map():
    table = request.args.get('table')

    data = PlotlyController.get_map(table)
    plot_map = data.drop(['MyUnknownColumn'], axis=1)
    fig = px.scatter_geo(plot_map, locations="CountryCode", color="CountryName",
                         hover_name="CountryName", size="pop",
                         projection="natural earth")
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json