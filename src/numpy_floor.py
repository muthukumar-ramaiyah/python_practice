# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
# %%
import numpy

# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print(numpy.floor(my_array))         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# # %%

# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print(numpy.ceil(my_array))          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# # %%

# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print(numpy.rint(my_array))          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
# # %%

numpy.set_printoptions(legacy='1.13') # To match the output format
my_array = numpy.array(list(map(float, input().split())))
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))

# testcase 0
# input
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
# output
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]     
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]    
# %%
