# %% [markdown]
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fibonacci_series(10))  
# ➝ [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
