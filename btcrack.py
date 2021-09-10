import sys
import os
import time
import requests

def convert(num):

	nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	new_num = ""
	while num != 0:
		remainder = int(num % 36)
		new_num += nums[remainder]
		num -= remainder
		num /= 36

	return new_num[::-1]

def tryBT(urlPrefix, enrty):
	url = 'http://' + urlPrefix + '/' + enrty

	try:
	    r = requests.get(url, timeout=1)
	    r.raise_for_status()
	    print(r.status_code)

	except requests.RequestException as e:
	    print('Error '+ str(e))

	    return 0
	else:

	    return 1


# ip:port
urlPrefix = '127.0.0.1:8888'

i = 1

while (i < 36*36*36*36*36*36*36*36) :
	convertStr = str(convert(i)).lower()
	result = tryBT(urlPrefix, convertStr)

	while result != 0:
		url = 'http://' + urlPrefix + '/' + convertStr
		print('BT Entry Found: ' + url)
		exit()

	i+=1














