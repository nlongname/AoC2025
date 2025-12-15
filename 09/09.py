import pprint

with open('test_input.txt', 'r+') as f:
    data = [line.strip('\n').split(',') for line in f.readlines()]

data = [[int(x) for x in d] for d in data]

print("Day 9")
print("Part 1:")

maximum = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        area = (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1)
        if area > maximum:
            maximum = area
print(maximum)

print("Part 2:")

left_candidates = []
right_candidates = []
lefts = 0
rights = 0
for i in range(len(data)):
    prev_pt = data[i-1]
    current_pt = data[i]
    next_pt = data[(i+1)%len(data)]
    v_1 = [current_pt[0]-prev_pt[0], current_pt[1]-prev_pt[1]]
    v_2 = [next_pt[0]-current_pt[0], next_pt[1]-current_pt[1]]

    delta = [-v_1[0]/abs(sum(v_1))+v_2[0]/abs(sum(v_2)), -v_1[1]/abs(sum(v_1))+v_2[1]/abs(sum(v_2))]
    candidate = (int(current_pt[0] + delta[0]), int(current_pt[1]+delta[1]))
    anti_candidate = (int(current_pt[0] - delta[0]), int(current_pt[1] - delta[1]))
    if v_1[0]*v_2[1] > v_1[1]*v_2[0]: # cross-product, right hand rule
        right_candidates.append(candidate)
        left_candidates.append(anti_candidate)
        rights += 1
    else:
        left_candidates.append(candidate)
        right_candidates.append(anti_candidate)
        lefts += 1
if rights > lefts: #going clockwise, so right-candidates are interior
    candidates = right_candidates
    anti = left_candidates
else: #going counterclockwise, this set are interior
    candidates = left_candidates
    anti = right_candidates
print(candidates)

width = max(data, key=lambda x: x[0])[0]+2
#min_x = min(data, key=lambda x: x[0])[0]
height = max(data, key=lambda x: x[1])[1]+2
#min_y = min(data, key=lambda x: x[1])[1]-1
domain = [['.' for i in range(width)] for j in range(height)] 

for i in range(len(data)):
    d = data[i]
    if data[i-1][0] == data[i][0]: #vertical
        for j in range(min(data[i-1][1], data[i][1])+1, max(data[i-1][1], data[i][1])):
            domain[j][data[i][0]] = 'x'
    if data[i-1][1] == data[i][1]: #horizontal
        for j in range(min(data[i-1][0], data[i][0])+1, max(data[i-1][0], data[i][0])):
            domain[data[i][1]][j] = 'x'
    x, y = d
    domain[y][x] = '#'
for c in candidates:
    domain[c[1]][c[0]]= 'c'
for a in anti:
    domain[a[1]][a[0]] = 'a'
pprint.pprint(domain)

maximum = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        area = (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1)
        conflicts = [a for a in anti if (a[0]-data[i][0])*(a[0]-data[j][0])<0 and (a[1]-data[i][1])*(a[1]-data[j][1])<0]
        if conflicts == [] and area > maximum:
            maximum = area
print(maximum)
