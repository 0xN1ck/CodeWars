from statistics import mean
import matplotlib.pyplot as plt
import numpy as np


class Datamining:
    def __init__(self, train_set):
        W = [np.random.random() for _ in range(5 + 1)]  # +1 is for W_0
        x_tr = np.array([i[0] for i in train_set])
        y_tr = np.array([i[1] for i in train_set])
        print(W)
        print(x_tr, y_tr)
        W = self.update_weights(3, x_tr, y_tr)
        self.g = self.predict(W, x_tr)

        # Showing regression line
        self.plot_regression_line([i[0] for i in train_set],
                                  [i[1] for i in train_set],
                                  self.g)

    def update_weights(self, degree, x, y):
        A = np.linalg.inv(np.array(
            [[sum(np.power(x, i)) for i in range(j, degree + 1 + j)] for j in range(degree + 1)]
        ))

        return np.dot(A, np.array([sum(y * np.power(x, i)) for i in range(degree + 1)]))

    def predict(self, W, x):
        return sum([W[i] * x ** i for i in range(len(W))])

    # def predict(self, x):
    #     y_pred = x * self.b[1] + self.b[0]
    #     return y_pred

    # For showing regression line
    @staticmethod
    def plot_regression_line(x, y, g):
        # plotting the actual points as scatter plot
        plt.scatter(x, y, color="m",
                    marker="o", s=30)

        # predicted response vector
        #y_pred = [i * b[1] + b[0] for i in x]

        # plotting the regression line
        plt.plot(x, g, color="g")

        # putting labels
        plt.xlabel('x')
        plt.ylabel('y')

        # function to show plot
        plt.show()


def main():
    example_train_set = [(1, 4), (4, 4), (2, 2), (3, 2), (5, 2)]

    dm = Datamining(example_train_set)
    # predicted = [dm.predict(point[0]) for point in example_train_set]
    # print(predicted)


if __name__ == "__main__":
    main()
