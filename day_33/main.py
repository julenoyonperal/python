# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:56:52 2021

@author: joyon
"""

import requests as rq

response = rq.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

data["iss_position"]