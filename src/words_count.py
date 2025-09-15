# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# %%
from collections import defaultdict

def main():
    n = int(input())
    word_count = defaultdict(int)

    for _ in range(n):
        word = input().strip()
        word_count[word] += 1

    print(len(word_count))
    print(' '.join(str(count) for count in word_count.values()))

if __name__ == "__main__":
    main()