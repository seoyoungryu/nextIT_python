import requests
url = 'http://127.0.0.1:5000/subject'
res3 = requests.get(url + '/501')
print(res3)
print(res3.json())
