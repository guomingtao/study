import requests
import time
company_url='http://docs.python-requests.org/zh_CN/latest/user/quickstart.html'


try:
        req = requests.get(company_url, timeout=0.01)
        print(req.text)

except requests.exceptions.Timeout as a:
        print("a:"+str(a))
except requests.exceptions.ReadTimeout as b:
        print("b:"+str(b))

