with open('dayseventest.txt', 'r') as file:
    lines = file.read().split('\n')

def splitter_reached_bottom(i, j):
    num_of_times = 2
    for k in range(i, len(lines)):
        if lines[k][j-1] == '^':
            num_of_times -= 1
            break
    for k in range(i, len(lines)):
        if lines[k][j+1] == '^':
            num_of_times -= 1
            break
    #print(f'splitter at {i}, {j} reached the bottom {num_of_times} time(s)')
    return num_of_times

paths_map = dict()

def num_of_unique_paths(i, j):
    if str(i) + str(j) in paths_map:
        return paths_map[str(i) + str(j)]
    num_of_paths = 0
    k = i - 1
    while lines[k][j] != '^' and k >= 0:
        if lines[k][j] == 'S':
            paths_map[str(i) + str(j)] = 1
            return 1
        if lines[k][j-1] == '^':
            num_of_paths += num_of_unique_paths(k, j-1)
        if lines[k][j+1] == '^':
            num_of_paths += num_of_unique_paths(k, j+1)
        k -= 1
    paths_map[str(i) + str(j)] = num_of_paths
    return num_of_paths

m = len(lines)
n = len(lines[0])

timelines = 0

for i in range(m-3):
    for j in range(n):
        if lines[i][j] == '^':
            timelines += (splitter_reached_bottom(i, j) * num_of_unique_paths(i, j))

for j in range(n):
    if lines[m-2][j] == '^':
        #print(f'number of paths to {m-2}, {j} is {num_of_unique_paths(m-2, j)}')
        timelines += (2 * num_of_unique_paths(m-2, j))
    
print(timelines)
