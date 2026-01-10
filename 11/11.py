from datetime import datetime
from multiprocessing import Pool, Value, Array
from math import prod
from ctypes import c_int

with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(' ') for line in f.readlines()]

print("Day 11")
print("Part 1:")

def init_pool_processes(shared_value):
    global zero
    zero = shared_value

def atob(args):
    #print(args)
    start = args[0]
    end = args[1]
    if len(args) == 3:
        DNU=args[2]
    else:
        DNU = None
    multiplicity = {}
    for k in links.keys():
        multiplicity[k] = 0
    multiplicity[start] = 1
    coming_up = [start]
    answer = 0
    while len(coming_up) > 0:
        if zero.value:  # if one of the parellel processes found a zero
            return 0
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
    if answer == 0:
        with zero.get_lock():
            #print("zero")
            zero.value = 1 # True
    return answer

links = {'out':[]}
for d in data:
    key = d[0][:-1]
    links[key] = d[1:]

zero = Value(c_int, 0)
print(atob(('you', 'out')))

print("Part 2:")

# too many to go all at once, need to break into segments
# one path is svr->fft (without dac) * fft->dac * dac->out
# other is svr->dac (without fft) * dac->fft * fft->out


def addone(a):
    print(a)

#atob(('fft', 'dac'))

if __name__ =="__main__":
    zero = Value(c_int, 0)
    with Pool(initializer=init_pool_processes, initargs=(zero,)) as po:
        #print(datetime.now())
        answer2 = prod(po.map(atob, [('svr', 'dac', 'fft'), ('dac', 'fft'), ('fft', 'out')]))
        #print(datetime.now())
        #print(answer2)
        zero.value = 0
        answer2 += prod(po.map(atob, [('svr', 'fft', 'dac'), ('fft', 'dac'), ('dac', 'out')]))
        #print(datetime.now())
        #print(answer2)
#answer2 = atob('svr', 'fft', 'dac')*atob('fft', 'dac')*atob('dac', 'out')
#answer2 += atob('svr', 'dac', 'fft')*atob('dac', 'fft')*atob('fft', 'out')
print(answer2)
