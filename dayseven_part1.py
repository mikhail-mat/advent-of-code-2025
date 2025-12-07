with open('dayseven.txt', 'r') as file:
    lines = file.read().split('\n')

reach_map = dict()

def beam_reached_splitter(i, j):
    if str(i) + str(j) in reach_map:
        return reach_map[str(i) + str(j)]

    print(f'splitter found at {i}, {j}')
    for k in range(i-1, -1, -1):
        print(f'going up to {k}')
        
        if lines[k][j] == '^':
            print(f'cannot go up, splitter blocking path at {k}, {j}')
            break
        
        if lines[k][j] == 'S':
            print('found the source of the beam!')
            reach_map[str(i) + str(j)] = True
            return True
        
        if lines[k][j-1] == '^':
            print(f'splitter found to the left at {k}, {j-1}')
            if beam_reached_splitter(k, j-1):
                print(f'the beam reaches the splitter at {k}, {j-1}!')
                reach_map[str(i) + str(j)] = True
                return True
        
        if lines[k][j+1] == '^':
            print(f'splitter found to the right at {k}, {j+1}')
            if beam_reached_splitter(k, j+1):
                print(f'the beam reaches the splitter at {k}, {j+1}!')
                reach_map[str(i) + str(j)] = True
                return True
    
    print(f'the beam does not reach the splitter at {i}, {j}')
    reach_map[str(i) + str(j)] = False
    return False

splitter_count = 0
split_count = 0
for i in range(len(lines)):
    n = len(lines[0])
    for j in range(n):
        if lines[i][j] == '^':
            splitter_count += 1
            if beam_reached_splitter(i, j):
                split_count += 1

print(splitter_count)
print(split_count)