if __name__ == '__main__':
    n = int(input()) # Number of English Subscribers
    eng_subs = set(map(int, input().split()))

    m = int(input()) # Number of French Subscribers
    french_subs = set(map(int, input().split()))

    print(len(eng_subs^french_subs))
