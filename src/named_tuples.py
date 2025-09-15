# solution.py
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
import sys
from collections import namedtuple

def main():
    data = sys.stdin.read().strip().split('\n')
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    # print(next(it))  # Skip header line
    columns = ','.join(next(it).split())

    # print(n)
    # print(columns)

    # students = (namedtuple('Student', columns)
    students = []
    total_marks = 0
    for _ in range(n):
        values = next(it).split()
        # print(values)
        student = namedtuple('Student', columns)(*values)
        students.append(student)
        total_marks += int(student.MARKS)

    # print(students)
    average_marks = total_marks / n if n > 0 else 0
    print(f"{average_marks:.2f}")

if __name__ == "__main__":
    main()
