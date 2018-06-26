#!/bin/bash
url='http://ctfq.sweetduet.info:10080/~q9/flag.html'
curl -i -q $url > out.txt

#response = MD5( MD5(A1) ":" nonce ":" nc ":" cnonce ":" qop ":" MD5(A2)
A1='c627e19450db746b739f41b64097d449'
nonce=$(grep -o -E "[a-zA-Z0-9]{11}=[a-z0-9]{40}" out.txt)
nc='00000001'
cnonce='1611c349765d94fd'
qop='auth'
method='GET'
uri_path='/~q9/flag.html'
A2=$(echo -n "$method:$uri_path" | md5)

response=$(echo -n "$A1:$nonce:$nc:$cnonce:$qop:$A2" | md5)

curl -i -H "Authorization: Digest username=\"q9\", realm=\"secret\", nonce=\"$nonce\", uri=\"/~q9/flag.html\", algorithm=MD5, response=\"$response\", qop=$qop, nc=$nc, cnonce=\"$cnonce\"" $url