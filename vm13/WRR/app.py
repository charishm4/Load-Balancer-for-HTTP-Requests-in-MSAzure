from flask import Flask , request, send_file, redirect, url_for, session
import requests
import sys
import os

servers = ['1', '2']
w1 = 1
w2 = 2

n=0
i=0
def get_servers():
        global n,i
        tw = w1 + w2
        if i %tw > w1:
                x = servers[0]
        else :
                x = servers[1]
        i = i + 1
        return x

app = Flask(__name__)

# Enter the Ip adrress of your VM
ip1 = "http://104.41.211.213:8080"
ip2 = "http://40.85.126.76:8080"

@app.route('/')
def func():
        round_robin=get_servers()
        if round_robin == "1":
                response = requests.get(url = ip1)
                return str(response.content)
        elif round_robin == "2":
                response = requests.get(url = ip2)
                return str(response.content)
        else:
                return "Not Found", 404

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)
