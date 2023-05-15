"""
The higher the degree, the more accurate the result.
"""


import scipy.stats as stats
import pandas as pd
import numpy as np


def clean_mean(sample: list, cutoff: int):
    df = pd.DataFrame(sample)
    degree = 3
    for i in range(degree):
        df = df[(np.abs(stats.zscore(df[0])) < cutoff)]

    return df.mean().round(2).values[0]


if __name__ == '__main__':
    sample = [1.01, 0.99, 1.02, 1.01, 0.99, 0.97, 1.03, 0.99, 1.02, 0.99, 3, 10]
    cutoff = 3
    clean_mean(sample, cutoff)