# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(input_text):
    alphabet = []
    for up_lit in range(65, 91):
        alphabet.append(chr(up_lit))
    for low_lit in range(97, 123):
        alphabet.append(chr(low_lit))

    def permutation_lit(input_text):
        list_word_text = input_text.split(' ')
        new_text = ''
        for word in list_word_text:
            if word[0] in alphabet:
                new_word = word[1:] + word[:1] + 'ay'
                new_text = new_text + new_word + ' '
            else:
                new_word = word
                new_text = new_text + new_word + ' '
        new_text = new_text[0:-1]
        return new_text
    return permutation_lit(input_text)


print(pig_it('Pig latin is cool'))
