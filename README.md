# code_swapping

Step 6: Swap fragments (Python 3.6 version)

### Requrements: 
1. Two fragments with the same variable numbers and types, like [fragment1](https://github.com/wellido/code_swapping/blob/master/data/fragment1.txt) and [fragment2](https://github.com/wellido/code_swapping/blob/master/data/fragment2.txt).
2. Variables json, like [variable1](https://github.com/wellido/code_swapping/blob/master/data/v1_dict.json). Need to save the variables names and the values returning before this fragment in order to judge the type.
3. [*faker*](https://github.com/joke2k/faker)

### Details of step 6 in this implementation:
**a**. Load variable *V* from the json file, [code](https://github.com/wellido/code_swapping/blob/d96ce03d7a99a5b7f8851526e5dbb3b3f483e575/runnable_code_generation.py#L24-L27). 
   Analyze the variable types, [code](https://github.com/wellido/code_swapping/blob/d96ce03d7a99a5b7f8851526e5dbb3b3f483e575/utils.py#L13-L41).

**b - c**. For each variable in fragment1, find the variables in fragment2 whose types are the same as the first one, [code](https://github.com/wellido/code_swapping/blob/d96ce03d7a99a5b7f8851526e5dbb3b3f483e575/test_data_generation.py#L62-L68)

**d - e**. Set a maximum generation number (here is 10) and use the [*faker*](https://github.com/joke2k/faker) library to generate test data, [code](https://github.com/wellido/code_swapping/blob/d96ce03d7a99a5b7f8851526e5dbb3b3f483e575/utils.py#L44-L68), then use control variable method to find the swap variables list, [code](https://github.com/wellido/code_swapping/blob/d96ce03d7a99a5b7f8851526e5dbb3b3f483e575/runnable_code_generation.py#L5-L136).

**finally**. Swap code according to the swap list, [code](https://github.com/wellido/code_swapping/blob/d96ce03d7a99a5b7f8851526e5dbb3b3f483e575/swap_code.py#L5-L11).

### How to use: 

#### test_data_generation.py -> generate test data

Parameters
* d1_path: file path of fragment 1 variables, default=data/v1_dict.json
* d2_path: file path of fragment 2 variables, default=data/v2_dict.json
* save_path: file path of generated data, default=data/data_dict.json

#### main.py -> swap code

Parameters
* d1_path: file path of fragment 1 variables, default=data/v1_dict.json
* d2_path: file path of fragment 2 variables, default=data/v2_dict.json
* save_path: file path of generated data, default=data/data_dict.json
* f1_path: file path of fragment 1 code, default=data/fragment1.txt
* f2_path: file path of fragment 2 code, default=data/fragment2.txt

#### Example
```bash
python test_data_generation.py --d1_path xxx --d2_path xxx --save_path xxx
python main.py --d1_path xxx --d2_path xxx --save_path xxx --f1_path xxx --f2_path xxx
```

#### Case study

##### before swapping
```python
####################### fragment 1 ############################
current_data = save_set[previous_index[i + 1]] + test_data[i]
if current_data >= save_set[i]:
    save_set[i + 1] = current_data
    flag.append([1, previous_index[i + 1]])
else:
    save_set[i + 1] = save_set[i]
    flag.append([0, i])

####################### fragment 2 ############################
cd = td[i] + ss[pi[i + 1]]
if cd < ss[i]:
    ss[i + 1] = ss[i]
    f = f + [[0, i]]
else:
    ss[i + 1] = cd
    f = f + [[1, pi[i + 1]]]
```
##### after swapping
```python
####################### fragment 1 ############################
cd = ss[pi[i + 1]] + td[i]
if cd >= ss[i]:
    ss[i + 1] = cd
    f.append([1, pi[i + 1]])
else:
    ss[i + 1] = ss[i]
    f.append([0, i])
####################### fragment 2 ############################
current_data = test_data[i] + save_set[previous_index[i + 1]]
if current_data < save_set[i]:
    save_set[i + 1] = save_set[i]
    flag = flag + [[0, i]]
else:
    save_set[i + 1] = current_data
    flag = flag + [[1, previous_index[i + 1]]]
```




