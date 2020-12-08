# Detect English module
# https://www.nostarch.com/crackingcodes (BSD Licensed)

# To use, type this code:
#   import detectEnglish
#   detectEnglish.isEnglish(someString) # returns True or False
# (There must be a "dictionary.txt" file in this directory with all English
# words in it, one word per line. You can download this from
# https://invpy.com/dictionary.txt)
UPPERLETTERS = 'AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚÜVWXYZ' #Agregar Ñ, acentos y diéresis
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    #dictionaryFile = open('dictionary.txt')
    dictionaryFile = open('dictEsp.txt', encoding='utf-8')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    #print(possibleWords)

    if possibleWords == []:
        return 0.0 # No words at all, so return 0.0.

    matches = 0
    #print(ENGLISH_WORDS)
    for word in possibleWords:
        if word.lower() in ENGLISH_WORDS:
            matches += 1
    #print(matches)
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message,wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    #print(getEnglishCount(message) * 100)
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    #print(wordsMatch)
    numLetters = len(removeNonLetters(message))
    #print(removeNonLetters(message))
    #print(numLetters)
    messageLettersPercentage = float(numLetters) / len(message) * 100
    #print(messageLettersPercentage)
    lettersMatch = messageLettersPercentage >= letterPercentage
    #print(lettersMatch)
    return wordsMatch and lettersMatch

#print(isEnglish("KROHDU"))
