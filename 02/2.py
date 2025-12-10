with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split()[0] for line in f.readlines()]
    data = data[0].split(',')

print("Day 2")
print("Part 1:")

total = 0
for d in data:
    for i in range(int(d[:d.index('-')]),int(d[d.index('-')+1:])+1):
        #print(i)
        if len(str(i))%2 == 0:
            half = len(str(i))//2
            if str(i)[:half] == str(i)[half:]:
                total += i
print(total)

print("Part 2:")
total = 0
for d in data:
    for i in range(int(d[:d.index('-')]),int(d[d.index('-')+1:])+1):
        half = len(str(i))//2
        for j in range(1, half+1):
            if str(i)[:j]*(len(str(i))//j) == str(i):
                total += i
                #print(i)
                break
print(total)
