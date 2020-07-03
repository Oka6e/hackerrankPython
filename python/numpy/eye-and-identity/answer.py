import numpy as np

if __name__ == '__main__':
    np.set_printoptions(sign=' ')
    N, M = map(int, input().split()) # rows, column for eye function

    print(np.eye(N, M))
