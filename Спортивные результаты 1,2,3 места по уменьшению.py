print('Введите количество участников')
n = int(input())
print('Введите результаты всех учестников')
largest = 0
prelargest = 0
preprelargest = 0
for i in range(n):
    m = int(input())
    if m > largest:
        preprelargest = prelargest
        prelargest = largest
        largest = m
    elif largest > m > prelargest:
        prelargest = m
    elif prelargest > m > preprelargest:
        preprelargest = m
print('Первое место', largest)
print('Второе место', prelargest)
print('Третье место', preprelargest)