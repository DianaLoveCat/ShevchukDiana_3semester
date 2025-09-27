import math
import sys

def read_coef(ind, symb):
    result = []
    try:
        str_coef = sys.argv[ind]
    except:
        print("Введите коэффициент", symb)
        str_coef = input()
    return float(str_coef)

def get_root(a, b, c):
    result = []
    D = b*b-4*a*c
    if D == 0.0:
        result.append(-b / (2.0 * a))
    elif D > 0.0:
        sdD = math.sqrt(D)
        result.append((-b + sdD) / (2.0 * a))
        result.append((-b - sdD) / (2.0 * a))
    return result


if __name__ == '__main__':
    a = read_coef(1, 'A')
    b = read_coef(2, 'B')
    c = read_coef(3, 'C')

    print("Исходное уравнение: ",a,'x*x + ', b, 'x + ', c, ' = 0', sep= '')
    print("Итог: ", end = '')

    roots = get_root(a, b, c)
    n = len(roots)
    if n == 0:
        print("Нет корней")
    elif n == 1:
        print("Один корень: {}".format(roots[0]))
    elif n == 2:
        print("Два корня: {} и {}".format(roots[0], roots[1]))