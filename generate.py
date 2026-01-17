import random, string

login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) # k = Character count
password = ''.join(random.choices(string.ascii_letters  + string.digits + '!@#$%', k=16)) # k = Character count too

print(f'Login: {login}\nPassword: {password}') # Console output
