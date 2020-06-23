import numpy as np

def convert_to_3x3(arr):
    return np.reshape(arr,(3,3))

if __name__ == '__main__':
    arr = np.array(input().split(), int)
    print(convert_to_3x3(arr))
