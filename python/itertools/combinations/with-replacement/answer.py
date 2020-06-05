from itertools import combinations_with_replacement as cwr

if __name__ == '__main__':
    S, k = input().split()

    for i in cwr(sorted(S), int(k)):
        print(''.join(i))
