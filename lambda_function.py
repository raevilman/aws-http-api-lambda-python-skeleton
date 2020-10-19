from app.utils import get_logger
from app.app import run
from app.responder import send_server_error
import json

# Setup logging
logger = get_logger("lambda_function")


def lambda_handler(event, context):
    try:
        logger.info('Request is '+json.dumps(event))
        return run()
    except Exception as e:
        import traceback
        info = traceback.format_exc()
        logger.error(info)
        return send_server_error(context.aws_request_id)
