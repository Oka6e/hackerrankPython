import numpy as np

if __name__ == '__main__':
    N, M = map(int, input().split())
    NxM = np.array([input().split() for _ in range(N)], int)

    print(np.sum(NxM, axis=0).prod())
