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

    data = PlotlyController.get_data(name, description)
    data.set_index(name, inplace=True)
    data.sort_values('count', ascending=False, inplace=True)
    fig = px.bar(data, title="원산지 별 적발 건수",
                 labels={'value': '적발건수', 'index': '품목의 원산지'})
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json