import numpy as np

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = np.array([input().split() for i in range(N)], int)
    B = np.array([input().split() for i in range(N)], int)
    
    print(np.add(A, B), np.subtract(A, B), np.multiply(A, B), np.floor_divide(A, B), \
        np.mod(A, B), np.power(A, B), sep='\n')
