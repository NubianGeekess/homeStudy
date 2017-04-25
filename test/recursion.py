# num_array = list()
# num = 3
# n="j"
# print 'Enter numbers in array: '
# for i in range(int(num)):
#     num_array.append(n)
# print 'ARRAY: ',num_array

def replicate_iter(times, data):
    array = []
    if times <= 0:
        return []
    for i in range(times):
        array.append(data)
    print array

print replicate_iter(-1, "ja")

# def replicate_recur(times, data):
#     array =[]
#     counter = 1
#
#     if counter != times:
#         array.append(data)
#         counter += 1
#     print array
#
#
# print replicate_recur(3, "ja")
