
<p>Result：</p>
<table border="3" width="500px">
  <tr>
    <th style="color: #787878">All</th>
    <th style="color: #3cc8b4">Pass</th>
    <th style="color: #FFB5C5">Fail</th>
  </tr>
  <tr>
    <th style="color: #787878">2</th>
    <th style="color: #3cc8b4">1</th>
    <th style="color: #FFB5C5">1</th>
  </tr>
</table>


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
 {'code': 200, 'message': 'ok', 'uid': 21, 'is_first_login': False, 'regist_type': 8, 'api_token': '1a3141dc96b9f85525cd3b567ed4cb8c', 'refresh_token': 'c28d30b72972afb75968ae3537202eff', 'expires_in': 604800, 'nick_name': None, 'height': None, 'weight': None, 'sex': None, 'birthday': None, 'blood_type': None, 'smoking': None, 'area': None}
 Expect : 200
 Actual : 200
```
