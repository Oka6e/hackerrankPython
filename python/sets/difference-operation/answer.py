if __name__ == '__main__':
    tot_eng_subs = int(input())
    eng_subs = set(map(int,input().split()))

    tot_french_subs = int(input())
    french_subs = set(map(int,input().split()))

    just_eng = eng_subs - french_subs
    print(len(just_eng))
