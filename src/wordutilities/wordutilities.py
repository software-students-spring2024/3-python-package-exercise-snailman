import random

def fill_blanks():

    file1 = open("sentences.txt", "r")
    content1 = file1.read()
    file1.close()

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

    file2 = open("most_common_words.txt", "r")
    content2 = file2.read()
    file2.close()

    common_words = content2.split("\n")

    print("\nFill in the blank: " + sent_blank +"\n")

    word1 = common_words[random.randint(0, len(common_words) - 1)]
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
#fill_blanks()