import numpy

if __name__ == '__main__':
    N, M, P = map(int, input().split())
    arr_1 = numpy.array([input().split() for i in range(N)], int)
    arr_2 = numpy.array([input().split() for j in range(M)], int)
    print(numpy.concatenate((arr_1, arr_2), axis=0))
