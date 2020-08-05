import numpy

def min_and_max(N, M):
    arr_2D = numpy.array([input().split() for _ in range(N)], int)
    
    return numpy.min(arr_2D, axis=1).max()

if __name__ == '__main__':
    N, M = map(int, input().split())

    print(min_and_max(N, M))
