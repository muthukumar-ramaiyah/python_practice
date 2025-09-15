# https://www.hackerrank.com/challenges/np-identity-and-eye/problem?isFullScreen=true
# %%
import numpy
numpy.set_printoptions(legacy='1.13') # To match the output format
# print(numpy.identity(3)) #3 is for  dimension 3 X 3

# # %%
# print(numpy.eye(8, 7))    # 8 X 7 Dimensional array with first upper diagonal 1.
# # %%
# print(numpy.eye(8, 7, k = 1))    # 8 X 7 Dimensional array with first upper diagonal 1.
# # %%
# print(numpy.eye(8, 7, k = -9))    # 8 X 7 Dimensional array with first upper diagonal 1.

# # %%
n, m = map(int, input().split())
print(numpy.eye(n, m, k = 0))    # 8 X


# testcase 0
# input
# 3 3

# output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

