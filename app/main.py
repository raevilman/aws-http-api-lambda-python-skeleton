import json

from app.event import Event
from app.responder import send_ok_response, send_response
from app.utils import get_logger

# Setup logging
logger = get_logger("app")


def return_aliens(event: Event):
    return send_response(404, json.dumps({
        'message': 'Aliens!'
    }))


def run(event: Event):
    route_key = event.route_key()
    logger.info(route_key)
    router = {
        'GET /echo': handle_get_echo,
        'GET /greetings': handle_get_greetings
    }
    return router.get(route_key, return_aliens)(event)


def handle_get_echo(event: Event):
    return send_ok_response(body=json.dumps({
        'message': 'got echo!'
    }))


def handle_get_greetings(event: Event):
    return send_ok_response(body=json.dumps({
        'message': 'good day!'
    }))

