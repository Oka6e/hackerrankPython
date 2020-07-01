import numpy as np

if __name__ == "__main__":
    dim = tuple(map(int,input().split())) # dimension of array
    print(np.zeros(dim, dtype = np.int))
    print(np.ones(dim, dtype = np.int))
