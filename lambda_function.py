import json
import boto3



"""
    IAM 계정만 생성

    (todo) 예외처리 필요
    1. 중복
    2. 권한(IAM) 에러
    3. 등등
"""
def create_user(parameter):
    username = parameter['username']

    iam_client = boto3.resource('iam')
    iam_client.create_user(UserName=username)

"""
    IAM 계정 생성과 정책 설정
"""
def create_user_with_policy(parameter):
    username = parameter['username']
    policy = parameter['policy']

    iam_client = boto3.resource('iam')
    iam_client.create_user(
        UserName=username,
        PolicyArn='policy:arn'
    )
    pass

"""
    IAM 계정 삭제
    (todo) 예외처리 
"""
def delete_user(parameter):
    username = parameter['username']

    iam_client = boto3.resource('iam')
    iam_client.delete_user(UserName=username)

"""
    IAM 유저 목록
"""
def list_user(parameter=None):
    client=boto3.client('iam')
    response=client.list_users()

    for x in response['Users']:
        print(x['UserName'])


"""
    main function
"""
def lambda_handler(event, context):
    # (todo)예외 처리 필요 -> 파싱오류
    
    request_parameter = event['queryStringParameters']
    function_name = request_parameter['command']
    
    globals()[function_name](event['queryStringParameters'])
    
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