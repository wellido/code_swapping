import copy
import re


def code_swapping(fragment1, fragment2, swap_list):
    new_fragment1 = copy.deepcopy(fragment1)
    new_fragment2 = copy.deepcopy(fragment2)
    for pair in swap_list:
        new_fragment1 = re.sub(r'(?<!\w)+(%s)+(?!\w)' % pair[0], pair[1], new_fragment1)
        new_fragment2 = re.sub(r'(?<!\w)+(%s)+(?!\w)' % pair[1], pair[0], new_fragment2)
    return new_fragment1, new_fragment2
