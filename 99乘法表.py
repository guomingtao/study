import requests
import sys
import json
# for t in range(1,10):
#     for s in range(1,t+1):
#         print('{}x{}={}\t'.format(t, s, t*s), end='')
#     print()
# sum1=0
# for t in range(1,101):
#     if t%2 == 0 :
#         sum1=sum1+t
# print('1-100之间偶数和：' + str(sum1))
headers= { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36' }
# url = 'https://cloud.tencent.com/developer/article/1576229'
# t=requests.get(url,headers=headers)
# t.encoding='utf-8'
# print(t.headers['Server'])
# print(t.headers)
# print(t.text)
user='"sfadmin1"'
password='"SenseTime#2020"'
# print(user,password)

# print(payload)
# 获取SC accessToken
def getAccessToken():

    url="http://16.130.45.120:10219/uums/auth/token"
    #payload = "{\r\n  \"username\" : \"sfadmin1\",\r\n  \"password\" : \"SenseTime#2020\",\r\n  \"grant_type\" : \"password\"\r\n}"
    payload = "{\r\n  \"username\" : " + user + ", \r\n \"password\" : " + password + ",\r\n  \"grant_type\" :\"password\"\r\n}"
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data = payload)
    test = json.loads(response.text).get('data').get('accessToken')
    return test
    #print('accessToken:' + test)
accessToken=getAccessToken()
print("accessToken:" + accessToken)