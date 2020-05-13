#!/usr/bin/env python

import hashlib

deviceID_hash = "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5"
first_eight_bytes = "99999991"
cnt = 1

while (cnt <= 9999999):
	latter_seven_bytes = '{:0=7}'.format(cnt)
	print(first_eight_bytes + latter_seven_bytes)
	calculated_hash = hashlib.sha256(first_eight_bytes + latter_seven_bytes).hexdigest()
	#print(calculated_hash)
	if (calculated_hash == deviceID_hash):
		print("DeviceID: " + first_eight_bytes + latter_seven_bytes)
		print("AES key: " + str("!") + first_eight_bytes + latter_seven_bytes)
		break
	cnt += 1

	#DeviceID: 999999913371337
	#AES key: !999999913371337