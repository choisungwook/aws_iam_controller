# API
* 유저생성: /createuser?create_user&username=[유저이름]
* 유저목록조회: /createuser?command=list_user
* 유저삭제: /createuser?command=delete_user?username=[유저이름]
* 비밀번호 설정: /createuser?command=set_password?username=[유저이름]

# 참고자료
* [boto3 공식문서](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_user)