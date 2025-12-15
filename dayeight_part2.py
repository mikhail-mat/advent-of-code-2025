import heapq

with open('dayeight.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = [int(coor) for coor in lines[i].split(',')]

def compute_distance(junc_box1, junc_box2):
    distance = ((junc_box1[0]-junc_box2[0])**2 
                + (junc_box1[1]-junc_box2[1])**2 
                + (junc_box1[2]-junc_box2[2])**2) ** 0.5
    return distance

juncboxes = []
distances = []
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        juncboxes.append(str(i) + '-' + str(j))
        distances.append(compute_distance(lines[i], lines[j]))

circuits = []
for i in [distances.index(d) for d in heapq.nsmallest(5000, distances)]:
    juncboxA = juncboxes[i].split('-')[0]
    juncboxB = juncboxes[i].split('-')[1]

    print(f'juncbox A index: {juncboxA}, juncbox B index: {juncboxB}, distance: {distances[i]}')

    juncboxA_set = None
    juncboxB_set = None

    for j in range(len(circuits)):
        if juncboxA in circuits[j]:
            print(f'juncboxA {juncboxA} is in set {circuits[j]}')
            juncboxA_set = j
        
        if juncboxB in circuits[j]:
            print(f'juncboxB {juncboxB} is in set {circuits[j]}')
            juncboxB_set = j

    if juncboxA_set != None and juncboxB_set != None:
        if juncboxA_set != juncboxB_set:
            merged_set = circuits[juncboxA_set].union(circuits[juncboxB_set])
            print(f'juncbox A and B are both already in sets, merged set {merged_set}')
            print(f'A set: {circuits[juncboxA_set]}, B set: {circuits[juncboxB_set]}')
            circuits.remove(circuits[juncboxA_set])
            offset = 0
            if juncboxA_set < juncboxB_set:
                offset = -1
            circuits.remove(circuits[juncboxB_set + offset])
            circuits.append(merged_set)
    elif juncboxA_set != None:
        circuits[juncboxA_set].add(juncboxB)
        print(f'juncbox B was added to {circuits[juncboxA_set]}')
    elif juncboxB_set != None:
        circuits[juncboxB_set].add(juncboxA)
        print(f'juncbox A was added to {circuits[juncboxB_set]}')
    else:
        print('creating a new set of two juncboxes')
        new_set = {juncboxA, juncboxB}
        circuits.append(new_set)
    
    print(circuits)

    if len(circuits) == 1:
        if len(circuits[0]) == 1000:
            print(lines[int(juncboxA)][0]*lines[int(juncboxB)][0])
            break
