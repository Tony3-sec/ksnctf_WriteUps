#!/usr/bin/env python

array = "1,7,16,11,14,19,20,18"
array = array.split(',')

array2 = "85,111,117,43,104,127,117,117,33,110,99,43,72,95,85,85,94,66,120,98,79,117,68,83,64,94,39,65,73,32,65,72,51"
array2 = array2.split(',')

array_len = len(array)
array2_len = len(array2)

flag = ""

for i in range(array2_len):
	flag += chr(int(array2[i]) ^ int(array[i % array_len]))
print(flag)

'''
./rightsout-solver.py
The flag is FLAG_EhiAfPAAY7JG3UZ2
'''