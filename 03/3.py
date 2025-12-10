from itertools import combinations

def find_best(numbers, digits):
    total = 0
    for d in numbers:
        temp = [x for x in d]
        ans = []
        while len(ans) < digits:
            if len(ans)+1 == digits:
                largest = max(temp)
            else:
                largest = max(temp[:-digits+len(ans)+1])
            ans.append(largest)
            temp = temp[temp.index(largest)+1:]
        total += sum([10**(digits-i-1)*ans[i] for i in range(len(ans))])
    return total

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    data = [[int(x) for x in d] for d in data]

print("Day 3")
print("Part 1:")

print(find_best(data, 2))

print("Part 2:")

print(find_best(data, 12))
