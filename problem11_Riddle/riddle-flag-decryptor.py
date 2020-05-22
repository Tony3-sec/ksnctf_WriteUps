#!/usr/bin/env python

'''
This script will XOR the data. 
The key and the payload must be in hex format
Simplified the code from my_xor.py
'''

import binascii

#encrypted flag: 0xBFFF1B0D47A7184FCBD65C5995617357B3D1949FAC
#XOR key: 0xF9B35A4A18EA5D3699E2063FA120471FF586A3ACC7

enc = "BFFF1B0D47A7184FCBD65C5995617357B3D1949FAC"
key = "F9B35A4A18EA5D3699E2063FA120471FF586A3ACC7"
dec = ""

n = 2

## if key is single byte
if ( (len(key) / 2) == 1):
	m = 0
	for i in range(0, len(enc), n):
		dec += hex(int(enc[i:i+n], 16) ^ int(key[m:m+n], 16)).replace('0x', '').zfill(2)
else:
	m = 0
	for i in range(0, len(enc), n):
		dec += hex(int(enc[i:i+n], 16) ^ int(key[m:m+n], 16)).replace('0x', '').zfill(2)
		m += n
		## if the key gets to end, set the key back to beginning.
		if (m >= len(key)):
			m = 0

print(dec)
#dec = dec.replace('0d0d', '0d0a') ## not sure why but when hex contains '0d0d' it doesn't print properly so replacing to '0d0a'
#print(binascii.unhexlify(dec))
print(repr(binascii.unhexlify(dec)))
print("")
'''
464c41475f4d457952345a6634413448465737336b
'FLAG_MEyR4Zf4A4HFW73k'
'''