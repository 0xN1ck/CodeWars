import numpy as np


def regressionLine(x, y):
    numerator = np.sum((x - np.mean(x)) * (y - np.mean(y)))
    denominator = np.sum((x - np.mean(x)) ** 2)

    b = numerator / denominator
    a = np.mean(y) - b * np.mean(x)
    return round(a, 4), round(b, 4)


if __name__ == '__main__':
    if regressionLine([25, 30, 35, 40, 45, 50], [78, 70, 65, 58, 48, 42]) == (114.381, -1.4457):
        print("Task is solved")

    if regressionLine([56, 42, 72, 36, 63, 47, 55, 49, 38, 42, 68, 60],
                      [147, 125, 160, 118, 149, 128, 150, 145, 115, 140, 152, 155]) == (80.7777, 1.138):
        print("Task is solved")
