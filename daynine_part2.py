with open('daynine.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = [int(coord) for coord in lines[i].split(',')]

inside = set()
n = len(lines)

def get_area(corner1, corner2):
    return (abs(corner1[0]-corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)

def inside_or_bound(i):
    # if the tile before current tile was lower than it on the grid
    # and if the tile after current tile will be to the left of it on the grid
    # mark tile as "inside the shape (safe bounds)"
    if lines[(i-1) % n][1] > lines[i][1] and lines[(i+1) % n][0] < lines[i][0]:
        inside.add(i)
    # if the tile before current tile was to the left of it on the grid
    # and if the tile after current tile will be higher than it on the grid
    # mark tile as "inside the shape (safe bounds)"
    elif lines[(i-1) % n][0] < lines[i][0] and lines[(i+1) % n][1] < lines[i][1]:
        inside.add(i)
    # if the tile before current tile was higher than it on the grid
    # and if the tile after current tile will be to the right of it on the grid
    # mark tile as "inside the shape (safe bounds)"
    elif lines[(i-1) % n][1] < lines[i][1] and lines[(i+1) % n][0] > lines[i][0]:
        inside.add(i)
    # if the tile before current tile was to the right of it on the grid
    # and if the tile after current tile will be lower than it on the grid
    # mark tile as "inside the shape (safe bounds)"
    elif lines[(i-1) % n][0] > lines[i][0] and lines[(i+1) % n][1] > lines[i][1]:
        inside.add(i)
    # otherwise mark tile as a "bound tile"
    # do nothing

def get_rec_edge_vertices(vertex1, vertex2):
    rec_edge_vertices = []
    for i in range(len(lines)):
        if (min(vertex1[1], vertex2[1]) < lines[i][1] < max(vertex1[1], vertex2[1]) and 
            lines[i][0] == vertex1[0] or
            min(vertex1[1], vertex2[1]) < lines[i][1] < max(vertex1[1], vertex2[1]) and 
            lines[i][0] == vertex2[0]):
            rec_edge_vertices.append(i)
        elif (min(vertex1[0], vertex2[0]) < lines[i][0] < max(vertex1[0], vertex2[0]) and 
            lines[i][1] == vertex1[1] or
            min(vertex1[0], vertex2[0]) < lines[i][0] < max(vertex1[0], vertex2[0]) and 
            lines[i][1] == vertex2[1]):
            rec_edge_vertices.append(i)
    return rec_edge_vertices

def get_corners(vertex1, vertex2):
    corners = []
    if [vertex1[0], vertex2[1]] in lines:
        corners.append(lines.index([vertex1[0], vertex2[1]]))
    if [vertex2[0], vertex1[1]] in lines:
        corners.append(lines.index([vertex2[0], vertex1[1]]))
    #print(f'corners of {vertex1} and {vertex2} are {corners}')
    return corners

for i in range(len(lines)):
    inside_or_bound(i)

#print(inside)

max_area = 0
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        if i in inside and j in inside:
            #print(f'{lines[i]} and {lines[j]} are inside vertices!')
            area = get_area(lines[i], lines[j])
            if area > max_area:
                max_area = area
        elif i in inside or j in inside:
            if i not in inside:
                bound_corner = i
            else:
                bound_corner = j
            
            rec_edge_vertices = get_rec_edge_vertices(lines[i], lines[j])
            
            connected = True
            
            if lines[i][0] != lines[j][0] and lines[i][1] != lines[j][1]:
                for corner in get_corners(lines[i], lines[j]):
                    if (corner + 1) % n == bound_corner or (corner - 1) % n == bound_corner:
                        #print(f'{lines[corner]} is connected to {lines[bound_corner]}!')
                        pass
                    else:
                        #print(f'{lines[corner]} is not connected to {lines[bound_corner]}')
                        connected = False
                        break
            
            for vertex in rec_edge_vertices:
                if vertex not in inside:
                    #print(f'{lines[vertex]} is convex and on the sides of rectangle {lines[i]} and {lines[j]}')
                    connected = False
                    break

            if connected:
                area = get_area(lines[i], lines[j])
                if area > max_area:
                    max_area = area
    print(i)

print(max_area)
