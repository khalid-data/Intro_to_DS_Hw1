from statistics import calc_mean, calc_stdv, calc_covariance, population_statistics
import sys
from data import load_data, filter_by_feature, print_details, print_joint_details


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main(argv):
    # Question 1:
    print("Question 1:")
    features = sys.argv[2]
    features = features.split(", ")
    dictionary = load_data(sys.argv[1], features)

    ## extract summer data
    print("Summer:")
    summer_data = (filter_by_feature(dictionary, 'season', {1}))[0]
    features_for_printing = ['hum', 't1', 'cnt']
    statistic_functions = [calc_mean, calc_stdv]
    print_details(summer_data, features_for_printing, statistic_functions)
    print_joint_details(summer_data, ['t1', 'cnt'], [calc_covariance], "calc_covariance")

    ## extract holiday data
    print("Holiday:")
    holiday_data = (filter_by_feature(dictionary, 'is_holiday', {1}))[0]
    features_for_printing = ['hum', 't1', 'cnt']
    statistic_functions = [calc_mean, calc_stdv]
    print_details(holiday_data, features_for_printing, statistic_functions)
    print_joint_details(holiday_data, ['t1', 'cnt'], [calc_covariance], "calc_covariance")

    ## extract all data
    print("All:")
    features_for_printing = ['hum', 't1', 'cnt']
    statistic_functions = [calc_mean, calc_stdv]
    print_details(dictionary, features_for_printing, statistic_functions)
    print_joint_details(dictionary, ['t1', 'cnt'], [calc_covariance], "calc_covariance")

    # Question 2:
    print("Question 2:")

    # extract winter holiday and weekday  records
    winter_data = filter_by_feature(dictionary, 'season', {3})[0]
    winter_holiday_data, winter_weekday_data = filter_by_feature(winter_data, 'is_holiday', {1})

    print("If t1<=13.0, then:")
    population_statistics("Winter Holiday records:", winter_holiday_data, 't1', 'cnt', 13, False, statistic_functions)
    population_statistics("Winter Weekday records:", winter_weekday_data, 't1', 'cnt', 13, False, statistic_functions)

    print("If t1>13.0, then:")
    population_statistics("Winter Holiday records:", winter_holiday_data, 't1', 'cnt', 13, True, statistic_functions)
    population_statistics("Winter Weekday records:", winter_weekday_data, 't1', 'cnt', 13, True, statistic_functions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
