import numpy as np

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr_2D = [list(map(int, input().split())) for _ in range(N)]
    np.set_printoptions(legacy='1.13')
    print(np.mean(arr_2D, axis=1), np.var(arr_2D, axis=0), np.std(arr_2D), sep='\n')
