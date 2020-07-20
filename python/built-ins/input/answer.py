def check_eq(var, answer, func):
    if eval(func) == answer:
        return True
    return False

if __name__ == '__main__':
    x, k = map(int, input().split())
    P = input()

    print(check_eq(x, k, P))
