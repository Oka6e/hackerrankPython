import re

def check_valid_regex(regex_expression):
    try: 
        re.compile(regex_expression)
    except re.error:
        return False
    else:
        return True

if __name__ == '__main__':
    T = int(input()) # number of test cases

    for i in range(T):
        S = input() # individual test case
        print(check_valid_regex(S))
