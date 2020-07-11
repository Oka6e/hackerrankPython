if __name__ == '__main__':
    n_A = int(input()) # Number of elements in set A
    A = set(map(int, input().split()))

    N = int(input()) # Number of other sets
    for i in range(N):
        operation, len_other_set = input().split()
        new_set = set(map(int, input().split()))
        
        getattr(A, operation)(new_set)

    print(sum(A))
