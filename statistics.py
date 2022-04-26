import math
from data import fill_dict


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
    return temp_sum / (len(values1) - 1)


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    The method prints statistical indices on data representing the population and only it, using
    In methods in functions_statstic. The statistical indices are measured on the target attribute,
    after the records are collected. Suitable under the following conditions:
    If the is_above got the value True, the records in which the treatment program gets bigger vslues than threshold
    From a threshold .Otherwise, records will be collected in which the treatment  receives values smaller values
    :param feature_description: string describing a group name
    :param data: given dictionary
    :param treatment: dictionary key name
    :param target: dictionary key name
    :param threshold: threshold for treatment
    :param is_above: boolean variable
    :param statistic_functions: a list of statistic functions from statistics.py
    :return:none
    """
    print(feature_description)
    above_data = dict()
    under_data = dict()
    for key in data.keys():
        above_data[key] = list()
        under_data[key] = list()

    for row, value in enumerate(data[treatment]):
        if is_above and value > threshold:
            fill_dict(data, above_data, row)

        elif not is_above and value <= threshold:
            fill_dict(data, under_data, row)

    if is_above:
        num_mean = (statistic_functions[0](above_data[target]))
        num_stdv = (statistic_functions[1](above_data[target]))
        print("cnt" + ": " + str("%.2f" % round(num_mean, 2)) + ", " + str("%.2f" % round(num_stdv, 2)))

    else:
        num_mean = (statistic_functions[0](under_data[target]))
        num_stdv = (statistic_functions[1](under_data[target]))
        print("cnt" + ": " + str(r"%.2f" % round(num_mean, 2)) + ", " + str("%.2f" % round(num_stdv, 2)))

