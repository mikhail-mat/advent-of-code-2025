def button_to_mask(indices):
    mask = 0
    for idx in indices:
        mask |= (1 << idx)    # turn that bit on
    return mask

def lights_to_mask(lst):
    bits = ''.join('1' if x == '#' else '0' for x in reversed(lst))
    return int(bits, 2)

with open('dayten.txt', 'r') as file:
    lines = [line.split(' ') for line in file.read().split('\n')]
    for line in lines:
        for i in range(1, len(line)-1):
            line[i] = button_to_mask([int(idx) for idx in line[i][1:len(line[i])-1].split(',')])

def press_button(start_lights, end_lights, start_i):
    presses = []

    if str(start_lights) + '-' + str(start_i) not in memo:
        for i in range(start_i, len(line)-1):
            # current_lights = start_lights.copy()

            # for light_index in line[i]: # for index in button
            #     if current_lights[int(light_index)] == '.':
            #         current_lights[int(light_index)] = '#'
            #     else:
            #         current_lights[int(light_index)] = '.'

            current_lights = start_lights ^ line[i]

            if current_lights == end_lights: # check if you got final lights after pressing the button
                # print(f'reached final lights with {start_i} button presses')
                # print(f'last button pressed was {line[i]}')
                return start_i
            
            if start_i+1 < len(line)-1:
                # print(f'could not reach final lights with {start_i} button presses, trying {start_i+1}')
                presses.append(press_button(current_lights, end_lights, start_i+1))
        
    if len(presses) == 0:
        res = float('inf')
    else:
        res = min(presses)
    memo[str(start_lights) + '-' + str(start_i) ] = res

    return memo[str(start_lights) + '-' + str(start_i) ]

# e.g. .##. means that 0 has to be pressed an even number of times
#                      1 has to be pressed an odd number of times
#                      2 has to be pressed an odd number of times
#                      3 has to be pressed an even number of times

presses_sum = 0
for line in lines:
    # start_lights = list('.'*(len(line[0])-2))
    # end_lights = list(line[0][1:-1])

    start_lights = list('.'*(len(line[0])-2))
    start_lights = lights_to_mask(start_lights)
    end_lights = list(line[0][1:-1])
    end_lights = lights_to_mask(end_lights)

    memo = {}

    # first try 1 button from all len(line) - 2 buttons
    #   indices 1 to len(line) - 2 for i in range(1, len(line) - 1)
    #   if one of these works - return 1
    #   else
    #       try all combinations of 2 buttons
    #       for i in range(1, len(line) - 1)
    #       for j in range(i+1, len(line) - 1)
    #           if one of these works – return 2
    #           ...

    least_presses = press_button(start_lights, end_lights, 1)
    print(f'least presses: {least_presses}')
    presses_sum += least_presses

print(f'total: {presses_sum}')
