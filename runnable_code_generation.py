import json
from utils import exec_code, data_type_analysis, test_generation
import copy


def data_preparation(dic_json1, dic_json2):
    """

    :param dic_json1:
    :param dic_json2:
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
    for key in this_dict1.keys():
        dic_copy1 = copy.deepcopy(this_dict1)
        this_type = type(this_dict1[key])

        random_test_data = []
        for _ in range(5):
            random_test_data.append(test_generation(this_dict1[key]))

        dic_copy1[key] = random_test_data

        this_group2 = type_group_dict2[this_type]
        fragment2_input = []
        for name in this_group2:
            dic_copy2 = copy.deepcopy(this_dict2)
            dic_copy2[name] = random_test_data
            fragment2_input.append(dic_copy2)

    print(this_dict1)
    print(this_dict2)
    print(dic_copy1)
    for data in fragment2_input:
        print(data)


def code_generation(fragment, dic_json):
    """

    :param fragment:
    :param dic_json:
    :return:
    """
    with open(dic_json, 'r') as result_file:
        save_dict1 = json.load(result_file)

    type_dict, type_group = data_type_analysis(save_dict1)
    print(type_group)
    if isinstance(type_dict['i'], int):
        print("hahahaha")
    add_code_before = ""
    for key in save_dict1:
        str_line = str(key) + " = " + str(save_dict1[key]) + "\n"
        add_code_before += str_line

    add_code_after = "\nresult_save_dict = {}\n"
    for key in save_dict1:
        str_line = "result_save_dict['%s'] = %s" % (key, key) + "\n"
        add_code_after += str_line
    save_line = """
import json
with open('v1_result_dict.json', 'w') as result_file:
    json.dump(result_save_dict, result_file)"""
    # print(add_code_after)
    run_code = add_code_before + fragment + add_code_after + save_line
    # print(run_code)
    # print(run_code)
    exec_code(run_code)


# def code_run(start_part, fragment, end_part):
#
#     ...


if __name__ == '__main__':
    fragment = """
while i < l:
    cd = td[i][2] + ss[pi[i + 1]]
    if cd < ss[i]:
        ss[i + 1] = ss[i]
        f = f + [[0, i]]
    else:
        ss[i + 1] = cd
        f = f + [[1, pi[i + 1]]]
    i += 1
    """
    dic_json = "v2_dict.json"
    code_generation(fragment, dic_json)
