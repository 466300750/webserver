import requests
from multiprocessing.dummy import Pool

url = 'http://localhost:8080/girl'

def req_split(r):
    #requests.head is much faster than requests.get if your intention is only to get the status code
    req = requests.get(url) 

    if req.status_code == 200:
	    temp = r #return the url string if the server report OK
    else:
	    temp = 0
    return temp

data = range(0,5000)

with Pool(50) as p:
    pm = p.imap_unordered(req_split,data)
    pm = [i for i in pm if i]
