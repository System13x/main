n = int(input())
s = []
for i in range(n):
    n = input()
    s.append(n)
m = int(input())
p = []
for i in range(m):
    m = input()
    for j in s:
        if m.lower() in j.lower():
            p.append(j)
    s = p
    p = []  
print(*s, sep='\n')