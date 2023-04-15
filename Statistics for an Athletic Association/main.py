from datetime import datetime, timedelta
import numpy as np
import pandas as pd


def get_range(np_array: np.ndarray) -> str:
    """
    This function returns range
    :param np_array: np.ndarray
    :return: range_: str
    """
    td = pd.to_timedelta(pd.Series([np_array[-1] - np_array[0]])).mean()
    range_ = redact(td.seconds)
    return range_


def get_mean(np_array: np.ndarray) -> str:

    """
    This function returns average
    :param np_array: np.ndarray
    :return: avg: str
    """
    td = pd.to_timedelta(pd.Series(np.array([(x - np.datetime64('1900', 's')) for x in np_array]).mean())).mean()
    avg = redact(td.seconds)
    return avg


def get_median(np_array: np.ndarray) -> str:
    """
    This function returns median
    :param np_array: np.ndarray
    :return: median: str
    """
    td = pd.to_timedelta(pd.Series(np.array([(x - np.datetime64('1900', 's')) for x in np_array]))).median()
    median = redact(td.seconds)
    return median


def redact(seconds: int) -> str:
    """
    This function edits the data for the required results.
    It translates seconds to timedelta format (%H%M%S).
    :param seconds: int
    :return: result: str
    """
    result = str(timedelta(seconds=seconds)).replace(":", "|").strip()
    return '0' + result if len(result.split('|')[0]) < 2 else result


def stat(strg: str):
    """
    The main function of program
    :param strg:
    :return: result
    """
    if len(strg) < 1:
        return ''
    # This line formats input string into need format - adds 00 in empty spaces
    data = [':'.join([y+'00' if len(y.strip()) < 1 else y for y in x.strip().split('|')]) for x in strg.split(',')]

    # This line sorts input data and translates data into datetime format
    np_array = np.sort(
        np.array([np.datetime64(datetime.strptime(x, '%H:%M:%S'), 's') for x in data]))

    # We get need data for the result
    range_ = get_range(np_array=np_array)
    avg = get_mean(np_array=np_array)
    median = get_median(np_array=np_array)

    result = f'Range: {range_} Average: {avg} Median: {median}'
    return result
