from datetime import datetime

with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(' ') for line in f.readlines()]

print("Day 11")
print("Part 1:")

def atob(start, end, DNU=None):
    multiplicity = {}
    for k in links.keys():
        multiplicity[k] = 0
    multiplicity[start] = 1
    coming_up = [start]
    answer = 0
    while len(coming_up) > 0:
        #print(coming_up)
        current = coming_up[0]
        if current == DNU:
            multiplicity[DNU] = 0
            coming_up.remove(DNU)
        elif current == end:
            answer += multiplicity[end]
            multiplicity[end] = 0
            coming_up.remove(end)
        else:
            for i in links[current]:
                if i != DNU:
                    multiplicity[i] += multiplicity[current]
                    coming_up.append(i)
            multiplicity[current] = 0
            coming_up.remove(current)
            coming_up = list(set(coming_up))
    return answer

links = {'out':[]}
for d in data:
    key = d[0][:-1]
    links[key] = d[1:]

print(atob('you', 'out'))

print("Part 2:")

# too many to go all at once, need to break into segments
# one path is svr->fft (without dac) * fft->dac * dac->out
# other is svr->dac (without fft) * dac->fft * fft->out
#print(datetime.now())
answer2 = atob('svr', 'fft', 'dac')*atob('fft', 'dac')*atob('dac', 'out')
#print(datetime.now())
#print(answer2)
answer2 += atob('svr', 'dac', 'fft')*atob('dac', 'fft')*atob('fft', 'out')
#print(datetime.now())
print(answer2)
