from utils import data_type_analysis
from utils import test_generation
from runnable_code_generation import data_preparation


# a = {"a": 1, "b": 2}
# print(data_type_analysis(a))
# for test_type in [1, 1.0, '1', [1], {"1": 1}]:
#     print("%s : " % test_type, test_generation(test_type))
#
# i = 1
# print(isinstance(i, int))

dic_json2 = "v2_dict.json"
dic_json1 = "v1_dict.json"

data_preparation(dic_json1, dic_json2)
