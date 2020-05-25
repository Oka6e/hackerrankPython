# -- coding: utf-8 --
import math

def find_angle_MBC(AB, BC):
    deg_sign = u"\u00b0"
    # Right Angle ABC with median M means that AM == BM == CM
    # Therefore, angMBC == ang MCB
    # invTan == opp/adj == AB/BC

    angle = int(round(math.degrees(math.atan2(AB, BC))))
    print(str(angle) + deg_sign)
    

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    find_angle_MBC(AB, BC)
