regex_pattern = r"^M{0,3}(CM){0,3}D{0,1}(CD){0,3}C{0,3}(XC){0,3}L{0,1}(XL){0,3}X{0,3}(IX){0,3}V{0,1}(IV){0,3}I{0,3}$"
import re
print(str(bool(re.match(regex_pattern, input()))))
