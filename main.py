import argparse
from runnable_code_generation import swap_list_generation
from swap_code import code_swapping
from termcolor import colored


def run_code():
    parser = argparse.ArgumentParser()
    parser.add_argument("--d1_path", type=str,
                        default="data/v1_dict.json",
                        help="data1 path")
    parser.add_argument("--d2_path", type=str,
                        default="data/v2_dict.json",
                        help="data2 path")
    parser.add_argument("--f1_path", type=str,
                        default="data/fragment1.txt",
                        help="fragment1 path")
    parser.add_argument("--f2_path", type=str,
                        default="data/fragment2.txt",
                        help="fragment2 path")
    parser.add_argument("--save_path", type=str,
                        default="data/data_dict.json",
                        help="path of the execution results save file")
    args = parser.parse_args()
    d1_path = args.d1_path
    d2_path = args.d2_path
    f1_path = args.f1_path
    f2_path = args.f2_path
    save_path = args.save_path
    fragment1, fragment2, swap_list = swap_list_generation(d1_path, d2_path, f1_path, f2_path, save_path)
    new_fragment1, new_fragment2 = code_swapping(fragment1, fragment2, swap_list)
    print(colored("original fragment 1:", "blue", "on_red"))
    print(fragment1 + "\n")
    print(colored("swapped fragment 1:", 'blue', 'on_red'))
    print(new_fragment1 + "\n")
    print(colored("original fragment 2:", "blue", "on_red"))
    print(fragment2 + "\n")
    print(colored("swapped fragment 2:", 'blue', 'on_red'))
    print(new_fragment2 + "\n")


if __name__ == '__main__':
    run_code()


# python main.py

