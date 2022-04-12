# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 15:41:32 2022

@author: User
"""

import numpy as np
import streamlit as st
import pickle
model = pickle.load(open('object_detection.py', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def predict():
    """
    For rendering result on the HTML page
    
    """
    uploded_models = {}
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    uploaded_models.append(final_features)
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='the objects found{}'.format(output))
    return render_template('index.html', search_query="The object found in the video  is ".format(x))

@app.route('/search',methods=['POST'])
def search():
    x=0
    for x in uploaded_models:
        return x
    else:
        print('No records match your query')

if __name__=="__main__":
    app.run(debug=True)
