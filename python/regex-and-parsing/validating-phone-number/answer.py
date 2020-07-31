import re

def valid_phone_num(N):
    pat = re.compile(r'^[789]\d{9}$')
    
    for i in range(N):  
        phone_num = input()
        m = pat.match(phone_num)
        if m:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    N = int(input()) # Number of inputs
    
    valid_phone_num(N)
