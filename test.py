from utils import data_type_analysis
from utils import test_generation


a = {"a": 1, "b": 2}
print(data_type_analysis(a))
for test_type in ['int', 'float', 'str', 'list', 'dict']:
    print("%s : " % test_type, test_generation(test_type))
