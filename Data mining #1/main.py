from statistics import mean
import matplotlib.pyplot as plt


class Datamining:
    def __init__(self, train_set):
        self.b = self.estimate_coef(train_set)

        # Showing regression line
        # self.plot_regression_line([i[0] for i in train_set],
        #                           [i[1] for i in train_set],
        #                           self.b)

    def predict(self, x):
        y_pred = x * self.b[1] + self.b[0]
        return y_pred

    @staticmethod
    def estimate_coef(train_set):
        n = len(train_set)

        m_x = mean([i[0] for i in train_set])
        m_y = mean([i[1] for i in train_set])

        SS_xy = sum([i[0] * i[1] for i in train_set]) - n * m_y * m_x
        SS_xx = sum([i[0] * i[0] for i in train_set]) - n * m_x * m_x

        b_1 = SS_xy / SS_xx
        b_0 = m_y - b_1 * m_x

        return b_0, b_1

    # For showing regression line
    @staticmethod
    def plot_regression_line(x, y, b):
        # plotting the actual points as scatter plot
        plt.scatter(x, y, color="m",
                    marker="o", s=30)

        # predicted response vector
        y_pred = [i * b[1] + b[0] for i in x]

        # plotting the regression line
        plt.plot(x, y_pred, color="g")

        # putting labels
        plt.xlabel('x')
        plt.ylabel('y')

        # function to show plot
        plt.show()


def main():
    example_train_set = [(0, 1),
                         (2, 2),
                         (4, 3),
                         (9, 8),
                         (3, 5)
                         ]

    dm = Datamining(example_train_set)
    predicted = [dm.predict(point[0]) for point in example_train_set]
    print(predicted)


if __name__ == "__main__":
    main()
