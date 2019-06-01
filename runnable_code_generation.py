import json
from results_analysis import analyze_results


def swap_list_generation(save_dict1, save_dict2, f1_path, f2_path, dic_json):
    """

    :param save_dict1:
    :param save_dict2:
    :param f1_path:
    :param f2_path:
    :param dic_json:
    :return:
    """
    f1_result_save_path = 'results/f1_result_dict.json'
    f2_result_save_path = 'results/f2_result_dict.json'

    with open(f1_path, 'r') as file:
        fragment1 = file.read()
    with open(f2_path, 'r') as file:
        fragment2 = file.read()

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
            fragment = "try:\n" + fragment_final

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
                fragment = "try:\n" + fragment_final

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
    return fragment1, fragment2, swap_list


def code_run(code):
    """

    :param code:
    :return:
    """
    exec(code)


if __name__ == '__main__':

    with open('data/fragment1.txt', 'r') as file:
        fragment1 = file.read()
    with open('data/fragment2.txt', 'r') as file:
        fragment2 = file.read()

    # print(fragment1)
    # print(fragment2)
    f1_path = 'data/fragment1.txt'
    f2_path = 'data/fragment2.txt'
    data_json1 = "data/v1_dict.json"
    data_json2 = "data/v2_dict.json"
    dic_json = "data/data_dict.json"
    swap_list_generation(data_json1, data_json2, f1_path, f2_path, dic_json)
    # data_preparation(data_json1, data_json2, dic_json)
