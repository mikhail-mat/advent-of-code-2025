with open('daynine.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = [int(coord) for coord in lines[i].split(',')]

def get_area(corner1, corner2):
    return (abs(corner1[0]-corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)

max_area = 0
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        area = get_area(lines[i], lines[j])
        if area > max_area:
            max_area = area

print(max_area)
