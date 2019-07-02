import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):

    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get(
    "http://mikejuniperhill.blogspot.com/2018/11/quantlib-python-hull-white-one-factor.html"
)
print(r.status_code)
