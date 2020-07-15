from itertools import product

def S_Max(N, M):
    combos = map(lambda x: sum(i**2 for i in x)%M, product(*N))
    return max(combos)

if __name__ == '__main__':
    K, M = map(int, input().split()) # K = number of lists; M = modulo
    N = [list(map(int, input().split()))[1:] for i in range(K)]
    
    print(S_Max(N, M))
