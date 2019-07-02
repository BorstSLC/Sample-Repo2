import requests



r = requests.get(
    "http://mikejuniperhill.blogspot.com/2018/11/quantlib-python-hull-white-one-factor.html"
)
print(r.status_code)
print(r.ok)