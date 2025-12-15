import pprint

with open('input.txt', 'r+') as f:
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
#print(candidates)

border = []
for i in range(len(data)):
    d = data[i]
    border.append(tuple(d))
    if data[i-1][0] == data[i][0]: #vertical
        for j in range(min(data[i-1][1], data[i][1])+1, max(data[i-1][1], data[i][1])):
            border.append((data[i][0], j))
    if data[i-1][1] == data[i][1]: #horizontal
        for j in range(min(data[i-1][0], data[i][0])+1, max(data[i-1][0], data[i][0])):
            border.append((j, data[i][1]))
shell = []
for i in range(len(anti)):
    a = anti[i]
    shell.append(tuple(a))
    if anti[i-1][0] == anti[i][0]: #vertical
        for j in range(min(anti[i-1][1], anti[i][1])+1, max(anti[i-1][1], anti[i][1])):
            shell.append((anti[i][0], j))
    if anti[i-1][1] == anti[i][1]: #horizontal
        for j in range(min(anti[i-1][0], anti[i][0])+1, max(anti[i-1][0], anti[i][0])):
            shell.append((j, anti[i][1]))
#shell = [s for s in shell if s not in border]

maximum = 0
for i in range(len(data)):
    print(i)
    for j in range(i+1, len(data)):
        area = (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1)
        if area > maximum:
            min_x = min(data[i][0], data[j][0])
            max_x = max(data[i][0], data[j][0])
            min_y = min(data[i][1], data[j][1])
            max_y = max(data[i][1], data[j][1])
            conflicted = False
            for s in shell:
                if min_x <= s[0] and s[0] <= max_x and min_y <= s[1] and s[1] <= max_y:
                    conflicted = True
                    break
            if not conflicted:
                print((i, j), area)
                maximum = area
print(maximum)
