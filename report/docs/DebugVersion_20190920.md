
```
login: Case Fail
 Number: 1
 Method: post
 Url: https://mibapi.whoselab.com/api/user/auth
 Headers:
 {'Content-Type': 'application/json; charset=UTF-8;', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
 Data : 
 {"device_id":"febcbaae13751f7f8e44c2f107afb08d","os_type":1,"os_ver":"10.0","email":"402071088@qq.com","password":"123456"}
 Response : 
 {'code': 500, 'message': '認証に失敗しました。'}
 Expect : 200
 Actual : 500
```

```
devecReg: Case Pass
 Number: 2
 Method: post
 Url: https://mibapi.whoselab.com/api/user/devecReg
 Headers:
 {'Content-Type': 'application/json; charset=UTF-8;', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
 Data : 
 {"device_id":"febcbaae13751f7f8e44c2f107afb08d","os_type":1,"os_ver":"10.0"}
 Response : 
 {'code': 200, 'message': 'ok', 'uid': 21, 'is_first_login': False, 'regist_type': 8, 'api_token': '88a96ffccf7bbc0249b1617436e25d54', 'refresh_token': '273a489838c76f02b05a4e1a09fe43c9', 'expires_in': 604800, 'nick_name': None, 'height': None, 'weight': None, 'sex': None, 'birthday': None, 'blood_type': None, 'smoking': None, 'area': None}
 Expect : 200
 Actual : 200
```
