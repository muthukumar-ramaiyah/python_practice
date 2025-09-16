#  https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
# %%
import numpy
import sys
# my_array = numpy.array([[1, 2], [3, 4]])

# print(numpy.sum(my_array, axis=0))  # Output : [4 6]
# print(numpy.sum(my_array, axis=1))  # Output : [3 7]
# print(numpy.sum(my_array, axis=None))  # Output : 10
# print(numpy.sum(my_array))  # Output : 10

# # %%
# print(numpy.prod(my_array, axis=0))  # Output : [3 8]
# print(numpy.prod(my_array, axis=1))  # Output : [ 2 12]
# print(numpy.prod(my_array, axis=None))  # Output : 24
# print(numpy.prod(my_array))  # Output : 24

# %%
data = sys.stdin.read().strip().split('\n')
r, c = map(int, data[0].split())
# print(r, c)
# # Method 1: Using for loop
# two_d_array = []
# for i in range(r):
#     two_d_array.append(list(map(int, data[i + 1].split())))
# my_array = numpy.array(two_d_array)
# print(my_array)

# # Method 2: Using for loop
my_array = numpy.array([list(map(int, data[i + 1].split())) for i in range(r)])

print(numpy.prod(numpy.sum(my_array, axis=0), axis=0))

# python src/numpy_sum.py < tests/input/numpy_sum_0

# testcase 0
# input
# 2 2
# 1 2
# 3 4
# output
# 24
