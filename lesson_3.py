# Задание 16
N = int(input('Введите число элементов в массиве '))
A = [0]*N
counter = 0
for i in range(N):
    print('Введите ', i+1, ' элеиент массива')
    A[i] = int(input())
X = int(input('Введите число, которое хотите найти в массиве '))
for i in range(N):
    if A[i] == X:
        counter = counter + 1
print('Число ', X, ' встечается ', counter, ' раз(а)')


# Задание 18

N = int(input('Введите число элементов в массиве '))
A = [0]*N

for i in range(N):
    print('Введите ', i+1, ' элеиент массива')
    A[i] = int(input())
X = int(input('Введите число, которое хотите найти в массиве или близкое к нему по значению '))
MinDiff = abs(A[0] - X)
element = A[0]
for i in range(N):
    if (abs(A[i] - X) < MinDiff):
        MinDiff = abs(A[i] - X)
        element = A[i]
print(element)
