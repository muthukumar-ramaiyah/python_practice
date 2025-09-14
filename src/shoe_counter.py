# %%
# Problem Statement: https://www.hackerrank.com/challenges/collections-counter/problem
# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter
# %%
N = input("Enter the number of shoes: ")
shoes = list(map(int, input("Enter the shoe sizes: ").split()))
# print("Shoe sizes count:", Counter(shoes))
X = int(input("Enter the number of customers: "))
total_amount = 0

for _ in range(X):
    size, price = map(int, input("Enter the shoe size and price: ").split())
    # print(size, price)
    if size in shoes:
        total_amount += price
        shoes.remove(size)

# print("Total amount earned:", total_amount)
print(total_amount)


# %%
# input sequence copy as it is
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# output
# 200
# hackerrank
# %%
