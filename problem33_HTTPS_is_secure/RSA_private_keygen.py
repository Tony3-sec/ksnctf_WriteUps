#!/usr/bin/env python

## Code inspired from https://pashango-p.hatenadiary.org/entry/20090706/1246897957

# get greatest common divisor
def gcd(a, b):
     while b:
          a, b = b, a%b
     return a
# get least common multiple
def lcm(a, b):
    return a * b / gcd(a,b)
# get d
'''
1 < d < l
e * d mod l = 1
'''
def get_d(a, b):
    if b == 0:
        u = 1
        v = 0
    else:
        q = a / b
        r = a % b
        (u0, v0) = get_d(b, r)
        u = v0
        v = u0 - q * v0
    return (u, v)

# N for 192.168.0.39, 13099412999179996463.crt
N1 = 0x00a5a7ce44462e8ac6e4da5e8a8d58e003b8267568b358106cf06412884ceeb7cc4251c2cce2db74689d1afa109bde9762402e81d96cb6c8c6c5aebc8d45a96bf214a618b499a8c6134035c5039bf9a39bc47190e4cc4560cb75ab8d63635cdee8e50f5815b29180cc51a4c8cf76a8bbe6e61c68aca385fdf99e712b10a6be7ed794cf27540b7aa00f59da5579040a9b3b7c23e9e22a15c29eb0c060b96d1f48d1c458e2c412512962ce5af885237b6138df6c9e85d101c266c3b80b02ff97d6fde46598e19e3fa1df2c56bd34addfe716569a2ed42c6442bf2db5e9a51cc2d7dd4497717ddd9a8a66ae281e1a2abf7df7a59779b499cc0f8167a19e3ca5c9bbe3
# N for 192.168.0.40, 13099412999179996462.crt
N2 = 0x00a4daad49eae0b5c59da0452978ae987e1b96f149dedb62274c97f99ac4544aa90db4aaf9a0967f118b7009097bcb0baeb4a19636777a7747e06ad84496c9c61d18a7b5ca776585a817526ed6d9f0f2abd8c434c62cbf025eb7ce5a83e4a7f9938f3862de24e6292f43270ffda757c17aaa797ff9fe18fd1cb23921dc585d4550384ff5c4f24e6dfc6d4f44b569345808239247c20d266cd0f5e373889ed4e459590b7d742d2837c1c48dcf9418e22191ab4a0bca0ed79b1d45c0ca5d36ea6960c9360c11412329fd5d90ff3467f2d82e23021adf3b6d8be24903b76effc938154ec219f344118f1c41fec31171b62945a07e35762a961a05795389086052dec7

p = gcd(N1, N2)
q1 = N1 / p
q2 = N2 / p
l1 = lcm((p - 1), (q1 - 1))
l2 = lcm((p - 1), (q2 - 1))
e = 65537
d1 = get_d(e, l1)[0]
if d1 < 0:
	d1 += l1
d2 = get_d(e, l2)[0]
if d2 < 0:
	d2 += l2

print('p: ' + str(p))
print('')
print('N for 192.168.0.39: ' + str(p * q1))
print('q for 192.168.0.39: ' + str(q1))
print('l for 192.168.0.39: ' + str(l1))
print('d for 192.168.0.39: ' + str(d1))
print('e1 for 192.168.0.39: ' + str(d1 % (p - 1)))
print('e2 for 192.168.0.39: ' + str(d1 % (q1 - 1)))
print('coeff for 192.168.0.39: ' + str((q1 ^ - 1) % p))
print('')
print('N for 192.168.0.40: ' + str(p * q2))
print('q for 192.168.0.40: ' + str(q2))
print('l for 192.168.0.40: ' + str(l2))
print('d for 192.168.0.40: ' + str(d2))
print('e1 for 192.168.0.40: ' + str(d2 % (p - 1)))
print('e2 for 192.168.0.40: ' + str(d2 % (q2 - 1)))
print('coeff for 192.168.0.40: ' + str((q2 ^ - 1) % p)) 
'''
These values are later used to generate openssl asn1parse file
https://stackoverflow.com/questions/19850283/how-to-generate-rsa-keys-using-specific-input-numbers-in-openssl
https://www.openssl.org/docs/manmaster/man3/ASN1_generate_nconf.html
https://www.openssl.org/docs/man1.0.2/man1/asn1parse.html
'''