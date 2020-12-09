import json


def send_response(status: int, body: str):
    response = {
        "statusCode": status,
        "body": body
    }
    return response


def send_ok_response(body: str):
    return send_response(200, body)


def send_error(status: int, msg: str, req_id: str):
    error = get_error_body(msg, req_id)
    return send_response(status, json.dumps(error))


def send_server_error(req_id: str):
    error = get_error_body(msg="Something went wrong", req_id=req_id)
    return send_response(500, json.dumps(error))


def get_error_body(msg: str, req_id: str):
    return json.dumps({
        'error': msg,
        'req_id': req_id
    })


def send_header_missing_error(header_key: str, req_id: str):
    error_msg = "'" + header_key + "' header is missing!"
    return send_response(status=401, body=get_error_body(error_msg, req_id))
