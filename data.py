import pandas


def load_data(path, features):
    """
      loads data into dictionary from csv file only with wanted featrues
      :param path: path of file
      :param features: features we want to keep in the dictionary
      :return: the dictionary
      """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    new_dict = dict()
    for key, value in data.items():
        for i in features:
            if i == key:
                new_dict[key] = value
    return new_dict


def filter_by_feature(data, feature, values):
    """
       the function returns two dict filtered by feature and value
       :param data: a dictionary, its keys are features from the csv file
       :param feature: feature from csv file
       :param values: values that can represent the feature
       :return: tow dic one with the data we want (filtered) and the rest of the data(trash)
       """
    wanted = dict()
    trash = dict()

    for key in data.keys():
        wanted[key] = list()
        trash[key] = list()

    for key in data.keys():
        n = len(data[feature])
        if key == feature:
            for i in range(n):
                if data[feature][i] in values:
                    fill_dict(data, wanted, i)

                else:
                    fill_dict(data, trash, i)

    return wanted, trash


def fill_dict(data, dictionary, index):
    """
    fills dictionary with list from data in the i"th row
    :param data: the original dictionary
    :param dictionary: dictionary to fill
    :param index: the row to fill from
    :return: none
    """
    for key in data.keys():
        dictionary[key].append(data[key][index])


def print_details(data, features, statistic_functions):
    """ str1 = str

     for feature in features:
         str1 = f"{feature}" + ":"  # check this
         for func in statistic_functions:
             value = statistic_functions[func](data[feature])
             str1 = str1 + value + ","

         print(str1[:-1])"""

    for i in features:
        num_mean = (statistic_functions[0](data[i]))
        num_stdv = (statistic_functions[1](data[i]))
        print(i + ":", round(num_mean, 2), round(num_stdv, 2))


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    """
    prints statistic data on the dictionary data on the two lists under the keys in features
    :param data: dictionary of given data
    :param features: list of two features from the data set
    :param statistic_functions: a list of statistic functions from statistics.py
    :param statistic_functions_names: names of function for printing
    :return:
    """
    for func in statistic_functions:
        print("Cov" + "(" + f"{features[0]}" + ", " + f"{features[1]}" + "): "
              + str(round(func(data[features[0]], data[features[1]]), 2)))
