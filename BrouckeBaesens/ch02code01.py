import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(url)

print(r.status_code)
print(r.reason)
print(r.headers)
print(r.request)
print(r.request.headers)

print(r.text)
