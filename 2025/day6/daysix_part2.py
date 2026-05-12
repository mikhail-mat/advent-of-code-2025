import numpy as np

with open('daysix.txt', 'r') as file:
    lines = file.read().split('\n')

numbers = []
operation = []
for j in range(len(lines[0])):
    col_num = []
    if lines[0][j] == ' ' and lines[1][j] == ' ' and lines[2][j] == ' ' and lines[3][j] == ' ':
        numbers.append(operation)
        operation = []
        continue
    for i in range(len(lines)):
        col_num.append(lines[i][j])
    operation.append(col_num)
    if j == len(lines[0]) - 1:
        numbers.append(operation)

total = 0
for operation in numbers:
    if operation[0][4] == '+':
        op_total = 0
        add = True
    else:
        op_total = 1
        add = False

    for number in operation:
        number_str = ''
        for i in range(len(number)):
            if number[i] != '+' and number[i] != '*':
                number_str += number[i]
        number_int = int(number_str.strip())
        if add:
            op_total += number_int
        else:
            op_total *= number_int

    total += op_total

print(total)
            