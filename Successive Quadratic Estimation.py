from math import *
import operator
from exp_speak import *

e = 2.7182818284590452353602874713527


def f(y):
    return round(eval(question.replace("x", "(" + str(y) + ")")), 8)


gideon_speaks("Successive quadratic estimation program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
x1 = float(gideon_asks("value of x1?").replace(" ", ""))
delta = float(gideon_asks("Step size?").replace(" ", ""))
x2 = x1 + delta
k = 1

if f(x1) >= f(x2):
    x3 = x1 + 2 * delta
else:
    x3 = x1 - delta

while True:
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    Fmin = min(f1, f2, f3)
    if Fmin == f1:
        Xmin = x1
    elif Fmin == f2:
        Xmin = x2
    else:
        Xmin = x3
    a1 = (f2 - f1) / (x2 - x1)
    a2 = ((f3 - f1) / (x3 - x1) - a1) / (x3 - x2)
    x_bar = (x1 + x2) / 2 - a1 / (2 * a2)
    fx_bar = f(x_bar)
    x_dict = {f1: x1, f2: x2, f3: x3, fx_bar: x_bar}
    x_dict = dict(sorted(x_dict.items(), key=operator.itemgetter(0)))
    if abs(Fmin - fx_bar) < 0.001 or abs(Xmin - x_bar) < 0.001:  # "or k >= 2:" stops after 2 iterations
        gideon_speaks("Minimum lies at " + str(round(x_dict[list(x_dict.keys())[0]], 7)))
        break
    x_dict.pop(list(x_dict.keys())[3])
    x_dict = dict(sorted(x_dict.items(), key=operator.itemgetter(1)))
    [x1, x2, x3] = list(x_dict.values())
    k += 1
