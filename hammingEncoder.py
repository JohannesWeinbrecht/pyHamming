import sys
import math

import util

def find_code_tuple(l: int)->tuple[int, int]:
    # calculate number of use bits
    use_bits = math.floor(math.log2(l))

    if VERBOSE: 
        print(use_bits)
    return (l, (l-use_bits))


def encode(data: list[bool]) -> list[bool]:
    parity_indices = []
    n = 0
    l = len(data)
    while int(math.pow(2, n))<l:
        data.insert(int(math.pow(2, n))-1, False)
        parity_indices.append(int(math.pow(2, n))-1)
        n+=1
        l = len(data)

    n_parity_bits = len(parity_indices)
    if VERBOSE:
        print("Needed Parity bits: ", n_parity_bits)
        print("Hamming Code Type: ", (len(data), len(data)-n_parity_bits))


    true_bits = util.get_true_bits(data)

    parity_bits = util.xor_multiple_bool_list(true_bits)
    if VERBOSE:
        print("Parity bits: ")
        for index, element in enumerate(parity_indices):
            literal = "1" if parity_bits[index] else "0"
            print("p"+ str(element+1), ": ", literal)

    assert(len(parity_bits) == n_parity_bits)


    for i, index in enumerate(parity_indices):
        data[index] = parity_bits[i]

    data = util.reduce_bool_list(data)

    return data

def main():
    global VERBOSE 
    VERBOSE = False
    data = None
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        if '--verbose' in args:
            VERBOSE = True
        string_data = args[-1]
    elif not sys.stdin.isatty():
        string_data = sys.stdin.read().strip()
    else:
        print("No arguments found, please use arguments or pip input")
        sys.exit(1)


    bool_list_data = util.convert_string_to_bool_list(string_data)

    bool_list_result = encode(bool_list_data)

    string_result = util.convert_bool_list_to_string(bool_list_result)

    if VERBOSE:
        print("Final Result: ")
    print(string_result, flush=True)

if __name__ == '__main__':
    main()
