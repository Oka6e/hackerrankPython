def get_key(x):
    if x.islower():
        return (1,x)
    elif x.isupper():
        return (2,x)
    elif x.isdigit():
        if int(x)%2 != 0:
            return (3,x)
        else:
            return (4,x)

if __name__ == '__main__':
    string = input()
    print(''.join(sorted(string, key=get_key)))
