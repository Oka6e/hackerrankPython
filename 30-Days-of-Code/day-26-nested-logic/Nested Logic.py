def fee_calculator(ad,am,ay,ed,em,ey):
    if (ay,am,ad)<=(ey,em,ed):
        return 0
    elif (ay,am) == (ey,em):
        return 15 * (ad - ed)
    elif ay == ey:
        return 500 * (am - em)
    else:
        return 10000

if __name__ == '__main__':
    ad, am, ay = [int(i) for i in input().split(' ')]
    ed, em, ey = [int(j) for j in input().split(' ')]
    print(fee_calculator(ad,am,ay,ed,em,ey))
