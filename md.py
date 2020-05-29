import hashlib

md5 = hashlib.md5()
#md5.update(0xffff)
print(f"{md5.hexdigest()}")
print(f"{md5.digest()}")

sha1 = hashlib.sha1()
print(f"{sha1.hexdigest()}")