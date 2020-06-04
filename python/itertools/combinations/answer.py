from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()

    for i in range(1, int(k) + 1):
        comb = list(combinations(sorted(S), i))
        for j in comb:
            print(''.join(j))
