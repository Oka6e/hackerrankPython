def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        t = string[i:i + k]
        t = list(dict.fromkeys(t)) 
        print(''.join(t))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
