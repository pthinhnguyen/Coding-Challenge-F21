#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.sentiment_analysis import *
import argparse, sys

inputString = ''

def main():
    parser = argparse.ArgumentParser(description='Conduct sentiment analysis on a text file')
    parser.add_argument('-i', '--input', help = 'input file path')
    parser.add_argument('-o', '--output', help = 'output file path')
    parser.add_argument('-v', dest='verbose', action='store_true', help = 'display result')
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        # show help when no args
        parser.print_help()
        sys.exit(1)

    inputFile = args.input if args.input is not None else './data/input.txt'
    outputFile = args.output if args.output is not None else './data/output.txt'
    outputFileCreation = open(outputFile, 'w+')
    outputFileCreation.close()
    verbose = True if args.verbose is not None else False

    inputString = readFile(inputFile)
    if not inputString: sys.exit(1)

    nltk_sentiment = nltk_sentimentAnalysis(inputString, "./resources/stop_words.txt")
    textblob_sentiment = textBlob_sentimentAnalysis(inputString, "./resources/stop_words.txt")
    manual_sentiment = manual_sentimentAnalysis(inputString, "./resources/stop_words.txt", "./resources/positives.txt", "./resources/negatives.txt")

    resultNLTK = 'NLTK Lib result: compound = ' + str(nltk_sentiment['compound']) + ' POSITIVE' if nltk_sentiment['compound'] >= 0 else ' NEGATIVE'
    resultTextBlob = 'TextBlob Lib result: polarity = ' + str(textblob_sentiment[0]) + " subjecttivity = " + str(textblob_sentiment[1]) + ' POSITIVE' if textblob_sentiment[0] + textblob_sentiment[1] >= 0 else ' NEGATIVE'
    resultManual = 'Manual Sentiment Score: absolute_sentiment = ' + str(manual_sentiment) + ' POSITIVE' if manual_sentiment >= 0 else ' NEGATIVE'
    result = '\n'.join([resultNLTK, resultTextBlob, resultManual])

    if verbose: print(result)

    with open(outputFile, "r+") as outputWriter:
        data = outputWriter.read()
        outputWriter.seek(0)
        outputWriter.write(result)
        outputWriter.truncate()

if __name__ == "__main__":
    main()


