import json
from utils import data_type_analysis


def analyze_results(save_dict1, save_dict2, result_1, result_2):
    """

    :param save_dict1:
    :param save_dict2:
    :param result_1:
    :param result_2:
    :return:
    """
    with open(save_dict1, 'r') as result_file:
        save_dict1 = json.load(result_file)
    with open(save_dict2, 'r') as result_file:
        save_dict2 = json.load(result_file)
    type_group_list1, type_group_dict1 = data_type_analysis(save_dict1)
    type_group_list2, type_group_dict2 = data_type_analysis(save_dict2)
    with open(result_1, 'r') as result_file:
        result_dict1 = json.load(result_file)
    with open(result_2, 'r') as result_file:
        result_dict2 = json.load(result_file)
    if not result_dict1['runnable'] and not result_dict2['runnable']:
        return True

    jump_signal = 0
    if result_dict1['target'] == result_dict2['target']:
        jump_signal = 1

    for group in type_group_list1:
        this_type = type(result_dict1[group[0]])

        str_result1 = []
        str_result2 = []
        for name in type_group_dict1[this_type]:
            if jump_signal and name == result_dict1['target']:
                continue
            str_result1.append(str(save_dict1[name]))
        for name in type_group_dict2[this_type]:
            if jump_signal and name == result_dict2['target']:
                continue
            str_result2.append(str(save_dict2[name]))
        str_result1.sort()
        str_result2.sort()
        print(str_result1)
        print(str_result2)
        if str_result1 != str_result2:
            return False
    print("the same")


