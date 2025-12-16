import random, string

login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
password = ''.join(random.choices(string.ascii_letters  + string.digits + '!@#$%', k=16))

print(f'Login: {login}\nPassword: {password}')