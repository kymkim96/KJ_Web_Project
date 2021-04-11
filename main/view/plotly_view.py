from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
from ..controller import PlotlyController


@app.route("/plotly")
def plotly_test():
    name = request.args.get('name')
    description = request.args.get('description')
    title = request.args.get('title')
    value = request.args.get('value')
    index = request.args.get('index')

    title = f'{title} 별 {value}'

    data = PlotlyController.get_data(name, description)
    column_name = data.columns[1]
    data.set_index(name, inplace=True)
    data.sort_values(column_name, ascending=False, inplace=True)
    fig = px.bar(data, title=title,
                 labels={'value': value, 'index': index})
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json