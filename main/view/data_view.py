from flask import render_template, jsonify, request
from flask import current_app as app
import pandas as pd
import numpy as np
from ..controller import PlotlyController

@app.route('/test-data')
def test_data():
    id = request.args.get('id')

    data = PlotlyController.get_test_data(id)
    dataframe = data.to_json()

    return dataframe
