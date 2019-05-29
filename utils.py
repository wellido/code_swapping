import copy
from faker import Faker
import random
import string


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def exec_code(code_str):
    exec(code_str)


def data_type_analysis(dict):
    """

    :param dict:
    :return:
    """
    new_dict = copy.deepcopy(dict)
    type_dict = {}
    for key in new_dict:
        type_dict[key] = type(new_dict[key])
    return type_dict


def test_generation(data_type):
    """

    :param data_type:
    :return:
    """
    fake = Faker()
    if data_type == 'int':
        test_data = fake.random_int(min=-100, max=100)
    elif data_type == 'float':
        test_data = fake.random_number() * 0.01
    elif data_type == 'str':
        # test_data = random_string(5)
        test_data = fake.word()
    elif data_type == 'list':
        list_length = random.randint(0, 10)
        test_data = [random.randint(-100, 100) for _ in range(list_length)]
    elif data_type == 'dict':
        test_data = {}
        dict_length = random.randint(0, 10)
        for _ in range(dict_length):
            test_data[random_string(5)] = random.randint(-100, 100)
    else:
        ...
    return test_data



