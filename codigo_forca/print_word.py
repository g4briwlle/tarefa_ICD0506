""" Print Word """


def print_word(word, characters_used):
    word_to_user = ''
    for c in word:
        if c in characters_used:
            word_to_user += c
        else:
            word_to_user += '_'
    print(f'Palavra: {word_to_user}')
