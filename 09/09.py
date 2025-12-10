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
width = max(data, key=lambda x: x[0])[0]+2
min_x = min(data, key=lambda x: x[0])[0]-1
height = max(data, key=lambda x: x[1])[1]+2
min_y = min(data, key=lambda x: x[1])[1]-1
domain = [['.' for i in range(min_x, width)] for j in range(min_y, height)] 

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
pprint.pprint(domain)

seed = (0, 0)
domain[0][0] = '-'
flood = [(0, 1), (1, 0)]
checked = [(0,0)]
while len(flood) > 0:
    f = flood[0]
    if domain[f[1]][f[0]] not in ['-', '#', 'x']:
        domain[f[1]][f[0]] = '-'
        checked.append(f)
        for i in range(-1, 2):
            for j in range(-1, 2):
                test = (f[0]+i, f[1]+j)
                if test not in checked:
                    flood.append(test)
    flood = flood[1:]

pprint.pprint(domain)

maximum = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        still_in = True
        area = (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1)
        if area > maximum:
            for x in range(min(data[i][0], data[j][0]), max(data[i][0], data[j][0])+1):
                for y in range(min(data[i][1], data[j][1]), max(data[i][1], data[j][1])+1):
                    if domain[y][x] not in ['#', 'x', '.']:
                        still_in = False
                        break
            if still_in:
                maximum = area
print(maximum)
