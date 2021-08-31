a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1):
    print('YES')
else:
    print('NO')