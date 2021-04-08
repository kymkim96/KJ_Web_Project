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
    return render_template('layout.jinja2', data={'inner': '1'})
