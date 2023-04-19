# Задание 26

A = int(input("Введите число "))
B = int(input("Введите степень "))
def Multiply(x, y):
    b = x
    if y > 2:
        b=  Multiply(x, y-1)
    return x * b
print(Multiply(A, B))

# Задание 28

A = int(input("Введите первое число "))
B = int(input("Введите второе число "))
def Sum(x, y):
    b=x
    if y > 0:
        b = Sum(x + 1, y - 1)
    return b
    

print(Sum(A, B))

