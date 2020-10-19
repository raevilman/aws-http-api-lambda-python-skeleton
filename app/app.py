from app.responder import send_ok_response
import json


def run():
    return send_ok_response(json.dumps({
        'message': 'Hello'
    }))
