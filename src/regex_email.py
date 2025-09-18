# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
# %%
import re
n = int(input())
for _ in range(n):
    s = input().strip()
    # if re.match(r'<[a-zA-Z]*[a-zA-Z0-9-_.]@[a-zA-Z]*.[a-zA-Z]{1,3}>', s):
    if re.match(r'.*<[a-zA-Z][a-zA-Z0-9-_.]*@[a-zA-Z]*\.[a-zA-Z]{1,3}>', s):
        print('*' * 20)
        print(s)
    # res = re.match(r'.*<[a-zA-Z][a-zA-Z-_.]*@[a-zA-Z]*.[a-zA-Z]{1,3}>', s)
    # print("res:", res)



# %%
# testcase 0
# input:
"""
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

"""
# output:
"""
DEXTER <dexter@hotmail.com>
"""

# %%

"""
3
DEXTER <dexter@hotmail.com>
DEXTER <dexter@hotmail.com2>
DEXTER <dexter@hotmail.co>

"""

# testcase 1
# input:
"""
9
vin <vineet@>
vineet <vineet@gmail.com>
vineet <vineet@gma.il.co.m>
vineet <vineet@gma-il.co-m>
vineet <vineet@gma,il.co@m>
vineet <vineet@gmail,com>
vineet <.vin@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>

"""
# output:
"""
vineet <vineet@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>
"""


# %%# testcase 2
# input:
"""
1
vineet <vineet@gmail,com>

"""
# output:
# (no output)

# %%# testcase 3
# input:
"""
7
dheeraj <dheeraj-234@gmail.com>
crap <itsallcrap>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
mattp <matt23@@india.in>
harsh <.harsh_1234@rediff.in>
harsh <-harsh_1234@rediff.in>

"""
# output:
"""
dheeraj <dheeraj-234@gmail.com>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
"""

# testcase 4
# input:
"""
1
dheeraj <dheeraj-234@gmail.com>

"""
# output:
"""
dheeraj <dheeraj-234@gmail.com>
"""