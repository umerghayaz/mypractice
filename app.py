from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"


def send_msg(msg):
    PHONE_ID = "110829038490956"
    TOKEN = "EAAJVc3j40G8BADmXpwkMPbpZAREzu4knZAYJZAEEHIUdg3gZAnP0Ak9QeYZBSFRITs2jmLPneZCAwtqj0Uvoyv1B9ins6nRTYl25BU2TD3U5ddUEPLxqdbIIG28H6XWVNBbabYY84cnPeTw2FCar3ZCSc3YGHkrAYP8MnZAaaLiVF8znScWre7BSTpGV11FnoBe2bdAtwyZBfJgZDZD"
    NUMBER = "923462901820"
    MESSAGE = "<message>"
    headers = {
        "Authorization": "Bearer "+TOKEN,
    }
    json_data = {
        'messaging_product': 'whatsapp',
        "to": NUMBER,
        'type': 'text',
        "text": {
            "body": msg
        }
    }
    response = requests.post( "https://graph.facebook.com/v13.0/"+PHONE_ID+"/messages", headers=headers,
                             json=json_data)
    print(response.text)


@app.route('/receive_msg', methods=['POST', 'GET'])
def webhook():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "umer":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200
    print(request)
    res = request.get_json()
    print(res)
    try:
        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            send_msg("Thank you for the response.")
    except:
        pass
    return '200 OK HTTPS.'


if __name__ == "__main__":
    app.run(debug=True)