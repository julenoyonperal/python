# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:26:55 2021

@author: JOyon
"""

import requests as rq
import os
from twilio.rest import Client

api_web = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = 'd2cae00c279a5b5329acd172311d7f40'
api_key_2 = '85ecec0302ea53fb7b6f89e88475444c'
parameters = {
    "lat" : 51.507351 ,
    "lon" : -0.127758,
    "exclude" : 'current,minutely,daily', 
     "appid" : api_key
    
    }
response = rq.get(api_web, params=parameters)
response.raise_for_status()
data = response.json()
weather = data["hourly"][:12]

will_rain = False
for hour_data in weather:
    condition_code = hour_data["weather"][0]["id"]
    
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring an umbrella")
    Print("we can put here the code to send an email")
    



# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACddb3353e393b610ba6db0e165f39eb0f"
auth_token = "622dccba4be383f370619ea13558d57f"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Te amo con todo my corazon. Tu admirador secreto.",
                     from_='+18576638571',
                     #to='+447562292131'
                     to='+447762142666'
                    )

print(message.sid)