import math

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
print("Day 7")
print("Part 1:")

beams = set([data[0].index('S')])
splits = 0

for i in range(2, len(data), 2):
    new_beams = set()
    for j in [k for k in range(len(data[0])) if data[i][k]=='^']:
        if j in beams:
            beams.add(j-1)
            beams.add(j+1)
            beams.remove(j)
            splits += 1        
    #print(beams)
print(splits)

print("Part 2:")
beams = [0 for i in range(len(data[0]))]
beams[data[0].index('S')] = 1

for i in range(2, len(data), 2):
    for j in [k for k in range(len(data[0])) if data[i][k]=='^']:
        multiplicity = beams[j]
        if multiplicity != 0:
            beams[j-1] += multiplicity
            beams[j+1] += multiplicity
            beams[j] = 0       
    #print(beams)
print(sum(beams))

