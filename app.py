# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:59:35 2021

@author: Yash
"""

import numpy as np
import pandas as pd
from math import ceil, isnan
import seaborn as sns
import folium
import geopy
from pickle import load, dump
from flask import Flask, request, render_template
from flasgger import Swagger
from predict import predict
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return "Welcome to Maverick!!!"

@app.route('/recommend')
def registration_process():
    
    """ To get recommendations for a particular wholesaler, you need to enter the wholesaler ID.
    ---
    parameters:
        - name: name
          in: query
          type: string
          required: true
        - name: phone
          in: query
          type: number
          required: true
        - name: wholesaler_id
          in: query
          type: number
          required: true
          
    responses:
        200:
            description: The output values
        
    """
    name = request.args.get('name')
    phone = request.args.get('phone')
    user_id = request.args.get('wholesaler_id')
    amount, recommendations, map_ = predict(int(user_id))
    text = "We would like to recommend the wholesaler, " +str((int(amount))) + " HL of beverage with following material id: \n\n"
    for i in recommendations:
        text = text + "\n" + str(i)
    with open("output.txt", "a") as f:
        f.write(text)
    print(recommendations)
    map_.save('templates/map.html')
    return text
    #return map_._repr_html_()

@app.route('/map')
def map_display():
    return render_template('map.html')


if __name__ == '__main__':
    app.run()