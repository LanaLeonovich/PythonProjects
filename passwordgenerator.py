import random

# Symbols in password
symbols = 'abcdefghyjklmnopqrstuvwxyz'
symbols += symbols.upper()
nums = str(1234567890)
symbols += nums
special = '!@#$%^&*()_+-'
symbols += special

length = 12 # password length
password = "".join(random.sample(symbols, length))
print(password)
