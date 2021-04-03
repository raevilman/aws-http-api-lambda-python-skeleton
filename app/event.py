class Event:
    def __init__(self, event):
        self.event = event

    def req_context(self):
        return self.event['requestContext']

    def route_key(self):
        return self.event['routeKey']
    def get_path_param(self, param_name: str):
        if 'pathParameters' in self.event and self.event['pathParameters'] is not None:
            path_params = self.event['pathParameters']
            if param_name in path_params:
                return path_params[param_name]
        return None

    def http_path(self):
        return self.req_context()['http']['path']

    def http_method(self):
        return self.req_context()['http']['method']

    def source_ip(self):
        return self.req_context()['http']['sourceIp']

    def req_id(self):
        # return self.req_context()['requestId']
        return self.context.aws_request_id

    def headers(self) -> dict:
        return self.event['headers']

    def get_header(self, key: str):
        return self.headers().get(key, None)

    def req_body(self):
        if 'body' in self.event:
            return self.event['body']
        else:
            return None

    def get_query_param(self, param_name: str):
        if 'queryStringParameters' in self.event and self.event['queryStringParameters'] is not None:
            query_params = self.event['queryStringParameters']
            if param_name in query_params:
                return query_params[param_name]
        return None

    def is_base64encoded(self):
        return self.event['isBase64Encoded']

    def jwt_claims(self):
        return self.req_context()['authorizer']['jwt']['claims']

    def jwt_claim_firebase_uid(self):
        return self.jwt_claims()['user_id']

    def jwt_claim_firebase_email(self):
        return self.jwt_claims()['email']
