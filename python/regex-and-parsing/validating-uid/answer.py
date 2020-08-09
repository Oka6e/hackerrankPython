import re

def valid_UID(UID):
    patterns = [ r'(.*[A-Z].*){2,}', # Pattern for at least 2 capital letters
                r'(.*[0-9].*){3,}', # Pattern for at least 3 numbers
                r'^(?:([a-zA-Z0-9])(?!.*\1))*$', # No repeats of alphanumeric charc
                r'^[a-zA-Z0-9]{10}$'] # Pattern to check for UID of length 10
                
    regex = map(re.compile, patterns)
    
    if all(i.match(UID) for i in regex):
        return "Valid"
    else:
        return "Invalid"

if __name__ == '__main__':
    T = int(input()) # Number of test cases.
    for _ in range(T):
        print(valid_UID(input()))