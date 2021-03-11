import json
import boto3



"""
    (todo) 예외처리 필요
    1. 중복
    2. 권한(IAM) 에러
    3. 등등
"""
def create_user(username):
    iam_client = boto3.resource('iam')
    iam_client.create_user(UserName=username)

"""
    main function
"""
def lambda_handler(event, context):
    # (todo)예외 처리 필요 -> 파싱오류
    username_parameter = event['queryStringParameters']['username']

    create_user(username_parameter)
    # (todo) 회원가입 실패하면 에러 응답 전달
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