print('������� ���������� ����������')
n = int(input())
print('������� ���������� ���� ����������')
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
print('������ �����', largest)
print('������ �����', prelargest)
print('������ �����', preprelargest)