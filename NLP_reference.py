'''
Python Natural Language Processing Quick Reference

https://github.com/steincastillo/python-reference.git
Edited by: Stein Castillo
http://www.stein-castillo.com

Table of Contents:
    Library imports
    Book corpora
    NLTK Functions
    Tokenization
    Stemming
    Lemmatization
    Name entity recognition
    Frequency distribution
    Sentiment analysis
'''


### Library imports ###
import nltk                         # Base import
from nltk.sentiment.vader import SentimentIntensityAnalyzer     # Sentiment analyzer
from nltk.tokenize import sent_tokenize     # Sentence tokenizer
from nltk.tokenize import word_tokenize     # Word tokenizer



### Book corpora ###
from nltk.book import *             # Imports the texts of the library included in nltk
'''
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
'''


# NLTK Functions
text1.concordance('monstrous')      # Returns the instances where the word monstrous appears
text1.similar(<word>)               # Identifies contextually similar words
text1.dispersion_plot(['word1', 'word2', 'word3'])  # Creates a dispersion plot of the words list
text5.count('lol')                  # Returns the number of times that word 'lol' apperas in text5
len(text3)                          # Retunrs the number of words in text3
len(set(text3))                     # Returns the number of unique types (tokens) in text3 - includes punctuation symbols
len(set(text3)) / len(text3)        # Calculates the lexical richness of the text

text4.index('awaken')               # Returns the index where the word first occurs



### Tokenization ###
"""
tokenization is the process of breaking a stream of text up into words, 
phrases, symbols, or other meaningful elements called tokens. 
"""

word_tokens = nltk.word_tokenize(text)      # Tokenizes the WORDS of text. Returns a list 
sentence_tokens = nltk.sent_tokenize(text)  # Tokenizes the SENTENCES of text. Returns a list

len(word_tokens)        # Returns the number of words in the tokenized list of text
len(sentence_tokens)    # Returns the number of sentences in the tokenized list of text
word_unique = list(set(word_tokens))  # Eliminates duplicated words in the tokenized list


### Stemming ###
"""
stemming is the process of reducing inflected (or sometimes derived) words to 
their word stem, base or root form
"""

porter = nltk.PorterStemmer()       # Initializes the Porter stemmer
lancaster = nltk.LancasterStemmer() # Initializes the Lancaster stemmer

[porter.stem(t) for t in word_tokens]       # Stems (porter) the tokens in the word_tokens list 
[lancaster.stem(t) for t in word_tokens]    # Stems (lancaster) the tokens in the word_tokens list


### Lemmatization ###
"""
Lemmatisation is the algorithmic process of determining the lemma of a word based on its intended meaning.
Unlike stemming, lemmatisation depends on correctly identifying the intended part of speech and meaning of a word in a sentence, 
as well as within the larger context surrounding that sentence, such as neighboring sentences or even an entire document. 
"""

wnl = nltk.WordNetLemmatizer()      # Initializes the Word Net lemmatizer

[wnl.lemmatize(t) for t in word_tokens] # Lemmatizes (Word Net) the tokens in the word_tokens list


### Frequency distribution ###
'''
Tally of number of times each unique word is used in a text
'''

fdist = FreqDist(text1)         # Calculates the frequency distribution of text1 (Moby Dick by Herman Melville 1851)
len(fdist)                      # Returns the number of unique types (tokens) in text1 - includes punctuation symbols
fdist.most_common(50)           # Returns the 50 most common words of text1
fdist.plot(50, cumulative=True) # Returns the cumulative frequency plot. Helps determine the total number of filler words
fdist.hapaxes()                 # Retunrs the hapaxes (words with one occurrence only)
fdist['whale']                  # Returns the number of occurrences of the word 'whale'


# Searching for long unique words:
ex = set(text1)
big_words = [w for w in ex if len(w)>15]
sorted(big_words)


### Sentiment analysis ###

# NLTK
from nltk.sentiment.vader import SentimentIntensityAnalyzer     # Import the sentiment analyzer

sid = SentimentIntensityAnalyzer()      # Initializes the sentiment analyzer

ss = sid.polarity_scores(sentnce)      # Analizes the sentiment of the sentence

# ss is a dictionary with the sentiment analysis results:
# ss['neg', 'neu', 'pos', 'compound']
# ['compound'] returns the sentiment analisys. (-1 >= x <= 1)
# x = 0: Neutral, x > 0: Pos, x<0: Neg

print (ss['compound'])      # Returns the compund sentiment analysis
