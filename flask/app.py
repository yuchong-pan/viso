import json
from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/api/leap/alert")
def received_alert():
    namespace = "/" + request.args.get("id", "")
    socketio.emit("alert", "!", namespace=namespace)
    return "received alert from: " + namespace

@app.route("/api/ide/modify", methods=["POST"])
def code_modified():
    body = json.loads(request.data)
    namespace = "/LP01632947305"
    socketio.emit("modify", json.dumps({"code": body["code"], "pos": body["pos"], "select": body["select"]}), namespace=namespace)
    return "code changed from: " + namespace

@app.route("/api/ide/lang")
def lang_changed():
    namespace = "/LP01632947305"
    socketio.emit("lang", request.args.get("l", ""), namespace=namespace)
    return "lang changed from: " + namespace

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)
