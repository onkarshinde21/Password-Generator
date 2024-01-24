import random
chars='abcdefghijklmnopqrstuvwxyz()ABCDEFGHIJKLMNOPQRSTUVWXYZ!,.-@#$%^&*!'
length = input('Password length\n')
length = int(length)
x = int(input("Number of Passwords You Want?\n"))
# password = "a"
while(x!= 0):
    for p in range(length):
        password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
    x = x-1