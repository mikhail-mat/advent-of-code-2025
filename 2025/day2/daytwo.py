with open('daytwo.txt', 'r') as file:
    content = file.read().split(',')

def is_invalid(id):
    str_id = str(id) # 121212
    n = len(str_id) # 6
    # create a loop from 2 to n to create 2 to n equal slices of the string, compare them
    for i in range(2, n+1): # number of groups from 2 to n
        if n % i != 0:
            continue
        # n // 3 -> 0:n // 3 -> n//3:2*(n//3) -> 2*(n//3):n
        slice_arr = []
        slice_size = n // i # 3
        for j in range(i): # 0, 1
            new_slice = str_id[slice_size*j:slice_size*(j+1)] # 0:2
            slice_arr.append(new_slice) # 12
        init_slice = slice_arr[0]
        count = 0
        for slice in slice_arr:
            if slice == init_slice:
                count += 1
        if count == len(slice_arr):
            return True
    return False

id_sum = 0

for id_pair in content:
    first_id = id_pair.split('-')[0]
    last_id = id_pair.split('-')[1]
    for id in range(int(first_id), int(last_id) + 1):
        if is_invalid(id): # if this is true
            id_sum += id # add the id to the sum

print(id_sum)
