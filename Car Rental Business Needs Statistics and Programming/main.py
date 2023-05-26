import math


def prob_simpson(lamb, x, op='='):
    p = 0
    match op:
        case '=':
            p = (lamb ** x * math.e ** (-lamb)) / (math.factorial(x))
            return p
        case '<':
            for _ in range(x+1):
                p += (lamb ** _ * math.e ** (-lamb)) / (math.factorial(_))
            return 1 - p
        case '>':
            for _ in range(x):
                p += (lamb ** _ * math.e ** (-lamb)) / (math.factorial(_))
            return p
        case '>=':
            for _ in range(x + 1):
                p += (lamb ** _ * math.e ** (-lamb)) / (math.factorial(_))
            return p
        case '<=':
            for _ in range(x):
                p += (lamb ** _ * math.e ** (-lamb)) / (math.factorial(_))
            return 1 - p


if __name__ == '__main__':
    if prob_simpson(8, 12) == 0.04812680428195667:
        print("1 Task is solved")
    if prob_simpson(8, 11) == 0.072190206422935:
        print("2 Task is solved")
    if prob_simpson(8, 10) == 0.09926153383153563:
        print("3 Task is solved")
    if prob_simpson(8, 12, '>') == 0.8880759989814817:
        print("4 Task is solved")
    if prob_simpson(8, 12, '>=') == 0.9362028032634384:
        print("5 Task is solved")
    if prob_simpson(8, 12, '<') == 0.06379719673656159:
        print("6 Task is solved")
    if prob_simpson(8, 12, '<=') == 0.1119240010185183:
        print("7 Task is solved")
