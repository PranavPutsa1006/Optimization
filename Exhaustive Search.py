from math import *
from exp_speak import *

e = 2.7182818284590452353602874713527


def f(y):
    return round(eval(question.replace("x", "(" + str(y) + ")")), 8)


gideon_speaks("Exhaustive Search program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
a = float(gideon_asks("value of a?").replace(" ", ""))
b = float(gideon_asks("value of b?").replace(" ", ""))
n = float(gideon_asks("value of n?").replace(" ", ""))
delta_x = round((b - a) / n, 5)
x1 = a
x2 = x1 + delta_x
x3 = x1 + 2 * delta_x

fx1 = f(x1)
fx2 = f(x2)
while x3 <= b:
    fx3 = f(x3)
    if fx1 >= fx2 and fx2 <= fx3:
        gideon_speaks("Minimum lies in (" + str(round(x1, 7)) + "," + str(round(x3, 7)) + ")")
        break
    else:
        x1 += delta_x
        x2 += delta_x
        x3 += delta_x
        fx1 = fx2
        fx2 = fx3
