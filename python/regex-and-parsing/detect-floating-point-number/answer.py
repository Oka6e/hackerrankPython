import re

def is_floating_point_number(test_case_total):
    for i in range(T):
        print(bool(re.match(r'^[-+.]?[0-9]*\.[0-9]+$', input())))

if __name__ == '__main__':
    T = int(input()) # Number of test cases.

    is_floating_point_number(T)
