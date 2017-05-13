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

@app.route("/api/ide/modify")
def code_modified():
    author = request.form["author"]
    if author == "LP01632947305":
        namespace = "/interviewee"
    else:
        namespace = "/LP01632947305"
    socketio.emit("modify", request.form["code"], namespace=namespace)
    return "code changed from: " + namespace

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
