import requests
 
r = requests.get('http://localhost:8080/girl')
print(type(r))
print(r.status_code)
print(r.headers)
print(r.headers['content-type'])
#print(r.text)
