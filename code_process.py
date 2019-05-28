import bisect
import copy


def take_second(elem):
    return elem[1]


def define_p(data):
    start = [item[0] for item in data]
    end = [item[1] for item in data]
    p = [0, ]
    for j in range(len(data)):
        index = bisect.bisect_right(end, start[j])
        p.append(index)
    return p

# fragment 1
# test_data = [[0, 4, 2], [1, 6, 4], [5, 7, 4], [2, 9, 7], [8, 10, 2], [8, 11, 1]]
# previous_index = define_p(test_data)
# save_set = [0] * (len(test_data) + 1)
# flag = []
# data_len = len(test_data)
# test_data.sort(key=take_second)
#
# for i in range(data_len):
#     current_data = save_set[previous_index[i + 1]] + test_data[i][2]
#     if current_data >= save_set[i]:
#         save_set[i + 1] = current_data
#         flag.append([1, previous_index[i + 1]])
#     else:
#         save_set[i + 1] = save_set[i]
#         flag.append([0, i])




# fragment 2
i = 0
td = [[0, 4, 2], [1, 6, 4], [5, 7, 4], [2, 9, 7], [8, 10, 2], [8, 11, 1]]
pi = define_p(td)
ss = [0] * (len(td) + 1)
f = []
l = len(td)
td.sort(key=take_second)
first_p = locals()
first_p = first_p.copy()
# ...
first_p_cp = copy.copy(first_p)
print(first_p_cp['ss'])
# print(ss)
while i < l:
    cd = td[i][2] + ss[pi[i + 1]]
    if cd < ss[i]:
        ss[i + 1] = ss[i]
        f = f + [[0, i]]
    else:
        ss[i + 1] = cd
        f = f + [[1, pi[i + 1]]]
    i += 1
# print(ss)
second_p = locals()
second_p = second_p.copy()
# ...
second_p_cp = copy.copy(second_p)
print(first_p_cp['ss'])
# print(first_p)
# print(second_p)
second_key = second_p.keys()
new_variable = []
change_key = []
for key in second_p.keys():
    if key not in first_p.keys():
        new_variable.append(key)
        continue
    # print(key)
    if second_p[key] != first_p[key]:
        # print(key)
        # print(second_p[key])
        # print(first_p[key])
        change_key.append(key)
print(change_key)

# print(new_variable)
# print(change_dict)
# print(type(second_p))
# print(second_p['f'])
# print(new_variable)
# print(type(f))
# print(f)
# print(second_p.values())
