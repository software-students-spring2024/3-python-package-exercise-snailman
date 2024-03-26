import random as random
from collections import Counter

def anagrams(word):
    """
    TO BE IMPLEMENTED
    Returns list of anagrams of word.

    Args:
        word: word to find anagrams for
        
    Returns: 
        List containing anagrams
    """
    raise NotImplementedError

def is_anagram(word1, word2):
    """
    Checks whether two words are anagrams of eachother. Helper function for anagrams()

    Args:
        word1, word2: words to be compared

    Returns:   
        True if words are anagrams, False otherwise.
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
        String of word definitions within range, giving only the first if no range provided
    """

    # if lower is None:
    #     lower = 1
    # commented out for unit testing
    
    raise NotImplementedError

def select_random_sentence():
    """
    Selects a random rentence from 20 sentences.
    Returns:
        String with a sentence from one of the 20 sentences. Chosen at random.
    """
    content = """The quick brown fox jumps over the lazy dog.
My Mum tries to be cool by saying that she likes all the same things that I do.
A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.
Last Friday I saw a spotted striped blue worm shake hands with a legless lizard.
A song can make or ruin a person’s day if they let it get to them.
Sometimes it is better to just walk away from things and go back to them later when you’re in a better frame of mind.
Writing a list of random sentences is harder than I initially thought it would be.
Lets all be unique together until we realise we are all the same.
If I don’t like something, I’ll stay away from it.
I love eating toasted cheese and tuna sandwiches.
If you like tuna and tomato sauce- try combining the two. It’s really not as bad as it sounds.
Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.
Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.
When I was little I had a car door slammed shut on my hand and I still remember it quite vividly.
The clock within this blog and the clock on my laptop are 1 hour different from each other.
I want to buy a onesie… but know it won’t suit me.
I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.
I currently have 4 windows open up… and I don’t know why.
I often see the time 11:11 or 12:34 on clocks.
This is the last random sentence I will be writing and I am going to stop mid-sent."""
    
    sentences = content.split("\n")
    return sentences[random.randint(0, len(sentences) - 1)]

def select_random_most_common_word():
    """
    Selects a random word from a collection of 20 most common words.
    Returns:
        String with a word from one of the 20 most common words. Chosen at random.
    """
    content = """the
and
have
that
for
you
with
say
this
they
but
is
from
not
she
as
what
their
can
who
get"""
    common_words = content.split("\n")

    return  str(common_words[random.randint(0, len(common_words) - 1)])


def fill_blanks():

    """
    Choses at sentence at random, takes out a word from the sentence (also at random), and presents user with three options (A,B,C).
    User must guess correct answer, otherwise they will get a message prompting them to try again.
    User can quit by entering quit.
    """
    
    rand_sentence = select_random_sentence() # get random sentence

    words = rand_sentence.split(" ") 
    rand_word_index = random.randint(0, len(words) - 1)
    correct_word = words[rand_word_index] # pick word

    words[rand_word_index] = "______"  # replace word with blank

    sent_blank = ""

    for i in range(0,len(words)):
        if(i != 0):
            sent_blank += " " + words[i]
        else:
            sent_blank += words[i]

    print("\nFill in the blank: " + sent_blank +"\n") 

    word1 = select_random_most_common_word() # select two random words 
    word2 = select_random_most_common_word()

    while word1 == word2: # make sure random words are not the same
         word2 = select_random_most_common_word()

    options = [correct_word, word1, word2]
        
    options.sort() # sort so there is no particular order to the right answer

    i = 0

    for option in options:
        print(chr(i + 65)+" " + option)
        i += 1

    user_input = input("Enter your answer or quit to exit: ").upper() # get user input

    while True:

        if user_input == "QUIT":  # quit
            print("\nBye!")
            break

        if user_input not in ["A", "B", "C"]: # if invalid answer, let user know and prompt them to enter another answer
                print("\nPlease select A B or C only. Try again.")
                user_input = input("Enter your anwser or quit to exit: ").upper()
                continue

        if options[ord(user_input) - 65] == correct_word: # if correct, quit
            print("\nCorrect!")
            break

        if options[ord(user_input) - 65] != correct_word: # if answer is valid (A,B or C) but incorrect, prompt user to try again
            print("\nIncorrect. Try again.")  
            user_input = input("Enter your anwser or quit to exit: ").upper()
