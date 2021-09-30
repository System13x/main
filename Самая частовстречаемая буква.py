s = input()
bukva = 0
count = 0
for i in s:
    if s.count(i) >= count:
        count = s.count(i)
        bukva = i
print(bukva)