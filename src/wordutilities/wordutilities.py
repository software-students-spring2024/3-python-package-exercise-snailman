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

def define(word, lower = None, upper = None):
    """
    TO BE IMPLEMENTED
    Finds definition(s) of a word

    Args:
        word: Word to be defined.
        upper: upper bound in range of total function definitions, exclusive
        lower: lower bound in range of total function definitions, inclusive
        
    Returns:
        String of function definitions within range, giving only the first if no range provided
    """

    if lower is None:
        lower = 1
    
    return True
