def minion_game(string):
    stuart = 0
    kevin = 0
    l = len(string)

    for i in range(l):
        if s[i] in "AEOIU":
            kevin += l - i
        else:
            stuart += l - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
