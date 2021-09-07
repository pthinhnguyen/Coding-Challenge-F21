# UTD ACM Research Coding Challenge (Fall 2021)

Activate python virtual environment before running the script: ***`.\env\Scripts\activate`*** for windows cmd
Command to run the script: ***`python text_analysis.py -i ./data/input.txt`***

This script will analyze the input text file to determine sentiment through three methods: NLTK python module, TextBlob python module, and my self-defined analyzer.

- With NLTK, it is just a simple setup with a pre-trained sentiment analyzer called VADER (Valence Aware Dictionary and sEntiment Reasoner), which returns a compound value of 0.9982.
It means the input text sentiment is positive since the compound value is very near to 1 (near to -1, on the other hand, means negative)

- With TextBlob, the result is polarity = 0.26241134751773043 and subjectivity = 0.60177304964539, which also means the text is a positive voice.
Polarity measure shows the subject text is pretty positive while the subjectivity expresses personal feelings/views on the text, which is also positive.

- My manual self-defined analyzer returns the sentiment score is 0.0 which means neutral since the number of positive words in the text is equal to the number of negative words

###### In conclusion, the given text sentiment is positive. 
