# Babycrypto3

### Challenge Text
>Plesase decrypt and get flag.
>
>Flag is LINECTF{decryped text} and
decrypted text is human-readable text.

[pub.pem](pub.pem)
[ciphertext.txt](ciphertext.txt)

### Challenge Work

First, we take a look at the pub.pem file:

``` txt
(env) babycrypto3 % cat pub.pem
-----BEGIN PUBLIC KEY-----
ME0wDQYJKoZIhvcNAQEBBQADPAAwOQIyAyixQTmi5UuIpGYvGmfMOs0ZKcm2J5S7
ZJFq/wKZH4BFbk0O7U1ZHfdwjVry6bT7VokCAwEAAQ==
-----END PUBLIC KEY-----
```

That is not very large... Let us take a look under the hood:

```txt
(env) babycrypto3 % openssl rsa -pubin -in pub.pem -text -noout
Public-Key: (394 bit)
Modulus:
    03:28:b1:41:39:a2:e5:4b:88:a4:66:2f:1a:67:cc:
    3a:cd:19:29:c9:b6:27:94:bb:64:91:6a:ff:02:99:
    1f:80:45:6e:4d:0e:ed:4d:59:1d:f7:70:8d:5a:f2:
    e9:b4:fb:56:89
Exponent: 65537 (0x10001)
```

Ok, so I convert this to an integer, and find that it is only 119 digits long. I look it up on factordb and sure enough it is [already facotred for me](http://factordb.com/index.php?query=31864103015143373750025799158312253992115354944560440908105912458749205531455987590931871433911971516176954193675507337
).

I was able to take these two values and use them as P and Q to reverse the RSA inplementation used on the encrypted text. We also get the exponent value we need from the `pub.pem` file as well.

```python
# Sources
# https://stackoverflow.com/questions/4643647/fast-prime-factorization-module
# https://stackoverflow.com/questions/49856115/inverse-of-a-powa-b-n-function-in-python-decryption-code
# cryptohack.org

## Imports
import binascii
import base64
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

## Set Vars HERE
cipher_text = 10879776433900426660843740332190892429769159527203392037251077478777616065501519198653853699716123394455804888854401574
e = 65537
P = 109249057662947381148470526527596255527988598887891132224092529799478353198637
Q = 291664785919250248097148750343149685985101

def egcd(a, b):
	"""
	Extended (Euclid) Greatest Common Divisor
	"""
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# d3CrY9t0r
def decrypt_it_all(encrypted_message, e):
    gcd, x, y = egcd(e, (P-1)*(Q-1))

    if P != Q: # One would hope this is normally the case...
        n, phi = P * Q, (P - 1) * (Q - 1)
    else:
        n = P
        phi = (P - 1) * (Q - 1)
    
    D = inverse(e, phi)

    return pow(encrypted_message, D, n)

message = decrypt_it_all(cipher_text, e)
readable_message = long_to_bytes(message)

print(readable_message)
```
