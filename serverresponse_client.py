import requests


dict={}
dict["name"]="samarth"
r =requests.get("http://127.0.0.1:5000/hello_name",params=dict)
print(r.text)
