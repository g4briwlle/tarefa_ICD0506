""" Choose word """

from random import randint as rng

hangman_words = [
    'davi',
    'roger',
    'bryan',
    'davi',
    'gabrielle',
    'lucas sodré',
    'gustavo',
    'lucas coelho',
    'flavio',
    'sofia',
    'helouise',
    'nicolas',
    'bruno luis'
]


def choose_word():
    return hangman_words[rng(0, len(hangman_words)-1)]
