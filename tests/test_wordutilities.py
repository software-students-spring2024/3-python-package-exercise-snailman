import pytest
from unittest.mock import patch
from wordutilities import wordutilities

class TestWordUtilities:
    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed
    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_select_random_sentence_returns_non_empty_string(self):
        sentence = wordutilities.select_random_sentence()
        assert isinstance(sentence, str) and len(sentence) > 0

    def test_select_random_sentence_returns_valid_sentence(self):
        sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "My Mum tries to be cool by saying that she likes all the same things that I do.",      
            "A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.",
            "Last Friday I saw a spotted striped blue worm shake hands with a legless lizard.",
            "A song can make or ruin a person’s day if they let it get to them.",
            "Sometimes it is better to just walk away from things and go back to them later when you’re in a better frame of mind.",
            "Writing a list of random sentences is harder than I initially thought it would be.",
            "Lets all be unique together until we realise we are all the same.",
            "If I don’t like something, I’ll stay away from it.",
            "I love eating toasted cheese and tuna sandwiches.",
            "If you like tuna and tomato sauce- try combining the two. It’s really not as bad as it sounds.",
            "Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.",
            "Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.",
            "When I was little I had a car door slammed shut on my hand and I still remember it quite vividly.",
            "The clock within this blog and the clock on my laptop are 1 hour different from each other.",
            "I want to buy a onesie… but know it won’t suit me.",
            "I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.",
            "I currently have 4 windows open up… and I don’t know why.",
            "I often see the time 11:11 or 12:34 on clocks.",
            "This is the last random sentence I will be writing and I am going to stop mid-sent."
        ]  
        for _ in range(40):  # Arbitrary number of trials to ensure randomness is adequately tested
            sentence = wordutilities.select_random_sentence()
            assert sentence in sentences

    def test_select_random_most_common_word_returns_non_empty_string(self):
        word = wordutilities.select_random_most_common_word()
        assert isinstance(word, str) and len(word) > 0

    def test_select_random_most_common_word_returns_valid_word(self):
        common_words = ["the", "and", "have", "that","for","you","with","say","this","they","but","his","from","not","she","as","what","their","can","who","get"] 
        word = wordutilities.select_random_most_common_word()
        assert word in common_words

    @patch('builtins.input', side_effect=[ 'D','A','quit'])  # Assuming 'D' is an invalid choice leading to retry.
    @patch('builtins.print')
    def test_fill_blanks_incorrect_and_correct_guess(self, mock_print, mock_input):
        # Call the function to trigger the mocked input and print
        wordutilities.fill_blanks()

        # Assert that only these messages will appear: when user enters incorrect/invalid answer, when user enters correct answer, and when user quits
        # Will also verify that for each of these inputs: invalid, incorrect, correct, and "quit" the code will not break
        incorrect_message_found = any("\nPlease select A B or C only. Try again." or "\nIncorrect. Try again."in call_args[0][0] for call_args in mock_print.call_args_list)
        correct_message_found = any("\nCorrect!" in call_args[0][0] for call_args in mock_print.call_args_list)
        quit_message_found = any("\nBye!" in call_args[0][0] for call_args in mock_print.call_args_list)
        assert incorrect_message_found or correct_message_found or quit_message_found 

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
