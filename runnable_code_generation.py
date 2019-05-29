import json
from utils import exec_code


def code_generation(fragment, dic_json):
    """

    :param fragment:
    :param dic_json:
    :return:
    """
    with open(dic_json, 'r') as result_file:
        save_dict = json.load(result_file)

    add_code_before = ""
    for key in save_dict:
        str_line = str(key) + " = " + str(save_dict[key]) + "\n"
        add_code_before += str_line

    add_code_after = "\nresult_save_dict = {}\n"
    for key in save_dict:
        str_line = "result_save_dict['%s'] = %s" % (key, key) + "\n"
        add_code_after += str_line
    save_line = """
import json
with open('v1_result_dict.json', 'w') as result_file:
    json.dump(result_save_dict, result_file)"""
    # print(add_code_after)
    run_code = add_code_before + fragment + add_code_after + save_line
    print(run_code)
    # print(run_code)
    exec_code(run_code)


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
