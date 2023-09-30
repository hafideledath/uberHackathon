import hashlib

username = "example@gmail.com"
password = hashlib.sha512("123456789".encode('utf-8')).hexdigest()
a = hashlib.sha512(input().encode('utf-8')).hexdigest()

print(password == hashlib.sha512(input().encode('utf-8')).hexdigest())