import random as random
from collections import Counter

def anagrams(word):
    """
    TO BE IMPLEMENTED
    Returns list of anagrams of word.

    Args:
        word: word to find anagrams for
        valid: 
    Returns: list with anagrams
    """

    return True

def is_anagram(word1, word2):
    """
    Checks whether two words are anagrams of eachother. Helper function for anagrams()

    Args:
        word1, word2: words to be compared

    Returns:   
        true if words are anagrams, false otherwise.
    """

    if len(word1) != len(word2):
        return False
    return Counter(word1) == Counter(word2)


def scramble(word):
    """
    Arranges characters in string in random order

    Args:
        word: String to be shuffled

    Returns:
        Shuffled string
    """
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

