import numpy as np

if __name__ == '__main__':
    P_coeff = np.array(input().split(), float) # Coefficients of polynomial P
    x = float(input()) # Point x

    print(np.polyval(P_coeff, x))
