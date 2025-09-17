# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
# %%
import re

# #Squaring numbers
# def square(match):
#     number = int(match.group(0))
#     return str(number**2)

# print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))
# # %%

# import re

# html = """
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# """

# print(re.sub("(<!--.*?-->)", "", html)) #remove comment

# %%
def helper(match):
    str = match.group(0)
    x,y = match.span()
    # print(f"matched: {str}")
    # return " and " if str == " && " else " or "
    if str == "&&" and match.string[x-1] == ' ' and match.string[y] == ' ':
        return "and"
    elif str == "||" and match.string[x-1] == ' ' and match.string[y] == ' ':
        return "or"
    return str

n = int(input())
for _ in range(n):
    s = input()
    # print(re.sub(r"[ ]+[&]{2}[ ]+|[ ]+[|]{2}[ ]+", helper, s))
    print(re.sub(r"[&]{2}|[|]{2}", helper, s))

# %%
# testcase 0
# input:
"""
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""

# output:
"""
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""

# testcase 1
# input:
"""
1
n && && && && && &&n
"""
# output:
"""
n and and and and and &&n
"""