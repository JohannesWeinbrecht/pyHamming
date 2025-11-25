import math

def bool_list_to_int(d: list[bool]) -> int:
    ans = 0
    for index, elem in enumerate(d):
        if elem:
            ans += int(math.pow(2, index))
    return ans

def reduce_bool_list(d: list[bool]) -> list[bool]:
    while len(d)>1 and d[-1] == False:
        d.pop()
    return d

def convert_string_to_bool_list(s: str) -> list[bool]:
    bool_list = []
    for s0 in s:
        if s0=="0":
            bool_list.append(False)
        else:
            bool_list.append(True)
    bool_list.reverse()
    return bool_list

def convert_bool_list_to_string(l: list[bool]) -> str:
    s = ""
    l.reverse()
    for i in l:
        if i:
            s += "1"
        else:
            s += "0"
    return s

def get_true_bits(data: list[bool]) -> list[list[bool]]:
    true_bits = []
    for i, d in enumerate(data):
        if d:
            true_bits.append(convert_string_to_bool_list(bin(i+1)[2:]))
    return true_bits

def xor_bool_list(data1: list[bool], data2: list[bool]) -> list[bool]:
    tuple_list = zip(data1, data2)
    result = []
    for i, d in enumerate(tuple_list):
        result.append(d[0] != d[1])

    return result

def xor_multiple_bool_list(data: list[list[bool]]) -> list[bool]:
    if len(data) == 1:
        return data[0]

    max_length = len(data[0])
    for d in data:
        if len(d) > max_length:
            max_length = len(d)
    for i in range(len(data)):
        while len(data[i]) < max_length:
            data[i].append(False)

    result = data[0]
    for i in range(1, len(data)):
        result = xor_bool_list(result, data[i])
    return result
