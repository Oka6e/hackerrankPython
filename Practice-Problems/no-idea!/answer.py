def are_you_happy(arr, set1, set2):
    print(sum((i in A) - (i in B) for i in arr))

if __name__ == '__main__':
    n,m = input().split() 

    arr = input().split()

    A = set(input().split())
    B = set(input().split())

    are_you_happy(arr, A, B)
