from collections import namedtuple

N, Stats = int(input()), namedtuple('Stats', input().split())
marks = [Stats(*input().split()).MARKS for i in range(N)]
print("%.2f" % (sum(map(int, marks)) / N))
