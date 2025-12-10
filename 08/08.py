import math

with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(',') for line in f.readlines()]

data = [[int(x) for x in d] for d in data]

print("Day 8")
print("Part 1:")

n = 1000
distance_sq = {}
for i in range(len(data)):
    for j in range(i+1, len(data)):
        d_sq = (data[i][0]-data[j][0])**2 + (data[i][1]-data[j][1])**2 + (data[i][2]-data[j][2])**2
        distance_sq[(i, j)] = d_sq

connections = sorted(list(distance_sq.keys()), key=lambda x: distance_sq[x])

boxes = []
count = 0

while count < n:
    for i in range(len(connections)):
        c = connections[i]
        linked = []
        found = False
        for b in range(len(boxes)):
            if not found and c[0] in boxes[b] and c[1] in boxes[b]:
                # "nothing happens"
                found = True
            if c[0] in boxes[b] or c[1] in boxes[b]:
                linked.append(b)
                found = True
        if not found:
            boxes.append(list(c))
            count += 1
        if len(linked) == 2:
            boxes[linked[0]] = list(set(boxes[linked[0]]+boxes[linked[1]]))
            boxes[linked[1]] = []
            count += 1
        elif len(linked) == 1:
            boxes[linked[0]] = list(set(boxes[linked[0]]+list(c)))
            count += 1
        if count == n:
            break

#print(boxes)
bs = sorted([len(b) for b in boxes])
print(math.prod(bs[-3:]))

print("Part 2:")
last_connection = 0
boxes = [b for b in boxes if b != []]
while len(boxes) > 1:
    for i in range(len(connections)):
        c = connections[i]
        linked = []
        found = False
        for b in range(len(boxes)):
            if not found and c[0] in boxes[b] and c[1] in boxes[b]:
                # "nothing happens"
                found = True
            if c[0] in boxes[b] or c[1] in boxes[b]:
                linked.append(b)
                found = True
        if not found:
            boxes.append(list(c))
            count += 1
        if len(linked) == 2:
            boxes[linked[0]] = list(set(boxes[linked[0]]+boxes[linked[1]]))
            boxes[linked[1]] = []
            last_connection = c
            count += 1
        elif len(linked) == 1:
            boxes[linked[0]] = list(set(boxes[linked[0]]+list(c)))
            last_connection = c
            count += 1
        boxes = [b for b in boxes if b != []]
        if len(boxes[0])==len(data):
            break
        
print(data[last_connection[0]][0]*data[last_connection[1]][0])
