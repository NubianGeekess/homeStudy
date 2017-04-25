def binary_converter(number):
    if number < 0 or number > 255:
        return "Invalid input"
    else:
        binary = bin(number).split('0b')
        binary_string = ''.join(binary)
        return binary_string
print binary_converter(62)
