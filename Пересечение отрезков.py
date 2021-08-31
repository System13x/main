#print('Welcome, my test programm, enter your name')
#name = input()
#print('Hello,', name)
#phone = input('Enter your phone number ')
#print('Greate,', name, 'your phone number is', phone)
#n = int(input())
#print((n + 3) // 4)
#x = int(input())
#a = x // 1000
#b = x // 100 % 10
#c = x % 100 // 10
#d = x % 10
#print(a, b, c, d)
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 < a1:
    if b2 < a1:
        print('пустое множество')
    elif b2 == a1:
        print(b2)
    elif a1 < b2 <= b1:
        print(a1, b2)
    elif b2 > b1:
        print(a1, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('пустое множество')



