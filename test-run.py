from lambda_function import lambda_handler
import json

if __name__ == '__main__':
    with open('./docs/sample-req.json') as json_file:
        data = json.load(json_file)
        response = lambda_handler(event=data, context={})
        print('Status: ' + str(response['statusCode']))
        print(json.dumps(json.loads(response['body']), indent=1))
