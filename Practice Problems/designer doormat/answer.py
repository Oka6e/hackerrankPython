def createAMat(N,M):
    if N%2 == 0:
        return
    # prints top half of doormat
    for i in range(1, N, 2):
      print(('.|.'*i).center(M,'-'))
    
    # prints center of doormat
    print("WELCOME".center(M,'-'))

    # prints bottome half of doormat
    for i in range(N-2, 0, -2):
        print(('.|.'*i).center(M,'-'))

if __name__ == '__main__':
    N,M = map(int(), input().split())
    createAMat(N,M)
    
# Pythonic Code (not submitted)
# pattern = [('.|.'*i).center(M,'-') for i in range(1,N,2)]
# center = ["WELCOME".center(M,'-')]
# print('\n'.join(pattern + center + pattern[::-1])
