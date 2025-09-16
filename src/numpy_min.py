# //usr/bin/env python3
# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# %%
import numpy
import sys
# %%
data = sys.stdin.read().strip().split('\n')
r, c = map(int, data[0].split())

print(r, c)
# # Method 1: Using for loop
my_array = numpy.array([list(map(int, data[i + 1].split())) for i in range(r)])

print(max(numpy.min(my_array, axis=1)))

# python src/numpy_min.py < tests/input/numpy_min_0

# testcase 0

# input
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0

# output
# 3

