from utils import data_type_analysis
from utils import test_generation
from runnable_code_generation import data_preparation
from results_analysis import analyze_results
from swap_code import code_swapping

# data_json1 = "v1_dict.json"
# data_json2 = "v2_dict.json"
# result_path = 'data_dict.json'

# dic1_path = "results/f1_result_dict.json"
# dic2_path = "results/f2_result_dict.json"
# analyze_results(data_json1, data_json2, dic1_path, dic2_path)

fragment1 = """
current_data = save_set[previous_index[i + 1]] + test_data[i]
if current_data >= save_set[i]:
    save_set[i + 1] = current_data
    flag.append([1, previous_index[i + 1]])
else:
    save_set[i + 1] = save_set[i]
    flag.append([0, i])
        """

fragment2 = """
cd = td[i] + ss[pi[i + 1]]
if cd < ss[i]:
    ss[i + 1] = ss[i]
    f = f + [[0, i]]
else:
    ss[i + 1] = cd
    f = f + [[1, pi[i + 1]]]
    """
swap_list = [['data_len', 'l'], ['current_data', 'cd'], ['save_set', 'ss'], ['previous_index', 'pi'], ['test_data', 'td'], ['flag', 'f'], ['i', 'i']]
f1, f2 = code_swapping(fragment1, fragment2, swap_list)
print(f1)
print()
print(f2)
