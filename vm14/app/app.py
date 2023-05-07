from flask import Flask
import os
import socket
import psutil

app = Flask(__name__)
@app.route("/")
def hello():
    html = "<h3>Hello {name}! I am from webserver1 </h3> <b>Hostname:</b> {hostname}<br/> <p> Load = {myvalue} </p>"
    return html.format(name="all", hostname=socket.gethostname(), myvalue=str(psutil.cpu_percent()))

@app.route("/load")
def load():
        value=psutil.cpu_percent()
        return str(value)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
