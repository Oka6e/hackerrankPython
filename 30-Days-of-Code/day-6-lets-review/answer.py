def even_odd_str(S):
    even_str = ""
    odd_str = ""
    for N in range(len(S)):
        if N%2 == 0:
            even_str += S[N]
        if N%2 != 0:
            odd_str += S[N]
    print(even_str + " " + odd_str)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        S = str(input())
        even_odd_str(S)