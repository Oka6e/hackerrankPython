def swap_case(s):
    s_swap = ""
    s_list = []
    for n in s:
        if n.isupper():
            s_list.append(n.lower())
        else:
            s_list.append(n.upper())    
    return s_swap.join(s_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
