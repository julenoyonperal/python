# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:43:08 2021

@author: JOyon
"""

from flask import Flask

app = Flask(__name__)

@app.route('/hola/')
def hello_world():
    return "Hello World"