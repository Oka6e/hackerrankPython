import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * (size-1) +1
    lst = []
    for i in range(size-1,-1,-1):
        a = '-'.join(alpha[i:size])
        lst.append((a[::-1] +a[1:]).center(width, '-'))
    print('\n'.join(lst[:-1] + lst[::-1]))
    
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
