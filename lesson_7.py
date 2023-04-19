# Задание 34
data = list(map(str,input().split()))
flag = 1
count = []

for i in range(len(data)):
    count.append(len(list(filter(lambda x: x == '1', data[i]))))
    if count[0] != count[i]:
        flag = 0
        
if flag == 1:
    print('Парам пам-пам')
else:
    print('Пам парам”')

# Задание 36
def operation(x,y):
    return(x*y)
def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            nums.append(num)
        print(nums)
print_operation_table(operation, 6, 6)