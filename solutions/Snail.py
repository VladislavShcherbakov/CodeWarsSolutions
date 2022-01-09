# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    matrix_dict = {}
    i = 0
    for list in snail_map:
        i += 1
        j = 0
        for el in list:
            j += 1
            matrix_dict[(i, j)] = el

    list_matrix_dict = [key for key in matrix_dict]
    expected = []
    count = 0

    def array_processing(expected, list_matrix_dict, count):
        copy_list_matrix_dict = list_matrix_dict.copy()
        for key in copy_list_matrix_dict:
            if key[0] == 1 + count:
                expected.append(matrix_dict[key])
                list_matrix_dict.remove(key)
            elif key[1] == len(snail_map) - count:
                expected.append(matrix_dict[key])
                list_matrix_dict.remove(key)

        copy_list_matrix_dict = reversed(list_matrix_dict.copy())

        for key in copy_list_matrix_dict:
            if key[0] == len(snail_map) - count:
                expected.append(matrix_dict[key])
                list_matrix_dict.remove(key)
            elif key[1] == 1 + count:
                expected.append(matrix_dict[key])
                list_matrix_dict.remove(key)

        count += 1
        if len(list_matrix_dict) != 0:
            return array_processing(expected, list_matrix_dict, count)
        else:
            return expected

    return array_processing(expected, list_matrix_dict, count)


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))
