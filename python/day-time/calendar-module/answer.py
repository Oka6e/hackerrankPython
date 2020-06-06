import calendar 

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    
    n = calendar.weekday(year, month, day)
    print(calendar.day_name[n].upper())
