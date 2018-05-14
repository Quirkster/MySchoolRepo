import requests
res = requests.get('https://senorsalazarspanishclass.wordpress.com')
res.status_code == requests.codes.ok
len(res.text)
print(res.text[3000:50000])

