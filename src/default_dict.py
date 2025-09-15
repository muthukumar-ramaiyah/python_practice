# %%
# DefaultDict Tutorial
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# for i in d.items():
#     print(i)
# # %%
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)
# print(d['python'])
# # %%
# print(d['something-else2'])

# %%

counts = input()
n, m = counts.split()
# print(n, m)
a = []
b = []
for i in range(int(n)):
    a.append(input())
for j in range(int(m)):
    b.append(input())

# print(a)
# print(b)

# from collections import defaultdict
d = defaultdict(list)
for x in b:
    for i, y in enumerate(a):
        if x == y:
            d[x].append(i + 1)

# print(d)

for k in b:
    if k not in d:
        d[k].append(-1)  
    print(' '.join(map(str, d[k])))

# %%
# input sequence copy as it is
# 5 2
# a
# a
# b
# a
# b
# a
# b


# output
# 1 2 4
# 3 5⏎  