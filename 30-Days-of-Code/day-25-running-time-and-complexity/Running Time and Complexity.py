import math

def check_prime(n):
    if n <= 1:
        return "Not prime"
    sq = int(math.sqrt(n))
    if n != 2 and n % 2 == 0:
        return "Not prime"
    for j in range(3, sq+1, 2):
        if n % j == 0:
            return "Not prime"
    return "Prime"

T = int(input())
for i in range(T):
    n = int(input())
    print(check_prime(n))
