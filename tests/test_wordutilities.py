import pytest
from src.wordutilities.wordutilities import *

class TestWordUtilities:

    # @pytest.mark.xfail(raises=NotImplementedError)
    def test_is_anagram(self):
        assert is_anagram('listen', 'silent') == True
        assert is_anagram('elbow', 'below') == True
        assert is_anagram('hello', 'world') == False

    # @pytest.mark.xfail(raises=NotImplementedError)
    def test_scramble(self):
        word = 'hello'
        scrambled_word = scramble(word)
        assert sorted(word) == sorted(scrambled_word)
    
    @pytest.mark.xfail(raises=NotImplementedError)
    def test_anagrams(self):
        assert anagrams('listen') == ['silent']
        assert anagrams('elbow') == ['below']
        assert anagrams('elbow') != ['belowwwwww']
        assert anagrams('hello') == []
    
    @pytest.mark.xfail(raises=NotImplementedError)
    def test_define(self):
        # Define with no range specified
        assert define('hello') == 'A greeting or expression of goodwill.'
        
        # Define with upper bound specified
        assert define('hello', upper=2) == 'A greeting or expression of goodwill.'
        
        # Define with lower and upper bounds specified
        assert define('hello', lower=1, upper=2) == 'A greeting or expression of goodwill.'
        
        # Define with invalid range
        assert define('hello', lower=5, upper=10) == 'No definitions found in the given range.'

