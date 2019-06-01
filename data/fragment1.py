import bisect


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


test_data = [[0, 4, 2], [1, 6, 4], [5, 7, 4], [2, 9, 7], [8, 10, 2], [8, 11, 1]]
previous_index = define_p(test_data)
save_set = [0] * (len(test_data) + 1)
flag = []
data_len = len(test_data)
test_data.sort(key=take_second)

print("data_len", data_len)
# print("current_data", current_data)
print("save_set", save_set)
print("previous_index", previous_index)
print("test_data", test_data)
print("flag", flag)
# print("i", i)
###################################### fragment 1 #########################################
for i in range(data_len):
    current_data = save_set[previous_index[i + 1]] + test_data[i][2]
    if current_data >= save_set[i]:
        save_set[i + 1] = current_data
        flag.append([1, previous_index[i + 1]])
    else:
        save_set[i + 1] = save_set[i]
        flag.append([0, i])
###################################### fragment 1 #########################################

print("data_len", data_len)
print("current_data", current_data)
print("save_set", save_set)
print("previous_index", previous_index)
print("test_data", test_data)
print("flag", flag)
print("i", i)
