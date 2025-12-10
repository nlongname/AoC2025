with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split()[0] for line in f.readlines()]

print("Day 1")
print("Part 1")

current = 50
answer = 0

for d in data:
    if d[0] == 'L':
        multiplier = -1
    else:
        multiplier = 1
    current += multiplier*int(d[1:])
    current %= 100
    if current == 0:
        answer += 1

print(answer)
print("Part 2")

current = 50
previous = 50
answer = 0

for d in data:
    if d[0] == 'L':
        multiplier = -1
    else:
        multiplier = 1
    for i in range(int(d[1:])):
        current += multiplier
        current %= 100
        if current == 0:
            answer += 1
print(answer)
