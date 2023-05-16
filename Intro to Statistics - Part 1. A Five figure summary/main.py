import statistics


class StatisticalSummary(object):
    def __init__(self, seq):
        self.seq = seq
        self.seq = sorted([i for i in self.seq if type(i) is not str])

    def five_figure_summary(self, precision=None):
        N = len(self.seq)

        extreme_lower = self.seq[0]

        extreme_upper = self.seq[-1]

        lower_quartile, median, upper_quartile = statistics.quantiles(self.seq, method='inclusive')

        if precision is None:
            return N, extreme_lower, extreme_upper, lower_quartile, median, upper_quartile
        else:
            return tuple([round(i, precision) for i in [N, extreme_lower, extreme_upper, lower_quartile, median,
                                                        upper_quartile]])


if __name__ == "__main__":
    data = [i for i in range(0, 7)]
    if StatisticalSummary(data).five_figure_summary(2) == (7, 0, 6, 1.5, 3, 4.5):
        print("It is solved")
