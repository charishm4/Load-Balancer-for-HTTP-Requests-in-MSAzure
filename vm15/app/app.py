from flask import Flask
import os
import socket
import psutil

app = Flask(__name__)
@app.route("/")
def hello():
    html = "<h3>Hello {name}! I am from webserver2 </h3> <b>Hostname:</b> {hostname} <br/> <p> load = {myvalue} </p>"
    return html.format(name="all", hostname=socket.gethostname(), myvalue=str(psutil.cpu_percent()))

@app.route("/load")
def load():
        myvalue=str(psutil.cpu_percent())
        return myvalue


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
