#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 01:42:11 2018

@author: varunnukala
"""

from flask import Flask, request, render_template, render_template_string
import pandas as pd
import numpy as np
import csv
import json


app = Flask(__name__)

'''
@app.route('/')
def hello():
    return 'Hellar, World!' ''' 
    
@app.route('/')
def my_form():
    return render_template('index.html')





def Filter (Gender, Conditions):
    
    search = pd.read_csv('SearchResults-2.csv',encoding='latin1')
    search2 = search.copy()
    search3 = search2[search2['Status'].isin(['Recruiting'])]
    search4 = search3[search3['Gender'].isin([Gender, 'All'])]
    search5 = search4[search4['Conditions'].str.contains(Conditions)]
    searchFinal = search5.drop(search5.columns[[0, 1, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25]], axis=1)
    searchFinal
    searchFinal.to_csv('out.csv')
    with open('out.csv') as f:
        s = f.read() + '\n' # add trailing new line character

    searchFinal = repr(s)  
    #searchFinal.to_json('file.json')
    #dic = json.dumps('file.json')
    #df = pd.read_csv('out.csv')
    #df.to_html('your_file.html')
    
    return searchFinal
    

@app.route('/', methods=['POST'])
def my_form_post():
    
    
    if request.form['submit_button'] == 'csv':
        text = request.form['text']
        text2 = request.form['text2']
        #processed_text = text.upper()
        #lol = text.split(',')
        processed_text = Filter(text, text2)
        #processed_text = Filter('Male', 'Cancer')
        
        
        return processed_text
    
    
    if request.form['submit_button'] == 'map':
        return render_template('map.html')
    
    #return render_template('map.html')





if __name__ == "__main__":
    
    app.run()
   