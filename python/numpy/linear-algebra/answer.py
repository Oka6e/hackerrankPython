import numpy as np

if __name__ == '__main__':
    N = int(input())
    A = np.array([input().split() for _ in range(N)], float)
    print(round(np.linalg.det(A), 2))
