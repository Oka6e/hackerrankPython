from collections import deque

def dequeue_cmd(N):
    d = deque()
    for i in range(N):
        cmd, *arg = input().split()
        getattr(d, cmd)(*arg)
    print(*d)

if __name__ == '__main__':
    N = int(input()) # number of operations
    dequeue_cmd(N)
