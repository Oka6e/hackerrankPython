from itertools import product

def compute_cartesian_prod(*iterable):
    cartesian_prod = list(product(*iterable))
    return cartesian_prod

if __name__ == '__main__':
    A = map(int, input().split())
    B = map(int, input().split())

    print(*compute_cartesian_prod(A, B))
