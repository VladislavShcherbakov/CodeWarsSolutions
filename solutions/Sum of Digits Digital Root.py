# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(number):
    list_str_number = str(number)[::1]
    list_number = []
    for num in list_str_number:
        list_number.append(int(num))
    number = sum(list_number)
    print(number)
    if len(str(number)) > 1:
        return digital_root(number)
    return number


print(digital_root(493193))
