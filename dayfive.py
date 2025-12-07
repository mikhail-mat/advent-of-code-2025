with open('dayfive.txt', 'r') as file:
    content = file.read().split('\n')

ranges = None
ids = None

for i in range(len(content)):
    if content[i] == '':
        ranges = content[:i]
        ids = content[i+1:]

range_list = []
for rng in ranges:
    first_id = int(rng.split('-')[0])
    last_id = int(rng.split('-')[1])
    range_list.append([first_id, last_id])

range_list = sorted(range_list)
for i in range(len(range_list)):
    print(f'{range_list[i][0]} - {range_list[i][1]}')

new_list = []

for rng_a in range_list:
    append_rng = True
    for rng_b in new_list:
        if rng_b[1] >= rng_a[0]:
            if rng_b[1] >= rng_a[1]:
                append_rng = False
            else:
                rng_a[0] = rng_b[1] + 1
    if append_rng:
        new_list.append(rng_a)
        print(f'{rng_a[0]} -- {rng_a[1]}')

count = 0
for rng in new_list:
    count += (rng[1] - rng[0] + 1)
print(count)
