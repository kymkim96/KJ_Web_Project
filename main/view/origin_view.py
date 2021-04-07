from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import plotly.express as px
import plotly
import json
from ..controller import OriginController


@app.route("/plotly-test")
def plotly_test():
    data = OriginController.get_data()

    data.set_index('IDG_COUNTRY_OF_ORIGIN_34', inplace=True)
    data.sort_values('count', ascending=False, inplace=True)
    fig = px.bar(data, title="원산지 별 적발 건수",
                 labels={'value': '적발건수', 'index': '품목의 원산지'})
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json