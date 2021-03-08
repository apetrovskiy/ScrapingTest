from requests import get


r = get('https://api.github.com', auth=('user', 'pass'))

print(r.status_code)
print(r.headers['content-type'])
