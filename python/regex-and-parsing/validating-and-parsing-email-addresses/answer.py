import email.utils
import re

def valid_email(user_email):
    user, u_email = email.utils.parseaddr(user_email)
    pattern = re.compile(r'^[a-zA-Z]+[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
    m = re.match(pattern, u_email)
    if bool(m):
        print(email.utils.formataddr((user, u_email)))

if __name__ == "__main__":
    n = int(input()) # Number of email addresses

    for _ in range(n):
        user_email = input()
        valid_email(user_email)
