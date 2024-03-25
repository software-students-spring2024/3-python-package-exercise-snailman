import random as random

def scramble(word):
    word = list(word);
    random.shuffle(word);
    return ''.join(word);

