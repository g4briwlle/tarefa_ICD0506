""" Current Game State """
import print_word


def print_current_game_state(word, characters_used, num_errors, num_max_tries):
    print_word.print_word(word, characters_used)
    print(f'Letras já utilizadas: {characters_used}')
    print(f'Número de tentativas restantes: {num_max_tries - num_errors}')