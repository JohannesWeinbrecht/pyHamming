import sys
import math

import util

def find_parity_indices(l: int) -> list[int]:
    a = []
    i = 0
    while math.pow(2, i) < l:
        a.append(int(math.pow(2, i))-1)
        i+=1
    if VERBOSE:
        print("Parity indices:")
        print(a)
    return a

def remove_parity_bits(d: list[bool], a: list[int]) -> list[bool]:
    a.sort(reverse=True)

    for index in a:
        d.pop(index)

    return d

def correct_data(d: list[bool], i: int) -> list[bool]:
    d[i] = not d[i]
    return d

def print_error_code(d: list[bool], i: int):
    a = len(d) - i
    print("Error detected and not fixed in hamming code: ")
    string_bin = util.convert_bool_list_to_string(d)
    print(string_bin[0:a] + '\033[1m' + string_bin[a:(a+1)] + '\033[0m' + string_bin[(a+1):len(string_bin)])
    print((len(d)-i)*" " + "^" + (i-1)*" ")

def decode(data: list[bool]) -> list[bool]:

    true_bits = util.get_true_bits(data)


    xor_result = util.xor_multiple_bool_list(true_bits)

    xor_result = util.reduce_bool_list(xor_result)

    parity_indices = find_parity_indices(len(data))

    corrected_result = []

    if xor_result == [False]:
        if VERBOSE:
            print("Code is correct")
        result = remove_parity_bits(data, parity_indices)
        return result
    else:
        mistake_index = util.bool_list_to_int(xor_result) - 1
        if VERBOSE:
            print("Mistake detected")
        if INTERACTIVE:
            correct = False
            answer = input("Do you want to correct the mistake? [y/n]: ")
            if answer == 'y':
                correct = True
            if correct:
                corrected_result = correct_data(data, mistake_index)
            else:
                print_error_code(data, mistake_index)
                return []
        elif AUTOCORRECT:
            corrected_result = correct_data(data, mistake_index)
        else:
            print_error_code(data, mistake_index)
            return []
    corrected_result = remove_parity_bits(corrected_result, parity_indices)
    return corrected_result


def main():
    global VERBOSE 
    VERBOSE = False
    global AUTOCORRECT
    AUTOCORRECT = False
    global INTERACTIVE
    INTERACTIVE = False
    data = None

    if len(sys.argv) > 1:
        args = sys.argv[1:]
        if '--verbose' in args:
            VERBOSE = True

        if '--autocorrect' in args:
            AUTOCORRECT = True
        if '--interactive' in args:
            INTERACTIVE = True

        string_data = args[-1]
    elif not sys.stdin.isatty():
        string_data = sys.stdin.read().strip()
    else:
        print("No arguments found, please use arguments or pip input")
        sys.exit(1)


    #args = sys.argv[1:]

    bool_list_data = util.convert_string_to_bool_list(string_data)

    bool_list_result = decode(bool_list_data)


    string_result = util.convert_bool_list_to_string(bool_list_result)

    if VERBOSE:
        print("Final Result: ")
    print(string_result)

if __name__ == '__main__':
    main()
