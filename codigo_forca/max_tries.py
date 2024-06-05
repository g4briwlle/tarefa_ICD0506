""" Number of Maximum Tries """


def num_max_tries():
    num_max_tries = input("Quantas tentativas você quer? ")
    if num_max_tries.isdigit():
        num_max_tries = int(num_max_tries)
    else:
        num_max_tries = 5
    return num_max_tries
