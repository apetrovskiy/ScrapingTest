from urllib.request import Request, HTTPPasswordMgrWithDefaultRealm, \
    HTTPBasicAuthHandler, build_opener, install_opener, urlopen


gh_url = 'https://api.github.com'

req = Request(gh_url)

password_manager = HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'pass')

auth_manager = HTTPBasicAuthHandler(password_manager)
opener = build_opener(auth_manager)

install_opener(opener)

handler = urlopen(req)

print(handler.getcode())
print(handler.headers.get('content-type'))
