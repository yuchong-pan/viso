from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/api/leap/alert")
def received_alert():
    namespace = "/" + request.args.get("id", "")
    console.log("received alert from: " + namespace)
    emit("alert", "!", namespace=namespace)

if __name__ == "__main__":
    socketio.run(app)
