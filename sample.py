from src.wordutilities.wordutilities import *
from wordutilities import wordutilities

class sample:
    print('Testing possible anagrams:')
    print('\'listen\' and \'silent\'? ' + str(is_anagram('listen', 'silent')))
    print('\'elbow\' and \'below\'? ' + str(is_anagram('elbow', 'below')))
    print('\'hello\' and \'world\'? ' + str(is_anagram('hello', 'world')))

    print('\n\nScrambling words:')
    print('scramble of \'hello\': ' + scramble('hello'))
    print('scramble of \'world\': ' + scramble('world'))
    
    print('\n\nFinding anagrams of words:')
    print('anagrams of \'listen\': ' + str(anagrams('listen')))
    print('anagrams of \'elbow\': ' + str(anagrams('elbow')))
    print('anagrams of \'hello\': ' + str(anagrams('hello')))
    print('anagrams of \'QQQ\': ' + str(anagrams('QQQ')))

    print('\n\nFinding anagrams of words plus one wild letter:')
    print('blank anagrams of \'pancak\': ' + str(anagrams_blank('pancak')))
    print('blank anagrams of \'what\': ' + str(anagrams_blank('what')))
    print('blank anagrams of \'QQQ\': ' + str(anagrams_blank('QQQ')))

    print('\n\nFinding permutations of words:')
    print('permuations of \'abc\': ' + str(permutations('abc')))
    print('permutations of \'aabb\': ' + str(permutations('aabb')))

    print('\n\nGetting a random sentence:')
    print(select_random_sentence())
    print(select_random_sentence())

    print('\n\nGetting a random common word:')
    print(select_random_most_common_word())
    print(select_random_most_common_word())
    print(select_random_most_common_word())