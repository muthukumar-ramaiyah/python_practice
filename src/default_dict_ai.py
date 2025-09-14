# solution.py
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    positions = defaultdict(list)

    # read n words and record 1-based indices
    for i in range(1, n + 1):
        word = next(it)
        positions[word].append(i)

    # print("positions:", positions)

    out_lines = []
    # read m query words
    for _ in range(m):
        q = next(it)
        if q in positions:
            out_lines.append(" ".join(map(str, positions[q])))
        else:
            out_lines.append("-1")

    # print("out_lines:", out_lines)
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
