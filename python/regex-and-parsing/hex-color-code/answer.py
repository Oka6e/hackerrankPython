import re

def valid_colors(N):
    pat = re.compile(r'(?<!^)(#(?:[\da-fA-F]{3}){1,2})')
    
    for _ in range(N):
        CSS_Code = input()
        m = re.findall(pat, CSS_Code)
        if m:
            print(*m, sep='\n')

if __name__ == '__main__':
    N = int(input()) # Number of lines 
    valid_colors(N)
