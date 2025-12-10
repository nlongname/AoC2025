with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

print("Day 5")
print("Part 1:")
rules = []
phase_one = True
fresh = 0
for i in range(len(data)):
    current = data[i]
    if phase_one and current != '':
        b = int(current[:current.index('-')])
        e = int(current[current.index('-')+1:])
        rules.append((b, e))
    elif current == '':
        phase_one = False
    else:
        for r in rules:
            b, e = r
            if b <= int(current) and int(current) <= e:
                #print(f'{(b, e)}, {current}')
                fresh += 1
                break
print(fresh)

print("Part 2:")
rules.sort(key=lambda x:x[0]) #crucial, or some rules don't get cross-linked properly
new_rules = []
for r in rules:
    r_b, r_e = r
    if new_rules == []:
        new_rules = [r]
    else:
        melded = False
        for n in new_rules:
            n_b, n_e = n
            if (n_b <= r_b and r_b <= n_e) or (n_b <= r_e and r_e <= n_e):
                new_rules[new_rules.index(n)] = (min(r_b, n_b), max(r_e, n_e))
                melded = True
        if not melded:
            new_rules.append(r)
possible = 0
for n in new_rules:
    n_b, n_e = n
    possible += (n_e-n_b+1)
print(possible)
