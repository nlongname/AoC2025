import math

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

transposed = [''.join(data[y][i] for y in range(len(data)-1)) for i in range(len(data[0]))]

data = [line.split() for line in data]

print("Day 6")
print("Part 1:")

total = 0
for i in range(len(data[0])):
    operands = [int(data[y][i]) for y in range(len(data)-1)]
    if data[-1][i] == '*':
        total += math.prod(operands)
    else:
        total += sum(operands)
print(total)

print("Part 2:")

operands = []
problems = 0
total = 0
for t in transposed+['']:
    if t.strip() != '':
        operands.append(int(t))
    else:
        if data[-1][problems] == '*':
            total += math.prod(operands)
        else:
            total += sum(operands)
        #print(data[-1][problems])
        #print(operands)
        operands = []
        problems += 1
print(total)
