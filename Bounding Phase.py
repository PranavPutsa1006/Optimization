from math import *
from exp_speak import *

e = 2.7182818284590452353602874713527


def f(y):
    return round(eval(question.replace("x", "(" + str(y) + ")")), 8)


gideon_speaks("Bounding Phase program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
k = 0
x0 = float(gideon_asks("value of x0?").replace(" ", ""))
delta = float(gideon_asks("Increment value?").replace(" ", ""))
x_0 = x0
x1 = x0 - delta
x2 = x0 + delta

fx0 = f(x0)
fx1 = f(x1)
fx2 = f(x2)
search_dir = ''
fxk1 = fx0
if fx1 >= fx0 >= fx2:
    search_dir = 'right'
    fxk1 = fx2
elif fx1 <= fx0 <= fx2:
    search_dir = 'left'
    delta *= -1
    fxk1 = fx1
elif fx1 >= fx0 <= fx2:
    search_dir = 'stop'
    gideon_speaks("Minimum lies in (" + str(round(x1, 5)) + "," + str(round(x2, 5)) + ")")

fxk = fx0
while search_dir != 'stop':
    x1 = x0 + pow(2, k) * delta
    fxk1 = f(x1)
    if fxk1 < fxk:
        fxk = fxk1
        x0 = x1
        k += 1
    else:
        k -= 1
        x2 = x_0
        for i in range(0, k):
            x2 += (2 ** i) * delta
        gideon_speaks("Minimum lies in (" + str(round(min(x_0 + (2 ** (k - 1)) * delta, x1), 7)) + "," + str(
            round(max(x2, x1), 7)) + ")")
        break
