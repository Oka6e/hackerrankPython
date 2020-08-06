n = int(input())

phone_book = {}
for i in range(n):
    entry = input().split()
    phone_book[entry[0]] = entry[1]

while True:
    try:
        name = input()
        if name in phone_book:
            print(name + "=" + phone_book[name])
        else:
            print("Not found")
    except: 
        break