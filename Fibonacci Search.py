from math import *
from exp_speak import *

e = 2.7182818284590452353602874713527


def f(y):
    return round(eval(question.replace("x", "(" + str(y) + ")")), 8)


def fib(n):
    if n < 2:
        return 1
    i = 2
    last1 = 1
    last2 = 1
    while i <= n:
        result = last1 + last2
        last2 = last1
        last1 = result
        i += 1
    return result


gideon_speaks("Fibonacci Search program online")
question = process_eqn()
print(question)
question = question.replace("^", "**")
a = float(gideon_asks("value of a?").replace(" ", ""))
b = float(gideon_asks("value of b?").replace(" ", ""))
m = int(gideon_asks("Number of function evaluations?").replace(" ", ""))
length = b - a
k = 2

while True:
    lk = (fib(m - k + 1) / fib(m + 1)) * length
    x1 = a + lk
    x2 = b - lk
    if k == m:
        gideon_speaks("Minimum lies in (" + str(round(a, 7)) + "," + str(round(b, 7)) + ")")
        break
    fx1 = f(x1)
    fx2 = f(x2)
    if fx1 > fx2:
        a = x1
    elif fx1 < fx2:
        b = x2
    k += 1
