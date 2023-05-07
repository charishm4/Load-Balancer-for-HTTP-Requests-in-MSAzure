from flask import Flask
import requests
import sys
import os

app = Flask(__name__)

# Enter the ip address of the VM
url1="http://104.41.211.213:8080"
url2="http://40.85.126.76:8080"

load_server1 = ""
load_server2 = ""

@app.route('/')
def func():
        global load_server1, load_server2
        load_server1 = requests.get("http://104.41.211.213:8080/load").content
        load_server2 = requests.get("http://40.85.126.76:8080/load").content       
        if float(load_server1) > float(load_server2):
                response = requests.get(url=url1)
                return str(response.content)
        elif float(load_server1) <= float(load_server2):
                response = requests.get(url=url2)
                return str(response.content)
        else:
                return "Not Found", 404

if __name__== "__main__":
        app.run(host='0.0.0.0',port=8080)
