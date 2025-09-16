# !/usr/bin/env python3
# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# %%

if __name__ == '__main__':
    records = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.add(score)
    scores = list(scores)
    scores.sort()
    second_lowest = scores[1]
    names = []
    for record in records:
        if record[1] == second_lowest:
            names.append(record[0])
    names.sort()
    for name in names:
        print(name)

# testcase 0
# input:
# 5
# Harry
# 37.21
# Berry         
# 37.21
# Tina
# 37.21
# Akriti
# 41.0
# Harsh
# 39.0

# output:
# Berry
# Harry
