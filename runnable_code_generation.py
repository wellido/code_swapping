import json
from utils import data_type_analysis, test_generation
import copy
from results_analysis import analyze_results


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


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
        for _ in range(5):
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


def code_generation(fragment1, fragment2, dic_json):
    """

    :param fragment1:
    :param fragment2:
    :param dic_json:
    :return:
    """

    with open(dic_json, 'r') as result_file:
        save_dict = json.load(result_file)

    select_v_1 = save_dict['f1_select_key']
    select_v_2 = save_dict['f2_select_key']
    data_dict1 = save_dict['fragment1']
    data_dict2 = save_dict['fragment2']

    for idx in range(len(select_v_1)):
        v_1 = select_v_1[idx]
        v_2 = select_v_2[idx]
        d_1 = data_dict1[idx]
        d_2 = data_dict2[idx]

        ####################################### code 1 #######################################
        add_code_before = "for hq in " + str(d_1[v_1]) + ": \n"

        # definition part
        for key in d_1.keys():
            if key != v_1:
                str_line = "\t" + str(key) + " = " + str(d_1[key]) + "\n"
                add_code_before += str_line
            else:
                str_line = "\t" + str(v_1) + " = hq\n"
                add_code_before += str_line
        add_code_before += "\tresult_save_dict = {}\n"
        add_code_before += "\tresult_save_dict['target'] = '%s'\n" % v_1

        # fragment part
        fragment_final = ""
        for line in fragment1.splitlines():
            fragment_final += '\t\t' + line + "\n"
        fragment = "\ttry: " + fragment_final
        exception_info = """\texcept Exception as e:\n\t\tresult_save_dict['runnable'] = False
            \n\t\twith open('results/f1_result_dict.json', 'w') as result_file:\n\t\t\tjson.dump(result_save_dict, result_file)
            """
        fragment = fragment + exception_info

        # result process part
        add_code_after = "\n\tresult_save_dict['runnable'] = True\n"
        for key in d_1:
            str_line = "\tresult_save_dict['%s'] = %s\n" % (key, key)
            add_code_after += str_line

        # result save part
        save_line = """
            \n\timport json
            \n\twith open('results/f1_result_dict.json', 'w') as result_file:
                \n\t\tjson.dump(result_save_dict, result_file)
                \n\t\tresult_file.write("\\n")"""

        run_code = add_code_before + fragment + add_code_after + save_line
        # print(run_code)
        code_run(run_code)

        ####################################### code 2 #######################################
        for part in range(len(v_2)):

            d = d_2[part]
            v = v_2[part]
            add_code_before = "for hq in " + str(d[v]) + ": \n"

            # definition part
            for key in d.keys():
                if key != v:
                    str_line = "\t" + str(key) + " = " + str(d[key]) + "\n"
                    add_code_before += str_line
                else:
                    str_line = "\t" + str(v) + " = hq\n"
                    add_code_before += str_line
            add_code_before += "\tresult_save_dict = {}\n"
            add_code_before += "\tresult_save_dict['target'] = '%s'\n" % v_1

            # fragment part
            fragment_final = ""
            for line in fragment2.splitlines():
                fragment_final += '\t\t' + line + "\n"
            fragment = "\ttry: " + fragment_final
            exception_info = """\texcept Exception as e:\n\t\tresult_save_dict['runnable'] = False
            \n\t\twith open('results/f2_result_dict.json', 'w') as result_file:\n\t\t\tjson.dump(result_save_dict, result_file)
            """
            fragment = fragment + exception_info

            # result process part
            add_code_after = "\n\tresult_save_dict['runnable'] = True\n"
            for key in d:
                str_line = "\tresult_save_dict['%s'] = %s" % (key, key) + "\n"
                add_code_after += str_line

            # result save part
            save_line = """
                        \n\timport json
                        \n\twith open('results/f2_result_dict.json', 'w') as result_file:
                            \n\t\tjson.dump(result_save_dict, result_file)"""
            # print(add_code_after)
            run_code = add_code_before + fragment + add_code_after + save_line
            # print(run_code)
            code_run(run_code)


def code_run(code):
    """

    :param code:
    :return:
    """
    exec(code)


if __name__ == '__main__':
    fragment2 = """
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

    fragment1 = """
for i in range(data_len):
    current_data = save_set[previous_index[i + 1]] + test_data[i][2]
    if current_data >= save_set[i]:
        save_set[i + 1] = current_data
        flag.append([1, previous_index[i + 1]])
    else:
        save_set[i + 1] = save_set[i]
        flag.append([0, i])
        """
    dic_json = "data_dict.json"
    code_generation(fragment1, fragment2, dic_json)
