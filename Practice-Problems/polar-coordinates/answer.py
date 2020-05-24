import cmath

def complex_polar_convertor(z):
    r = abs(z)
    phi = cmath.phase(z)

    print(r, phi, sep='\n')

if __name__ == '__main__':
    z = complex(input())
    complex_polar_convertor(z)
