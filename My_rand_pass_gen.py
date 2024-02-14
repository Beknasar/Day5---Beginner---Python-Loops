import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*(){}[];:"

long_string = lower + upper + numbers + symbols
pass_length = int(input("How much symbols in password would you like?: "))
list_pass = random.sample(long_string, pass_length)
output = "".join(list_pass)
print(output)
