import requests

'''
r=requests.get("http://127.0.0.1:8000/hellor/v2")
print(r)
print(r.status_code)
print(r.text)
'''
data={}
data["name"]="samarth"
r=requests.get("http://127.0.0.1:8000/hello_name", params=data)
print(r)
print(r.status_code)
print(r.text)


r=requests.get("http://127.0.0.1:8000/hello_html")
print(r)
print(r.status_code)
print(r.text)


r=requests.get("http://127.0.0.1:8000/hello_html/samarth")
print(r)
print(r.status_code)
print(r.text)