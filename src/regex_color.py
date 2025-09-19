# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
# %%
import re
n = int(input())
for _ in range(n):
    s = input().strip()
    res = re.findall(r'#[0-9a-fA-F]{3}(?![0-9a-fA-F])|#[0-9a-fA-F]{6}(?![0-9a-fA-F])', s)

    # res = re.findall(r'#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}', s)
    if res and ':' in s:
        for r in res:
            # print('*' * 20)
            print(r)

# %%
"""
Valid Hex Color Codes
3
#FFF
#025
#F0A1FB

Invalid Hex Color Codes
3
#fffabg
#abcf
#12365erff

"""

# testcase 0
# input:
"""
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   

"""

# output:
""" 
#BED
"""