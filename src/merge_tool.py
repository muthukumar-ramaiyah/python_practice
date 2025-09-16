# //usr/bin/env python3
# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# %%

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        t = string[i:i+k]
        u = ''.join(sorted(set(t), key=t.index))
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# %%
# testcase 0
# input:
# AABCAAADA
# 3
# output:
# AB
# CA
# AD