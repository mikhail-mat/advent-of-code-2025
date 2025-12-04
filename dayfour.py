with open('dayfour.txt', 'r') as file:
    content = file.read().split('\n')

for i in range(len(content)):
    content[i] = list(content[i])

def count_adjacent_rolls(i, j):
    count = 0
    
    if j != 0:
        if content[i][j-1] == '@':
            count += 1
        if i != 0:
            if content[i-1][j-1] == '@':
                count += 1
        if i != len(content) - 1:
            if content[i+1][j-1] == '@':
                count += 1

    if j != len(content[i]) - 1:
        if content[i][j+1] == '@':
            count += 1
        if i != 0:
            if content[i-1][j+1] == '@':
                count += 1
        if i != len(content) - 1:
            if content[i+1][j+1] == '@':
                count += 1
    
    if i != 0:
        if content[i-1][j] == '@':
            count += 1

    if i != len(content) - 1:
        if content[i+1][j] == '@':
            count += 1
    
    return count

rmv_rolls = 0
changed = True
while changed:
    changed = False
    for i in range(len(content)): # replace by len(content)
        for j in range(len(content[i])):
            if content[i][j] == '@':
                count = count_adjacent_rolls(i, j)

                #print(f'{count}')

                if count < 4:
                    changed = True
                    rmv_rolls += 1
                    content[i][j] = '.'

print(rmv_rolls)
