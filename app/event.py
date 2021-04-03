class Event:
    def __init__(self, event):
        self.event = event

    def req_context(self):
        return self.event['requestContext']

    def route_key(self):
        return self.event['routeKey']

    def http_path(self):
        return self.req_context()['http']['path']

    def http_method(self):
        return self.req_context()['http']['method']

    def req_id(self):
        return self.req_context()['requestId']

    def req_body(self):
        if 'body' in self.event:
            return self.event['body']
        else:
            return None

    def is_base64encoded(self):
        return self.event['isBase64Encoded']
