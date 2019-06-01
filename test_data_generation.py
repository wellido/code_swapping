import json
from utils import data_type_analysis, test_generation
import copy
import argparse


def data_preparation(dic_json1, dic_json2, test_path):
    """

    :param dic_json1:
    :param dic_json2:
    :param test_path
    :return:
    """

    with open(dic_json1, 'r') as result_file:
        save_dict1 = json.load(result_file)

    with open(dic_json2, 'r') as result_file:
        save_dict2 = json.load(result_file)

    this_dict1 = copy.deepcopy(save_dict1)
    this_dict2 = copy.deepcopy(save_dict2)

    # get type list
    type_group_list1, type_group_dict1 = data_type_analysis(save_dict1)
    type_group_list2, type_group_dict2 = data_type_analysis(save_dict2)

    # duplicate data generation
    general_data = {}
    for group in type_group_list1:
        group_data = test_generation(this_dict1[group[0]])
        general_data[type(this_dict1[group[0]])] = group_data
    for key in general_data.keys():
        group1 = type_group_dict1[key]
        group2 = type_group_dict2[key]
        for name in group1:
            this_dict1[name] = general_data[key]
        for name in group2:
            this_dict2[name] = general_data[key]

    # test index select
    input_dict = {'f1_select_key': [], 'fragment1': [], 'f2_select_key': [], 'fragment2': []}
    for key in this_dict1.keys():
        print(key)
        input_dict['f1_select_key'].append(key)
        dic_copy1 = copy.deepcopy(this_dict1)
        this_type = type(this_dict1[key])

        random_test_data = []

        # fragment1 input
        for _ in range(10):
            random_test_data.append(test_generation(this_dict1[key]))

        dic_copy1[key] = random_test_data
        input_dict['fragment1'].append(dic_copy1)
        # input_dict[]
        fragment2_keys = []
        fragment2_input = []
        this_group2 = type_group_dict2[this_type]
        # fragment2 input
        for name in this_group2:
            fragment2_keys.append(name)
            dic_copy2 = copy.deepcopy(this_dict2)
            dic_copy2[name] = random_test_data
            fragment2_input.append(dic_copy2)
        input_dict['f2_select_key'].append(fragment2_keys)
        input_dict['fragment2'].append(fragment2_input)

    print(input_dict)
    with open(test_path, 'w') as result_file:
        json.dump(input_dict, result_file, indent=4)
    return save_dict1, save_dict2


def generate_code():
    parser = argparse.ArgumentParser()
    parser.add_argument("--d1_path", type=str,
                        default="data/v1_dict.json",
                        help="data1 path")
    parser.add_argument("--d2_path", type=str,
                        default="data/v2_dict.json",
                        help="data2 path")
    parser.add_argument("--save_path", type=str,
                        default="data/data_dict.json",
                        help="path of the save file")
    args = parser.parse_args()
    d1_path = args.d1_path
    d2_path = args.d2_path
    save_path = args.save_path
    data_preparation(d1_path, d2_path, save_path)


if __name__ == '__main__':
    generate_code()
