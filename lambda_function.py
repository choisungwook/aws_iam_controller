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
    iam_client = boto3.client('iam')

    user = iam_client.create_user(UserName=username)
    temporary_password = "Xf#Vfjck4T"

    iam_client.create_login_profile(
        UserName=username,
        Password=temporary_password,
        PasswordResetRequired=True
    )

    return "done"

"""
    IAM 계정 생성과 정책 설정
"""
def create_user_with_policy(parameter):
    username = parameter['username']
    policy = parameter['policy']

    iam_client = boto3.client('iam')
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

    iam_client = boto3.client('iam')
    iam_client.delete_user(UserName=username)

    return "done"

"""
    IAM 유저 목록
"""
def list_user(parameter=None):
    client=boto3.client('iam')
    response=client.list_users()

    user_lists = []    
    for user_info in response['Users']:
        user_lists.append(user_info['UserName'])
    
    return user_lists


"""
    계정 패스워드 등록
"""
def set_password(parameter):
    client=boto3.client('iam')

    username = parameter['username']
    temporary_password = "Xf#Vfjck4T"

    response = client.create_login_profile(
        UserName=username,
        Password=temporary_password,
        PasswordResetRequired=True
    )

    return response

"""
    main function
"""
def lambda_handler(event, context):
    # (todo)예외 처리 필요 -> 파싱오류
    
    request_parameter = event['queryStringParameters']
    function_name = request_parameter['command']
    
    response = globals()[function_name](event['queryStringParameters'])
    
    # (todo) 회원가입 실패하면 에러 응답 전달
    statusCode = 200

    response_body = {
        "reponse": response
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