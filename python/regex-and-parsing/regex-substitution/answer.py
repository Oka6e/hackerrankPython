import re

def replace_and_or(match):
    and_or = match.group()
    if and_or == '&&':
        return 'and'
    else:
        return 'or'

if __name__ == '__main__':
    N = int(input()) # number of lines input
  
    for i in range(N):
        text = input()
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', replace_and_or, text))
