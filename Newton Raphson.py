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


def f11(a):
    if a > 0.01 or a < -0.01:
        delta_a = 0.01 * abs(a)
    else:
        delta_a = 0.0001
    return (f(a + delta_a) - 2 * f(a) + f(a - delta_a)) / (delta_a ** 2.0)


gideon_speaks("Exhaustive Search program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
x0 = float(gideon_asks("value of x0?").replace(" ", ""))
eps = float(gideon_asks("Epsilon value?").replace(" ", ""))
k = 1

while True:
    x1 = x0 - f1(x0) / f11(x0)
    if abs(f1(x1)) < eps:
        gideon_speaks("Minimum lies at " + str(round(x1, 7)))
        break
    else:
        k += 1
        x0 = x1