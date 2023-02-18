print('ax^2 + bx + c = 0')
a = float(input('введите первый коэфициент'))
b = float(input('введите второй коэфициент'))
c = float(input('введите третий коэфициент'))
print('a =', a)
print('b =', b)
print('c =', c)
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + ((D) ** 0.5))/(2 * a)
    x2 = (-b - ((D) ** 0.5))/(2 * a)
    print(x1, x2)
elif D == 0:
    X1 = (-b) / (2 * a)
    print(X1)
else:
    print('корней нет')


