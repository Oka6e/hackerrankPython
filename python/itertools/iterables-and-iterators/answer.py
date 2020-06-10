from itertools import combinations

if __name__ == '__main__':
    N = int(input()) # length of list
    lst = input().split()
    K = int(input()) # number of indices to be selected

    comb = list(combinations(lst, K))
    count = 0
    length = len(comb)

    for i in comb:
        if 'a' in i:
            count += 1
    
    print(count/length)
