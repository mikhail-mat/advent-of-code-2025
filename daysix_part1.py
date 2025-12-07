import numpy as np

with open('daysix.txt', 'r') as file:
    lines = file.read().split('\n')

numbers = []
for i in range(len(lines)-1):
    line = []
    for j in lines[i].split(' '):
        if j != '' and j != ' ':
            line.append(int(j))
    numbers.append(line)

symbols = []
for i in range(len(lines)-1, len(lines)):
    for j in lines[i].split(' '):
        if j != '' and j != ' ':
            symbols.append(j)

matrix = np.matrix(numbers)
inverted_nums = np.transpose(matrix)
# print(inverted_nums.shape)

total = 0
for i in range(inverted_nums.shape[0]):
    nums_list = []
    for j in range(inverted_nums.shape[1]):
        max_len = len(str(np.max(inverted_nums[i])))
        temp = []
        for k in range(max_len - len(str(inverted_nums[i, j]))):
            temp.append('')
        for k in str(inverted_nums[i, j]):
            temp.append(k)
        nums_list.append(temp)
        print(temp)

    inverted_nums_list = []
    for n in range(len(nums_list[0])):
        concat_str = ''
        for m in range(len(nums_list)):
            concat_str += nums_list[m][n]
        inverted_nums_list.append(int(concat_str))
    print(inverted_nums_list)

    if symbols[i] == '+':
        line_total = 0
        for num in inverted_nums_list:
            line_total += num
    elif symbols[i] == '*':
        line_total = 1
        for num in inverted_nums_list:
            line_total *= num

    print(line_total)
    total += line_total

print(total)