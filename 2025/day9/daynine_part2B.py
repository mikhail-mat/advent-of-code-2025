with open('daynine.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = [int(coord) for coord in lines[i].split(',')]

n = len(lines)

#outer_shape = []
row_map = dict()
col_map = dict()
for i in range(len(lines)):
    if i % 2 == 0: # DONT FORGET TO CHANGE BETWEEN TEST AND REAL DATA
        if lines[i][1] > lines[(i+1) % n][1]:
            step = -1
        else:
            step = 1
        # for row in range(lines[i][1], lines[(i+1) % n][1], step):
        for row in range(lines[i][1], lines[(i+1) % n][1] + step, step):
            # outer_shape.append([lines[i][0], row])
            if lines[i][0] in col_map:
                col_map[lines[i][0]].add(row)
            else:
                col_map[lines[i][0]] = {row}
    else:
        if lines[i][0] > lines[(i+1) % n][0]:
            step = -1
        else:
            step = 1
        # for col in range(lines[i][0], lines[(i+1) % n][0], step):
        for col in range(lines[i][0], lines[(i+1) % n][0] + step, step):
            # outer_shape.append([col, lines[i][1]])
            if lines[i][1] in row_map:
                row_map[lines[i][1]].add(col)
            else:
                row_map[lines[i][1]] = {col}

for col in col_map.keys():
    for row in row_map.keys():
        if col in row_map[row]:
            col_map[col].add(row)

for row in row_map.keys():
    for col in col_map.keys():
        if row in col_map[col]:
            row_map[row].add(col)

for col in col_map.keys():
    for new_row in col_map[col]:
        if new_row not in row_map:
            row_map[new_row] = {col}
        else:
            row_map[new_row].add(col)

for row in row_map.keys():
    for new_col in row_map[row]:
        if new_col not in col_map:
            col_map[new_col] = {row}
        else:
            col_map[new_col].add(row)

print(f'columns: {col_map}')
print(f'rows: {row_map}')

def get_area(corner1, corner2):
    return (abs(corner1[0]-corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)

def get_other_corners(corner1, corner2):
    corner3 = [corner1[0], corner2[1]]
    corner4 = [corner2[0], corner1[1]]
    return corner3, corner4

def inside_shape(corner):
    # same_y = []
    # same_x = []
    # for vertex in outer_shape:
    #     if vertex[0] == corner[0]:
    #         same_y.append(vertex[1])
    #     if vertex[1] == corner[1]:
    #         same_x.append(vertex[0])
    # # print(same_y)
    # # print(same_x)
    # if (min(same_y) <= corner[1] <= max(same_y) and
    #     min(same_x) <= corner[0] <= max(same_x)):
    #     return True
    # return False
    if (corner[0] >= min(row_map[corner[1]]) and corner[0] <= max(row_map[corner[1]]) and
        corner[1] >= min(col_map[corner[0]]) and corner[1] <= max(col_map[corner[0]])):
        print(f'{corner[0]} is between {min(row_map[corner[1]])} and {max(row_map[corner[1]])}')
        print(f'{corner[1]} is between {min(col_map[corner[0]])} and {max(col_map[corner[0]])}')
        return True
    print(f'{corner[0]} is NOT between {min(row_map[corner[1]])} and {max(row_map[corner[1]])}')
    print(f'OR {corner[1]} is NOT between {min(col_map[corner[0]])} and {max(col_map[corner[0]])}')
    return False

max_area = 0
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        corner3, corner4 = get_other_corners(lines[i], lines[j])
        print(f'rectangle {lines[i]} {lines[j]} {corner3} {corner4}')
        if inside_shape(corner3) and inside_shape(corner4):
            area = get_area(lines[i], lines[j])
            if area > max_area:
                max_area = area

print(max_area)
