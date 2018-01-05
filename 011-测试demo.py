import requests


#发送get请求
f = requests.get(url = 'http://www.baidu.com')
print(f.status_code)
print(f)

r = requests.get(url = 'http://www.baidu.com',params = {'wd':'python'})
print(r)


#获取返回状态



