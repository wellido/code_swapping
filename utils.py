import copy
from faker import Faker
import random
import string


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def data_type_analysis(dict):
    """

    :param dict:
    :return:
    """
    new_dict = copy.deepcopy(dict)
    type_dict = {}
    key_name_list = []
    type_group = []

    for key in new_dict:
        type_dict[key] = type(new_dict[key])
        key_name_list.append(key)

    for key in key_name_list:
        group = [k for k, v in type_dict.items() if v == type_dict[key]]
        type_group.append(group)
        key_name_list = list(set(key_name_list) - set(group))

    # remove duplicate items
    type_group_final = []
    for key in type_group:
        if key not in type_group_final:
            type_group_final.append(key)
    type_group_dict = {}
    for group in type_group_final:
        type_group_dict[type_dict[group[0]]] = group
    return type_group_final, type_group_dict


def test_generation(data):
    """

    :param data:
    :return:
    """
    fake = Faker()
    if isinstance(data, int):
        test_data = fake.random_int(min=0, max=20)
    elif isinstance(data, float):
        test_data = fake.random_number() * 0.01
    elif isinstance(data, str):
        # test_data = random_string(5)
        test_data = fake.word()
    elif isinstance(data, list):
        list_length = random.randint(0, 20)
        test_data = [random.randint(0, 20) for _ in range(list_length)]
    elif isinstance(data, dict):
        test_data = {}
        dict_length = random.randint(0, 20)
        for _ in range(dict_length):
            test_data[random_string(5)] = random.randint(0, 20)
    else:
        ...
    return test_data



