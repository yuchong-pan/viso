import os
from flask import Flask, jsonify, request
from faker import Factory
from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    IpMessagingGrant,
    SyncGrant
)

app = Flask(__name__)
fake = Factory.create()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_KEY"]
api_secret = os.environ["TWILIO_API_SECRET"]
chat_service_sid = os.environ["TWILIO_CHAT_SERVICE_SID"]
sync_service_sid = os.environ["TWILIO_SYNC_SERVICE_SID"]

def access_token():
    identity = request.args.get("id", fake.user_name())
    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

@app.route("/chat/token")
def chat_token():
    token = access_token()
    chat_grant = IpMessagingGrant(service_sid=chat_service_sid)
    token.add_grant(chat_grant)
    return jsonify(identity=identity, token=token.to_jwt())

@app.route("/sync/token")
def sync_token():
    token = access_token()
    sync_grant = IpMessagingGrant(service_sid=sync_service_sid)
    token.add_grant(sync_grant)
    return jsonify(identity=identity, token=token.to_jwt())

if __name__ == "__main__":
    app.run(debug=True)
