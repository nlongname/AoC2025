from itertools import combinations, product
from functools import reduce

with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(' ') for line in f.readlines()]
goals = [d[0].strip('[]') for d in data]
switches = [[[int(i) for i in x.strip('()').split(',')] for x in d[1:-1]] for d in data]
joltages = [[int(i) for i in d[-1].strip('{}').split(',')] for d in data]

print("Day 10")
print("Part 1:")

for i in range(len(goals)):
    g = goals[i]
    g = g.replace('#', '1')
    g = g.replace('.', '0')
    g = g[::-1]
    g = int(g, base=2)
    goals[i] = g #I think this is all worth it so the ops are XORs, we'll see

switches_one = [[y for y in x] for x in switches]
for i in range(len(switches_one)):
    for j in range(len(switches_one[i])):
        switches_one[i][j] = sum([2**k for k in switches_one[i][j]])

answers = [None for d in data]
for i in range(len(data)):
    g = goals[i]
    s = switches_one[i]
    done = False
    n = 0
    if g == 0:
        answers[i] = 0
        done = True
    while not done and n < len(s):
        n += 1
        for combo in combinations(s, n):
            if reduce(lambda x,y: x^y, combo) == g:
                answers[i] = n
                done = True
                break
print(sum(answers))

print("Part 2")
answers_two = [None for d in data]
total = 0
for i in range(len(data)):
    j = joltages[i]
    s = switches[i]
    maxes = [min(j[s[x][i]] for i in range(len(s[x]))) for x in range(len(s))]
    prod = 'product('
    for m in maxes:
        prod += f'range({m}, -1, -1), '
    prod += ')'
    prod = eval(prod)
    best = 10**6
    for combo in prod:
        combo_total = sum(combo)
        if combo_total < 3*max(j) and combo_total < best and combo_total >= max(j):
            #print(f'n={sum(combo)}')
            test = [0 for x in j]
            for i in range(len(combo)):
                for x in s[i]:
                    test[x] += combo[i]
            if test == j:
                best = min(sum(combo), best)
                print(best)
    total += best
print(total)              
            
            
