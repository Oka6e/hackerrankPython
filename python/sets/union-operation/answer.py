if __name__ == '__main__':
    n = int(input()) # number of student subscribed to English newspaper
    eng_subscriptions = set(map(int, input().split()))
    
    b = int(input()) # number of student subscribed to English newspaper
    french_subscriptions = set(map(int, input().split()))

    distinct_subscriptions = eng_subscriptions | french_subscriptions
    print(len(distinct_subscriptions))
