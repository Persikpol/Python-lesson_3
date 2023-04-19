# задача 30

a_1 = int(input("Введите первый элемент арифм. прогресси "))
a_n = int(input("Введите кол-во элементов арифм. прогресси "))
d = int(input("Введите разность арифм. прогресси "))
for i in range(a_n):
    print (a_1 + i * d)

# задача 32

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)