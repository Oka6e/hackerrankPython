def isStrictSuperset(setA, n):
    
    return all(setA > set(map(int, input().split())) for i in range(n))
            

if __name__ == '__main__':
    setA = set(map(int, input().split()))
    n = int(input()) # Number of other sets
    
    print(isStrictSuperset(setA, n))
