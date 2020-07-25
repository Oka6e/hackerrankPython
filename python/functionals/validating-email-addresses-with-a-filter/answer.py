import re

def fun(s):
    pattern = r'^[\w_-]+@[\da-zA-Z]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, s)
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
