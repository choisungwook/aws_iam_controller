import json
import boto3

"""
    main function
"""
def lambda_handler(event, context):
    username_parameter = event['username']

    statusCode = 200
    response_body = {
        "hello": "world"
    }

    return {
        'statusCode': statusCode,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(response_body, ensure_ascii=False)
    }