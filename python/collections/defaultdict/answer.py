from collections import defaultdict

def is_groupB_word_in_groupA(n,m):
    groupA = defaultdict(list)
    groupB = []
    
    for i in range(1, n+1):
        groupA[input()].append(i)
    
    for a in range(m):
        groupB.append(input())
    
    for x in groupB:
        if x in groupA:
            print(*groupA[x])        
        else:
            print(-1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    is_groupB_word_in_groupA(n,m)
