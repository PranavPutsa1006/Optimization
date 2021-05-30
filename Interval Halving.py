from math import *
from exp_speak import *

e = 2.7182818284590452353602874713527


def f(y):
    return round(eval(question.replace("x", "(" + str(y) + ")")), 8)


gideon_speaks("Interval Halving program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
a = float(gideon_asks("value of a?").replace(" ", ""))
b = float(gideon_asks("value of b?").replace(" ", ""))
eps = float(gideon_asks("Termination parameter value?").replace(" ", ""))
length = b - a

while True:
    x1 = a + length / 4
    x2 = b - length / 4
    xm = (x1 + x2) / 2
    if abs(length) < eps:
        gideon_speaks("Minimum lies in (" + str(round(a, 7)) + "," + str(round(b, 7)) + ")")
        break
    fx1 = f(x1)
    fx2 = f(x2)
    fxm = f(xm)
    if fx1 < fxm:
        b = xm
        xm = x1
    elif fx2 < fxm:
        a = xm
        xm = x2
    else:
        a = x1
        b = x2
    length = b - a
