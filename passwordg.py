import random

char='abcdefghijklmnopqestuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890!@#$%^&*()'


pl=int(input('enter password length'))
pc=int(input('how many passwords you want to generate at a time'))

for i in range(pc):
    password=''
    for i in range(pl):
        randomchar= random.choice(char)
        password=password+randomchar
    print(password)