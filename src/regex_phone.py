# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# %%
import re
N = int(input())
for _ in range(N):
    s = input().strip()
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")

# %%
# testcase 0
# input:
"""
2
9587456281
1252478965

"""
# output:
# YES
# NO
# %%