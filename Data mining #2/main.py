"""
    This code of Algorith of "Polymonial regression" is realized without libraries:
    sklearn, pandas, tensorflow, numpy, scipy.
    Libraries numpy and matplotlib is needed for showing work of the algorithm and generation big dataset.
    Such a solution was selected for increasing performance and velocity of demonstration of the algorithm.

    The presence of all logic program in the __init__() function is due to the solution of the task on the CodeWars
    platform.
"""

# Libraries are for visualization and generation dataset with line regression.
# from matplotlib import pyplot as plt
# import numpy

import copy


class Datamining:
    def __init__(self, train_set: [()], d=5, lbda=0.5):
        self.w = None
        self.d = d
        self.lbda = lbda
        self.X = [i[0] for i in train_set]
        self.y = [i[1] for i in train_set]

        self.fit(self.X, self.y)

        # This line code shows points of dataset
        # plt.scatter(self.X, self.y)

        pred_arr = []
        [pred_arr.append(self.predict(x)) for x in self.X]

        # This example code is for showing regression line
        # plt.plot(self.X, pred_arr, c="red")
        # plt.show()

    def fit(self, X: [], y: []) -> [[]]:
        A = []
        C = []
        for i in range(self.d):
            A_row = []
            for j in range(self.d):
                lbda = 0 if i != j else self.lbda
                A_row.append(sum([x ** (i + j) +
                                  lbda for x in X]))
            A.append(A_row)
            C.append(sum([a * b for a, b in zip([x ** i for x in X], y)]))

        w = self.mul2x1(invert(A), C)
        self.w = w

    def predict(self, X: float) -> float:
        pred = sum_for_pred([[w_j_ * X ** j for w_j_ in w_j] for j, w_j in enumerate(self.w)])
        return pred

    @staticmethod
    def mul2x1(A: [[]], C: []) -> [[]]:
        arr2 = []
        for i in A:
            k_ = copy.copy(C)
            arr1 = []
            for j in range(len(i)):
                arr1.append(i[j] * k_.pop(0))
            arr2.append(arr1)
        return arr2


def invert(A) -> [[]]:
    ''' Returns the inverse of A, where  A is a square matrix in the form of a nested list of lists. '''
    A = [A[i] + [int(i == j) for j in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        A[i:] = sorted(A[i:], key=lambda r: -abs(r[i]))
        A[i] = [A[i][j] / A[i][i] for j in range(len(A) * 2)]
        A = [[A[j][k] if i == j else A[j][k] - A[i][k] * A[j][i] for k in range(len(A) * 2)] for j in range(len(A))]
    return [A[i][-len(A):] for i in range(len(A))]


def sum_for_pred(collection: [[]]) -> float:
    res = (sum([i for i in [sum(q) for q in collection]]))
    return res


if __name__ == '__main__':
    # For generation big dataset.
    # You will need refactoring dataset for Datamining
    # This commented code is example for generation big dataset

    # numpy.random.seed(0)
    # X = numpy.arange(0, 10, 0.1).tolist()
    # X = (X + numpy.random.normal(0, 0.2, len(X))).tolist()
    # y = numpy.sin(X)
    # y = (y + numpy.random.normal(0, 0.3, len(y))).tolist()
    # plt.scatter(X, y)
    # dataset = [(x, y) for x, y in zip(X, y)]
    # model = Datamining(dataset, d=12)

    model = Datamining([(1, 4), (4, 4), (2, 2), (3, 2), (5, 2)], d=12)
