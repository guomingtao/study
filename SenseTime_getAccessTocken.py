import requests
import json
import pybase64
import io

# 图片转换成base64
def picture2base(path):
    with open(path, 'rb') as img:
        # 使用base64进行编码
        b64encode = pybase64.b64encode(img.read())
        s = b64encode.decode()
#        base64 = 'data:image/jpeg;base64,%s' % s
         #返回base64编码字符串
        return s

# base64转换成图片
def base2picture(base64,path):
    # 分割字符串
    res=base64.split(',')[1]
    # 使用base64进行解码
    b64decode = pybase64.b64decode(res)
    image = io.BytesIO(b64decode).read()
    #图片输出目录
    with open(path, 'wb') as file:
        file.write(image)


# print(picture2base(r'C:\Users\cm\Desktop\demo.jpg'))
# base2picture(picture2base(r'C:\Users\cm\Desktop\demo.jpg'),r'C:\Users\cm\Desktop\demo1.jpg')



headers= { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36' }
user='"sfadmin"'
password='"SenseTime#2020"'
host='http://16.130.45.120:10219'
def getAccessToken():

    url= host + '/uums/auth/token'
    #payload = "{\r\n  \"username\" : \"sfadmin2\",\r\n  \"password\" : \"SenseTime#2020\",\r\n  \"grant_type\" : \"password\"\r\n}"
    payload = "{\r\n  \"username\" : " + user + ", \r\n \"password\" : " + password + ",\r\n  \"grant_type\" :\"password\"\r\n}"
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data = payload)
    token = json.loads(response.text).get('data').get('accessToken')
    return token




def getPortraits():
    token = getAccessToken()
    data1=picture2base(r'C:\Users\cm\Desktop\demo.jpg')
    url = host +'/whale-openapi/portraits/query'
    payload={
        "page":1,
        "senseType":1,
        "pageSize":10,
        "tarLibSerials":["8179eff2-08ce-4776-a775-1a31b21d8000"]
    }
    headers={'Content-Type': 'application/json','accessToken': token }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    return  json.loads(response.text)
#SC4.1以图搜图

def imageSearch(imagepath):
    token=getAccessToken()
    url = host + "/whale-openapi/composite-search/capture/search"

    payload = json.dumps({
        "objectSerial": "1653616525872",
        "serial": "1653616525776",
        "search": True,
        "searchFilter": {
            "attributeFilters": [],
            "cameraSerials": []
        },
        "searchImage": {
            "manual": True,
            "image": {
                "name": "sfa.jpg",
                "data": picture2base(imagepath)
            },
            "position": {
                "start": {
                    "x": 75,
                    "y": 66
                },
                "end": {
                    "x": 227,
                    "y": 225
                }
            }
        },
        "page": {
            "pageSize": 150,
            "page": 1
        },
        "period": {
            "endTime": 1653616507161,
            "startTime": 1653011707161,
            "type": 0
        },
        "onlyFace": False,
        "searchType": "FACE",
        "sort": "SCORE",
        "threshold": 0.95,
        "imageSource": 0,
        "cameraGroups": [
            {
                "selectType": 99
            }
        ]
    })
    headers = {
        'accessToken': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return  response.text

print(getPortraits())
print(imageSearch(r"C:\Users\cm\Desktop\sfa.jpg"))



