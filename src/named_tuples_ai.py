from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
print("%.2f" % (sum(int(Student._make(input().split()).MARKS) for _ in range(n)) / n))
