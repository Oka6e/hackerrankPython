from collections import deque

def pile_cubes(T):
    for i in range(T):
        n = int(input()) # Number of cubes
        side_lengths = deque(map(int, input().split()))
        for j in range(n//2):
            if side_lengths[0]<side_lengths[1] and side_lengths[-1]<side_lengths[-2]:
                print("No")
                break
            side_lengths.pop()
            side_lengths.popleft()
            if len(side_lengths) == 0  or len(side_lengths) == 1:
                print("Yes")

if __name__ == '__main__':
    T = int(input()) # Number of test cases

    pile_cubes(T)
