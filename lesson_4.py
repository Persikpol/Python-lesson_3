# задача 22

# list_1 = []
# list_2 = []
# N_1 = int(input('Введите количество элементов первого массива'))
# N_2 = int(input('Введите количество элементов второго массива'))
# print('Введите элементы первого массива')
# for i in range(N_1):
#     n = int(input())
#     list_1.append(n)
# print(list_1)
# print('Введите элементы второго массива')
# for i in range(N_2):
#     n = int(input())
#     list_2.append(n)
# print(list_2)
# for i in range(N_1):
#     Max = list_1[i]
#     j = i + 1
#     for j in range(N_1):
#         if list_1[j] > Max:
#             Max = list_1[j]
#             t = list_1[j]
#             list_1[j] = list_1[i]
#             list_1[i] = t
# print(list_1)
# for i in range(N_2):
#     Max = list_2[i]
#     j = i + 1
#     for j in range(N_2):
#         if list_2[j] > Max:
#             Max = list_2[j]
#             t = list_2[j]
#             list_2[j] = list_2[i]
#             list_2[i] = t
# print(list_2)

# Задача 24

garden_bed = []
N = int(input('Введите кол-во кустов '))
i = 0
for i in range(N):
    n = int(input('Введите число ягод на кусте '))
    garden_bed.append(n)
print(garden_bed)
Max= 0
for i in range(N-1):
    col = garden_bed[i] + garden_bed[i + 1] + garden_bed[i -1]
    if col>Max:
        Max = col
print(Max)

   