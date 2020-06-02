from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    
    perm = list(permutations(sorted(S), int(k)))

    for i in perm:
        print(''.join(i))
