# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_caharacters = '!@#$%'

all = lower + upper + numbers + special_caharacters
length = 12
gen_password = "".join(random.sample(all , length))

print(gen_password)