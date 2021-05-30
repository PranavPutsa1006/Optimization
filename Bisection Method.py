from math import *
from exp_speak import *

e = 2.7182818284590452353602874713527


def f(y):
    return round(eval(question.replace("x", "(" + str(y) + ")")), 8)


def f1(a):
    if a > 0.01 or a < -0.01:
        delta_a = 0.01 * abs(a)
    else:
        delta_a = 0.0001
    return (f(a + delta_a) - f(a - delta_a)) / (2 * delta_a)


gideon_speaks("Bisection method program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
a = float(gideon_asks("value of a?").replace(" ", ""))
b = float(gideon_asks("value of b?").replace(" ", ""))
eps = float(gideon_asks("Epsilon value?").replace(" ", ""))
x1 = a
x2 = b
k = 1

while f1(a) < 0 < f1(b):
    z = (x1 + x2) / 2
    if abs(f1(z)) < eps:
        gideon_speaks("Minimum lies at x = " + str(round(z, 7)))
        break
    elif f1(z) < 0:
        x1 = z
    elif f1(z) > 0:
        x2 = z
    k += 1
