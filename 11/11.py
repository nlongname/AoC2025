with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(' ') for line in f.readlines()]

print("Day 11")
print("Part 1:")

links = {}
multiplicity = {}
for d in data:
    key = d[0][:-1]
    links[key] = d[1:]
    multiplicity[key] = 0
multiplicity['svr'] = 1
multiplicity['out'] = 0
coming_up = ['svr']

answer = 0
while len(coming_up) > 0:
    current = coming_up[0]
    if current == 'out':
        answer += multiplicity['out']
        multiplicity['out'] = 0
        coming_up.remove('out')
    else:
        for i in links[current]:
            multiplicity[i] += multiplicity[current]
            coming_up.append(i)
        multiplicity[current] = 0
        coming_up.remove(current)
        coming_up = list(set(coming_up))
print(answer)

print("Part 2:")
# needs to go from svr to out through both fft & dac
# split into two cases depending on which comes first
# mult svr->fft by fft->dac by dac->out
# and mult svr->dac by dac->fft by fft->out
# but need to make sure e.g. svr->dac doesn't includ svr->fft->dac

def atob(start, end, DoNotUse):
    print('a')
