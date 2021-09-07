import sys, errno, re
import nltk

from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

positivity = 0
negativity = 0

def readFile(inputFileDir):
    try:
        with open(inputFileDir, 'r') as file:
            global inputString
            inputString = file.read().replace('\n', '')
            file.close()
        return inputString
    except IOError as e:
        if e.errno == errno.ENOENT:
            print(inputFileDir, 'does not exist')
        elif e.errno == errno.EACCES:
            print(inputFileDir, 'cannot be read')
        else:
            print(inputFileDir, 'some other error')
        return None

def loadWordList(dir):
    file = open(dir, "r")
    words = file.read()
    wordList = words.split("\n")
    return wordList
    file.close()

def removeSpecialCharacters(inputStr):
    return re.sub(r'\W+', ' ', inputStr)

def removeStopWords(inputStr, stopWordsDir):
    stopWordList = loadWordList(stopWordsDir)

    inputWordList = inputStr.split()
    inputWordListStripStopWord = [word for word in inputWordList if word not in stopWordList]
    inputStringStripStopWord = ' '.join(inputWordListStripStopWord)
    
    return inputStringStripStopWord

def normalization(inputStr, stopWordsDir):
    inputString = inputStr.lower()
    inputString = removeSpecialCharacters(inputString)
    inputString = removeStopWords(inputString, stopWordsDir)

    return inputString

def positivity(inputStr, posDir):
    global positivity
    positivity = 0
    positiveWordList = loadWordList(posDir)
    
    for positiveWord in positiveWordList:
        positivity = positivity + inputStr.count(positiveWord)
    
    return positivity

def negativity(inputStr, negDir):
    global negativity
    negativity = 0
    negativeWordList = loadWordList(negDir)
    
    for negativeWord in negativeWordList:
        negativity = negativity + inputStr.count(negativeWord)

    return negativity 

def neutrality(inputStr): 
    return (len(inputStr.split()) - (positivity + negativity))

def manual_sentimentAnalysis(inputStr, stopWordsDir, posDir, negDir):
    normalizedInputString = normalization(inputStr, stopWordsDir)
    pos = positivity(normalizedInputString, posDir)
    neg = negativity(normalizedInputString, negDir)
    neu = neutrality(normalizedInputString)

    sentiment = (pos - neg) / (pos + neg + neu)
    return sentiment

def textBlob_sentimentAnalysis(inputStr, stopWordsDir):
    normalizedInputString = normalization(inputStr, stopWordsDir)
    
    blob = TextBlob(normalizedInputString)
    return blob.sentiment

def nltk_sentimentAnalysis(inputStr, stopWordsDir):
    normalizedInputString = normalization(inputStr, stopWordsDir)
    nltk.download([
        "names",
        "stopwords",
        "state_union",
        "twitter_samples",
        "movie_reviews",
        "averaged_perceptron_tagger",
        "vader_lexicon",
        "punkt",
    ])

    nltk_sentiment = SentimentIntensityAnalyzer()
    return nltk_sentiment.polarity_scores(inputStr)
