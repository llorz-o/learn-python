import sys
money = [1, 4, 11]

target = 15

cache = {}

cache[0] = 0

for i in range(50):
    cost = 100
    if i == 0:
        continue
    for m in money:
        if i - m >= 0:
            cost = min(cost, cache[i-m] + 1)
    cache[i] = cost
    print(i, cache[i])
