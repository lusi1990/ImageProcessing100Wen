# /usr/bin/env python


from urllib import request

IP_CHECKER_URL = "https://httpbin.org/ip"
resp = request.urlopen(IP_CHECKER_URL)
print(resp.read())
