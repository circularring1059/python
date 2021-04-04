import hashlib
"""
md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.
"""

str1 = "hello world"

sha1 = hashlib.sha1(str1.encode("utf-8"))
print(sha1.hexdigest(), type(sha1.hexdigest()))   #str

print(str1.encode(), type(str1.encode())) #b'hello world' <class 'bytes'>
