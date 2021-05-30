from math import *
from exp_speak import *

e = 2.7182818284590452353602874713527


def f(y):
    return round(eval(question.replace("x", "(" + str(y * (b - a) + a) + ")")), 8)


gideon_speaks("Golden section Search program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
a = float(gideon_asks("value of a?").replace(" ", ""))
b = float(gideon_asks("value of b?").replace(" ", ""))
eps = float(gideon_asks("value of termination parameter?").replace(" ", ""))
aw = 0
bw = 1
lw = 1
k = 1

while True:
    w1 = aw + 0.618 * lw
    w2 = bw - 0.618 * lw
    lw = bw - aw
    if abs(lw) < eps:
        gideon_speaks("Minimum lies in (" + str(round(aw * (b - a) + a, 7)) + "," + str(round(bw * (b - a) + a, 7)) + ")")
        break
    fw1 = f(w1)
    fw2 = f(w2)
    if fw1 > fw2:
        bw = w1
    elif fw1 < fw2:
        aw = w2
    k += 1
