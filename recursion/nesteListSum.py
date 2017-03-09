def nested_list_sum(NL):
    sum = 0
    if isinstance(NL, int):
        return NL

    for i in range(0, len(NL)):
        sum = sum + nested_list_sum(NL[i])
    return sum

print nested_list_sum([1, [3, 4], 5])