import random

def fill_blanks():

    content1 = "The quick brown fox jumps over the lazy dog.\nMy Mum tries to be cool by saying that she likes all the same things that I do.\nA purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.\nLast Friday I saw a spotted striped blue worm shake hands with a legless lizard.\nA song can make or ruin a person’s day if they let it get to them.\nSometimes it is better to just walk away from things and go back to them later when you’re in a better frame of mind.\nWriting a list of random sentences is harder than I initially thought it would be.\nLets all be unique together until we realise we are all the same.\nIf I don’t like something, I’ll stay away from it.\nI love eating toasted cheese and tuna sandwiches.\nIf you like tuna and tomato sauce- try combining the two. It’s really not as bad as it sounds.\nSomeone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.\nSometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.\nWhen I was little I had a car door slammed shut on my hand and I still remember it quite vividly.\nThe clock within this blog and the clock on my laptop are 1 hour different from each other.\nI want to buy a onesie… but know it won’t suit me.\nI was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.\nI currently have 4 windows open up… and I don’t know why.\nI often see the time 11:11 or 12:34 on clocks\nThis is the last random sentence I will be writing and I am going to stop mid-sent"

    sentences = content1.split("\n")
    rand_sent_index = random.randint(0, len(sentences) - 1)
    rand_sentence = sentences[rand_sent_index]

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

    content2 = "the\nand\nhav\nthat\nfor\nyou\nwith\nsay\nthis\nthey\nbut\nhis\nfrom\nnot\nshe\nas\nwhat\ntheir\ncan\nwho\nget"
    common_words = content2.split("\n")

    print("\nFill in the blank: " + sent_blank +"\n")

    word1 = common_words[random.randint(0, len(common_words) - 1)]
    word2 = common_words[random.randint(0, len(common_words) - 1)]

    while word1 == word2: 
         word2 = common_words[random.randint(0, len(common_words) - 1)]
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
fill_blanks()