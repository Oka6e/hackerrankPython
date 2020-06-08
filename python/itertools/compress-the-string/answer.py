from itertools import groupby

def string_compression(S):

    for k, c in groupby(S):
        print((len(list(c)), int(k)), end=' ')

if __name__ == '__main__':
    S = str(input())

    string_compression(S)
