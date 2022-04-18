import math


def sum1(values):
    """
    calculates the sum of values(count is sum)
    :param values: list that contains numbers
    :return: the sum
    """
    count = 0
    for i in values:
        count += i
    return count


def calc_mean(values):
    """
    calculate the mean of values
    :param values:list that contains numbers
    :return: the mean
    """
    return sum1(values) / len(values)


def calc_stdv(values):
    """
    calculates the stdv of values
    :param values: given list
    :return:stdv
    """
    mean = calc_mean(values)
    temp_sum = 0
    for value in values:
        temp_sum = temp_sum + (value - mean) ** 2
    return math.sqrt(temp_sum / (len(values) - 1))


def calc_covariance(values1, values2):
    """
    returns covariance of values 1 and 2
    :param values1: given list
    :param values2: given list
    :return: the cov
    """
    temp_sum = 0
    for value1, value2 in zip(values1, values2):
        temp_sum = temp_sum + ((value1 - calc_mean(values1)) * (value2 - calc_mean(values2)))
    return temp_sum/(len(values1)-1)
