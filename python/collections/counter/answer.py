from collections import Counter

def total_revenue(shoes, N):
    revenue = 0

    for i in range(N):
        size, price = map(int, input().split())
        if shoes[size]:
            revenue += price
            shoes[size] -= 1

    return revenue

if __name__ == '__main__':
    X = int(input()) # amount of shoes at Raghu's store
    shoes = Counter(map(int, input().split())) # available shoe sizes 
    N = int(input()) # number of customers

    print(total_revenue(shoes, N))
