import json

# fragmen1
v1_names = ["data_len", "current_data", "save_set", "previous_index", "test_data", "flag", "i"]
v2_names = ["i", "l", "cd", "td", "ss", "f", "pi"]
v1_values = [6, 7, [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 3, 3], [[0, 4, 2], [1, 6, 4], [5, 7, 4], [2, 9, 7], [8, 10, 2], [8, 11, 1]], [], 6, 7]
v2_values = [0, 6, 7, [[0, 4, 2], [1, 6, 4], [5, 7, 4], [2, 9, 7], [8, 10, 2], [8, 11, 1]], [0, 0, 0, 0, 0, 0, 0], [], [0, 0, 0, 1, 0, 3, 3]]

v1_dict = {}
v2_dict = {}
for i in range(len(v1_names)):
    v1_dict[v1_names[i]] = v1_values[i]
for j in range(len(v2_names)):
    v2_dict[v2_names[j]] = v2_values[j]

import json
with open('data/v1_dict.json', 'w') as result_file:
    json.dump(v1_dict, result_file, indent=4)

with open('data/v2_dict.json', 'w') as result_file:
    json.dump(v2_dict, result_file, indent=4)
