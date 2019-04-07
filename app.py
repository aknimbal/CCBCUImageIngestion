
#directives

import pandas as pd
import json
import flask, flask_restplus, flask_jwt
import flask_jwt
import requests
import sqlalchemy
import datetime
import pytz
import pyodbc
import AzQueue as azconn
from datetime import timedelta
from sqlalchemy import create_engine
from flask_jwt import JWT
from flask import Flask, Blueprint, Response
from flask_restplus import Resource, Api
from pandas.io.json import json_normalize
# from azure.storage.queue import QueueService
#end of directives

app = Flask(__name__)

@app.route("/")
def home():         
    azureQueueAccountName = "ccbcustorage"
    azureQueueKey = "9Mg7JNNHVukysJgENg7XkWcf3egUgwNfQq25qZqftKkBR5IK1pzOiPSd9cb5cYS493aB5MwlHswVTMRJmD15cQ=="
    azureQueueAnalysisResults = "analysis-process-akshay"
    queue_service = azconn.load(azureQueueAccountName, azureQueueKey,azureQueueAnalysisResults)
    azconn.put_in_queue(queue_service,azureQueueAnalysisResults,page_parse())
    #boot up an instance of AKS to process queue items
    
    return("CCBCU Image ingestion service with queue using facet...!!!")


def page_parse():
    page_list = []
    page_list.append('https://pybuildproduct.azurewebsites.net/getpages')
    base_url = 'https://pybuildproduct.azurewebsites.net/getpages'
    base = "https://services.traxretail.com"
    apikey = ""
    headers = {"Authorization": apikey}
    r = requests.get(base_url, headers=headers)
    page_list.append('https://pybuildproduct.azurewebsites.net/getpages2')

    return page_list