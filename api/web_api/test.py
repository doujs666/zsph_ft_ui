import requests
url = 'https://www.kaola.com/login.html?target=https%3A%2F%2Fwww.kaola.com%2F&zn=top'
s = requests.session()
data = {'username':'gaohf', 'password':'admin'}
r = s.post(url, data=data, allow_redirects = True)
print r.encoding