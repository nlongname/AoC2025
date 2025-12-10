with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    data = [[d for d in r] for r in data]
print("Day 4")

length = len(data)
width = len(data[0]) #assuming a rectangle for now

part_one = True
removing = []
moved = None
total = 0
while moved != 0:
    moved = 0
    for y in range(length):
        for x in range(width):
            if data[y][x] == '@':
                neighbors = -1 #going to count itself as a neighbor, -1 to counteract
                for i in [x-1, x, x+1]:
                    if i >= 0 and i < width:
                        for j in [y-1, y, y+1]:
                            if j >= 0 and j < length and data[j][i] == '@':
                                neighbors += 1
                if neighbors < 4:
                    removing.append((x, y))
                    moved += 1
    if part_one:
        print("Part 1:")
        print(moved)
        part_one = False
    total += moved
    for r in removing:
        data[r[1]][r[0]]='.'
    removing = []
print("Part 2:")
print(total)

