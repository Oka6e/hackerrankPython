import re

def find_repeat_alphanum(S):
    pattern = r'([a-zA-Z\d])\1+' # raw string of alphanumeric for group 1 with repeat
    m = re.search(pattern, S)
    print(m.group(1) if m else -1)

if __name__ == '__main__':
    S = input()
    find_repeat_alphanum(S)
