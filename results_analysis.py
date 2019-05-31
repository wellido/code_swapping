import json
from utils import data_type_analysis


def analyze_results(save_dict1, save_dict2, result_1, result_2):
    """
    Judge if the two results are the same
    :param save_dict1:
    :param save_dict2:
    :param result_1:
    :param result_2:
    :return:
    """
    type_group_list1, type_group_dict1 = data_type_analysis(save_dict1)
    type_group_list2, type_group_dict2 = data_type_analysis(save_dict2)
    with open(result_1, 'r') as result_file:
        result_dict1 = json.load(result_file)
    with open(result_2, 'r') as result_file:
        result_dict2 = json.load(result_file)

    if not result_dict1['runnable'] and not result_dict2['runnable']:
        return True
    if not result_dict1['runnable'] or not result_dict2['runnable']:
        return False

    for group in type_group_list1:
        this_type = type(result_dict1[group[0]])

        str_result1 = []
        str_result2 = []

        for name in type_group_dict1[this_type]:
            if name == result_dict1['target']:
                continue
            str_result1.append(str(result_dict1[name]))
        for name in type_group_dict2[this_type]:
            if name == result_dict2['target']:
                continue
            str_result2.append(str(result_dict2[name]))
        str_result1.sort()
        str_result2.sort()
        if str_result1 != str_result2:
            return False
    return True


