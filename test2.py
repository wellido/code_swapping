import re

string = fragment1 = """
current_data = save_set[previous_index[i + 1]] + test_data[i]
if current_data >= save_set[i]:
    save_set[i + 1] = current_data
    flag.append([1, previous_index[i + 1]])
else:
    save_set[i + 1] = save_set[i]
    flag.append([0, i])
        """
s = 'save_set'
s2 = 'ss'

a = re.sub(r'(?<!\w)+(%s)\s+(?!\w)' % s, s2, string)
print(a)
