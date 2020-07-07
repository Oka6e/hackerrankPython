if __name__ == '__main__':
    n = int(input()) # Number of student subscribed to the English newspaper
    eng_subs = set(map(int, input().split()))

    b = int(input()) # Number of students subscribed to the French newspaper
    french_subs = set(map(int, input().split()))

    common_subs = eng_subs & french_subs

    print(len(common_subs))
