# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
#  
# %%
# from collections import OrderedDict
# %%
# ordinary_dictionary = {}
# ordinary_dictionary['a'] = 1
# ordinary_dictionary['b'] = 2
# ordinary_dictionary['c'] = 3
# ordinary_dictionary['d'] = 4
# ordinary_dictionary['e'] = 5

# print("Ordinary Dictionary:", ordinary_dictionary)
# %%
import sys
from collections import OrderedDict

def main():
    data = sys.stdin.read().strip().split('\n')
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    # print(n)

    ordered_dict = OrderedDict()
    for _ in range(n):
        item = next(it).rsplit(' ', 1)
        # print(item)
        fruit = item[0]
        price = int(item[1])
        if fruit in ordered_dict:
            ordered_dict[fruit] += price
        else:
            ordered_dict[fruit] = price

    for fruit, price in ordered_dict.items():
        print(f"{fruit} {price}")

if __name__ == "__main__":
    main()