# https://www.codewars.com/kata/581e014b55f2c52bb00000f8

def decipher_this(string):
    list_string = string.split(' ')
    decode_word_list = []
    for word in list_string:
        int_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        number_list = []
        letter_list = []
        for el in word:
            if el in int_list:
                number_list.append(el)
            else:
                letter_list.append(el)
        if len(letter_list) > 0:
            letter_list[-1], letter_list[0] = letter_list[0], letter_list[-1]
        decode_word_list.append(chr(int(''.join(number_list))) + ''.join(letter_list))
    return ' '.join(decode_word_list)


print(decipher_this('72olle 103doo 100ya'))
print(decipher_this('82yade 115te 103o'))
