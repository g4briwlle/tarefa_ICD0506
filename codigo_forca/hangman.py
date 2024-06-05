import choose_word
import current_state
import win_state
import lost_state
import max_tries


# Data
word = choose_word.choose_word()
characters_used = set()
num_errors = 0
num_max_tries = max_tries.num_max_tries()

while num_errors < num_max_tries:
    c = input('Selecione uma letra: ')
    if c not in word:
        num_errors += 1
    characters_used.add(c)
    current_state.print_current_game_state(word, characters_used, num_errors, num_max_tries)
    if set(word).issubset(characters_used):
        win_state.print_win_state()
    if num_errors == num_max_tries:
        lost_state.print_lost_state(word)
