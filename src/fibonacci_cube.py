# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
# %%
cube = lambda x: x ** 3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == '__main__':
    n = int(input("enter the number of terms: "))
    print(list(map(cube, fibonacci(n))))
# %%
