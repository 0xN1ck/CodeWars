import scipy.stats as stats


def t_test(sample, pop_mean, alpha):
    t = stats.ttest_1samp(a=sample, popmean=pop_mean).pvalue
    return 'Good to drink' if t > alpha else 'Reject'


if __name__ == '__main__':
    pop_mean = 4
    sample = [4.07, 3.94, 4.1, 4.15, 4.17, 4.08, 3.94, 4.04, 4.03, 3.81]
    alpha = 0.01
    print(t_test(sample, pop_mean, alpha))

    pop_mean = 5
    sample = [5.15, 4.95, 4.81, 5.43, 5.22, 5.06, 5.18, 5.27, 5.35]
    alpha = 0.05
    print(t_test(sample, pop_mean, alpha))