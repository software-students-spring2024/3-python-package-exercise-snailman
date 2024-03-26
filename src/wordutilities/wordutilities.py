import random

def select_random_sentence():
    content1 = """The quick brown fox jumps over the lazy dog.
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
    
    sentences = content1.split("\n")
    return sentences[random.randint(0, len(sentences) - 1)]

def select_random_most_common_word():
    content2 = """the
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
    common_words = content2.split("\n")

    return  str(common_words[random.randint(0, len(common_words) - 1)])


def fill_blanks():

    rand_sentence = select_random_sentence()

    words = rand_sentence.split(" ")
    rand_word_index = random.randint(0, len(words) - 1)
    correct_word = words[rand_word_index]

    words[rand_word_index] = "______"

    sent_blank = ""

    for i in range(0,len(words)):
        if(i != 0):
            sent_blank += " " + words[i]
        else:
            sent_blank += words[i]

    print("\nFill in the blank: " + sent_blank +"\n")

    word1 = select_random_most_common_word()
    word2 = select_random_most_common_word()

    while word1 == word2: 
         word2 = select_random_most_common_word()

    options = [correct_word, word1, word2]
        
    options.sort()

    i = 0

    for option in options:
        print(chr(i + 65)+" " + option)
        i += 1

    user_input = input("Enter your answer or quit to exit: ").upper()

    while True:

        if user_input == "QUIT":
            print("\nBye!")
            break

        if user_input not in ["A", "B", "C"]:
                print("\nPlease select A B or C only. Try again.")
                user_input = input("Enter your anwser or quit to exit: ").upper()
                continue

        if options[ord(user_input) - 65] == correct_word:
            print("\nCorrect!")
            break

        if options[ord(user_input) - 65] != correct_word:
            print("\nIncorrect. Try again.")  
            user_input = input("Enter your anwser or quit to exit: ").upper()