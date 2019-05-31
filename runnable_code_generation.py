import json
from utils import data_type_analysis, test_generation
import copy
from results_analysis import analyze_results


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


def code_generation(save_dict1, save_dict2, fragment1, fragment2, dic_json):
    """

    :param save_dict1:
    :param save_dict2:
    :param fragment1:
    :param fragment2:
    :param dic_json:
    :return:
    """
    f1_result_save_path = 'results/f1_result_dict.json'
    f2_result_save_path = 'results/f2_result_dict.json'

    # original data dict
    with open(save_dict1, 'r') as result_file:
        save_dict1 = json.load(result_file)
    with open(save_dict2, 'r') as result_file:
        save_dict2 = json.load(result_file)

    # generated data dict
    with open(dic_json, 'r') as result_file:
        save_dict = json.load(result_file)

    select_v_1 = save_dict['f1_select_key']
    select_v_2 = save_dict['f2_select_key']
    data_dict1 = save_dict['fragment1']
    data_dict2 = save_dict['fragment2']

    swap_list = []
    for idx in range(len(select_v_1)):
        v_1 = select_v_1[idx]
        v_2 = select_v_2[idx]
        d_1 = data_dict1[idx]
        d_2 = data_dict2[idx]
        ####################################### code 1 #######################################
        result_v2_list = [0 for _ in range(len(v_2))]
        data_len = len(d_1[v_1])
        for one_data in d_1[v_1]:
            add_code_before = "import json\n"
            # definition part
            for key in d_1.keys():
                if key != v_1:
                    str_line = str(key) + " = " + str(d_1[key]) + "\n"
                    add_code_before += str_line
                else:
                    str_line = str(v_1) + " = %s\n" % one_data
                    add_code_before += str_line
            add_code_before += "result_save_dict = {}\n"
            add_code_before += "result_save_dict['target'] = '%s'\n" % v_1

            # fragment part
            fragment_final = ""
            for line in fragment1.splitlines():
                fragment_final += '\t' + line + "\n"
            fragment = "try: " + fragment_final

            # result process part
            add_code_after = "\n\tresult_save_dict['runnable'] = True\n"
            for key in d_1:
                str_line = "\tresult_save_dict['%s'] = %s\n" % (key, key)
                add_code_after += str_line

            # result save part
            save_line = """
                            \n\timport json
                            \n\twith open('%s', 'w') as result_file:
                                \n\t\tjson.dump(result_save_dict, result_file)
                                """ % f1_result_save_path

            add_code_after = add_code_after + save_line
            exception_info = """\nexcept Exception as e:\n\tresult_save_dict['runnable'] = False
                \n\twith open('%s', 'w') as result_file:\n\t\tjson.dump(result_save_dict, result_file)
                """ % f1_result_save_path

            run_code = add_code_before + fragment + add_code_after + exception_info
            code_run(run_code)
            ####################################### code 2 #######################################
            for part in range(len(v_2)):

                d = d_2[part]
                v = v_2[part]
                add_code_before = "import json\n"
                for key in d.keys():
                    if key != v:
                        str_line = str(key) + " = " + str(d[key]) + "\n"
                        add_code_before += str_line
                    else:
                        str_line = str(v) + " = %s\n" % one_data
                        add_code_before += str_line
                add_code_before += "result_save_dict = {}\n"
                add_code_before += "result_save_dict['target'] = '%s'\n" % v

                # fragment part
                fragment_final = ""
                for line in fragment2.splitlines():
                    fragment_final += '\t' + line + "\n"
                fragment = "try: " + fragment_final

                # result process part
                add_code_after = "\n\tresult_save_dict['runnable'] = True\n"
                for key in d:
                    str_line = "\tresult_save_dict['%s'] = %s" % (key, key) + "\n"
                    add_code_after += str_line

                save_line = """
                               \n\timport json
                               \n\twith open('%s', 'w') as result_file:
                                \n\t\tjson.dump(result_save_dict, result_file)""" % f2_result_save_path
                add_code_after = add_code_after + save_line

                exception_info = """\nexcept Exception as e:\n\tresult_save_dict['runnable'] = False
                \n\twith open('%s', 'w') as result_file:\n\t\tjson.dump(result_save_dict, result_file)
                """ % f2_result_save_path
                run_code = add_code_before + fragment + add_code_after + exception_info
                code_run(run_code)

                # analyze results
                if analyze_results(save_dict1, save_dict2, f1_result_save_path, f2_result_save_path):
                    result_v2_list[part] += 1

        # find swap name
        for i in range(len(result_v2_list)):
            if result_v2_list[i] == data_len:
                swap_list.append([v_1, v_2[i]])
    print("swap list:")
    print(swap_list)
    return swap_list


def code_run(code):
    """

    :param code:
    :return:
    """
    exec(code)


if __name__ == '__main__':
    fragment2 = """
cd = td[i] + ss[pi[i + 1]]
if cd < ss[i]:
    ss[i + 1] = ss[i]
    f = f + [[0, i]]
else:
    ss[i + 1] = cd
    f = f + [[1, pi[i + 1]]]
    """

    fragment1 = """
current_data = save_set[previous_index[i + 1]] + test_data[i]
if current_data >= save_set[i]:
    save_set[i + 1] = current_data
    flag.append([1, previous_index[i + 1]])
else:
    save_set[i + 1] = save_set[i]
    flag.append([0, i])
        """
    data_json1 = "v1_dict.json"
    data_json2 = "v2_dict.json"
    dic_json = "data_dict.json"
    code_generation(data_json1, data_json2, fragment1, fragment2, dic_json)
    # data_preparation(data_json1, data_json2, dic_json)
