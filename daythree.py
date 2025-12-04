with open('daythree.txt', 'r') as file:
    content = file.read().split('\n')

def find_max(elem, order):
    if order < 0:
        return ''
    n = len(elem)
    max_index = 0
    currentMax = -1
    for i in range(n-order):
        if int(elem[i]) > currentMax:
            currentMax = int(elem[i])
            max_index = i
    newMax = find_max(elem[max_index+1:], order-1)
    return str(currentMax) + newMax

total_max = 0
for elem in content:
    bank_max = int(find_max(elem, 11))
    total_max += bank_max

print(total_max)