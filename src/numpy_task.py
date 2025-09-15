# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
# %%
import numpy

# z = numpy.zeros((1,2), dtype = int)
# z = numpy.zeros((3,3,3), dtype = int)
inv = tuple(map(int, input().split()))
z = numpy.zeros(inv, dtype = int)
o = numpy.ones(inv, dtype = int)
# o = numpy.ones((3,3,3), dtype = int)

print(z) #Type changes to int
print(o) #Type changes to int
#Output : [[0 0]]
# %%

# testcase 0
# input
# 3 3 3
# output

# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]        
