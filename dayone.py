with open('rotations.txt', 'r') as file:
    content = file.read().split('\n')

current_pos = 50
count = 0

for i in range(len(content)):
    shift = int(content[i][1:]) % 100

    # increment count for every full circle around the lock
    full_rots = int(content[i][1:]) // 100
    if current_pos == 0 and shift == 0:
        full_rots -= 1
    count += full_rots

    if content[i][0] == 'L':
        shift = -shift

    if current_pos + shift < 0:
        if current_pos != 0:
            count += 1
        current_pos = 100 + (current_pos + shift)
    elif current_pos + shift > 99:
        current_pos = (current_pos + shift) - 100
        count += 1
    else:
        current_pos = current_pos + shift
        if current_pos == 0:
            count += 1

    # print(f'current position: {current_pos}; count: {count}')

print(count)
