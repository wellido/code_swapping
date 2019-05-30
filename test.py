from utils import data_type_analysis
from utils import test_generation
from runnable_code_generation import data_preparation
from results_analysis import analyze_results

data_json1 = "v1_dict.json"
data_json2 = "v2_dict.json"
# result_path = 'data_dict.json'

# code_generation()
# data_preparation(dic_json1, dic_json2, result_path)

dic1_path = "results/f1_result_dict.json"
dic2_path = "results/f2_result_dict.json"
analyze_results(data_json1, data_json2, dic1_path, dic2_path)

# a = ['[]', '[2, 3]', 's']
# b = ['s', '[2, 3]', '[]']
# b.sort(key=str.lower)
# a.sort(key=str.lower)
# if a == b:
#     print(1)
