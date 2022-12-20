import cmath

a = float(input('Введите точку a '))
b = float(input('Введите точку b '))

def function(x):
    return x**3 + 3 * x**2 + 12*x + 8
def func(x):
    return 3*x**2 + 6*x + 12

x0, x1, out, y, e, k = a, b, 0, 1, 1e-4, 0
while abs(y - out) >= e:
    out = x1 - ((x1 - x0) / (function(x1) - function(x0))) * function(x1)
    x0 = x1
    x1 = out
    k += 1
    y = out

print("Кол-во итераций", k)
print("Метод секущих", out)

x0, x1, out, y, e, k = a, b, 0, 1, 10e-8, 0

while abs(y - out) >= e:
    out = x1 - (function(x1)/func(x1))
    x1 = out
    k += 1
    y = out

print("Кол-во итераций", k)
print("Метод Ньютона", out)

x0, x1, out, y, e, k = a, b, 0, 0, 10e-8, 0

while x1 - x0 >= e:
    if function(y) * function(x0) < 0:
        x1 = y
    else:
        x0 = y
    y = (x1 + x0) / 2
    k += 1

print("Кол-во итераций", k)
print("Метод Дихотомии", y)