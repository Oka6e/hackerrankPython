import numpy

if __name__ == '__main__':
    N, M = map(int, input().split()) # rows and columns
    arr = numpy.array([input().split() for i in range(N)], int)
    print(arr.transpose(), arr.flatten(), sep='\n')
