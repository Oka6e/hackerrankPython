import numpy as np

if __name__ == '__main__':
    N = int(input()) # Dimension of matrix
    
    A = np.array([input().split() for _ in range(N)], int)
    B = np.array([input().split() for _ in range(N)], int)

    print(np.dot(A, B))
