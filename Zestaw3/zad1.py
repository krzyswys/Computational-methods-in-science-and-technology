import math
import numpy as np


def f1(x):
    if x < 3 * math.pi / 2 or x > 2 * math.pi:
        return 0
    return math.cos(x) * math.cosh(x) - 1


def f2(x):
    if x <= 0 or x > math.pi / 2:
        return 0
    return 1 / x - math.tan(x)


def f3(x):
    if x < 1 or x > 3:
        return 0
    return 2 ** (-x) + (math.e) ** (x) + 2 * math.cos(x) - 6


def f4(x):
    return (x + 1) ** 2 - 1


def bisec(prec, dom, e, f):
    a, b = dom
    x = prec((a + b) / 2)
    i = 0
    if f(x) == 0:
        return x
    while abs(b - a) > e:
        if f(a) * f(x) < 0:
            b = x
        elif f(x) * f(b) < 0:
            a = x
        x = prec(((b - a) / 2) + a)
        i += 1
        if f(x) == 0:
            break
    return x, i


e1 = 10 ** (-7)
e2 = 10 ** (-15)
e3 = 10 ** (-33)
prec = np.float64
f_1 = ((3 * math.pi / 2, 2 * math.pi), f1)
f_2 = ((0.0, math.pi / 2), f2)
f_3 = ((1.0, 3.0), f3)
e = [e1, e2, e3]
f = [f_1, f_2, f_3]
for j, fun in enumerate(f):
    # for epsilon in e:
    x, i = bisec(prec, fun[0], e1, fun[1])
    print(
        "Obliczone f",
        j + 1,
        "(x)=0, dla x=",
        x,
        "przy precyzji: ",
        prec,
        " oraz epsilon rownym: ",
        e1,
        "ilosc potrzebnych iteracji do obliczenia: ",
        i,
    )


def newton(prec, dom, e, f):
    a, b = dom
