'''
Python Natural Language Processing Quick Reference

https://github.com/steincastillo/python-reference.git
Edited by: Stein Castillo
http://www.stein-castillo.com

Table of Contents:
    Library imports
    Book corpora
    Wordnet
    NLTK Functions
    Tokenization
    Stemming
    Lemmatization
    Frequency distribution
    POS Tagging (part of speech)
    Latent semantic analysis (LSA)
    Sentiment analysis

Natural Language ToolKit (NLTK) is a comprehensive Python library for natural language
processing and text analytics. Originally designed for teaching, it has been adopted in the
industry for research and development due to its usefulness and breadth of coverage. NLTK
is often used for rapid prototyping of text processing programs and can even be used in
production applications
'''


### Library imports ###
import nltk                         # Base import
from nltk.sentiment.vader import SentimentIntensityAnalyzer     # Sentiment analyzer
from nltk.tokenize import sent_tokenize     # Sentence tokenizer
from nltk.tokenize import word_tokenize     # Word tokenizer



### Book corpora ###
'''
A corpus is just a body of text, and corpus readers are designed to make accessing a corpus
much easier than direct file access
'''

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

nltk.corpus.gutenberg.fileids()     # Returns available texts from gutember project include in ntlk corpus
nltk.corpus.webtext.fileids()       # Returns firefox discussion forum and pirates of the caribbean script
nltk.corpus.nps_chat.fileids()      # Returns over 10,000 anonymized posts
ntlk.corpus.brown.fileids()         # Returns brown corpus. first 1 mio word electronic corpus created in 1961

from ntlk.corpus import gutenberg   # Alternative import statement
gutenberg.fileids()                 # Returns available texts from gutember project include in ntlk corpus

bible_words = gutenberg.words(['bible-kjv.txt'])    # Returns the words of the selected text
bible_words = gutenberg.words(['bible-kjv.txt'])[:20] # Returns the first 20 words of the selected text
bible_sentences = gutenberg.sents('bible-kjv.txt')  # Returns the sentences of the selected txt
brown_genres = brown.categories()                   # Returns the categories of the selecte corpus

# Stopwords
'''
Stopwords are common words that carry limited semantic value and generally do not 
contribute to the meaning of a sentence
'''
from nltk.corpus import stopwords
stopwords.fileids()                 # Returns the available languages
english_stop = set(stopwords.words('english'))  # Creates a list with english stopwords
spanish_stop = set(stopwords.words('spanish'))  # Creates a list with spanish stopwords

# Usage example:
words = ["Can't", 'is', 'a', 'contraction']
[word for word in words if word not in english_stop] # Returns ["Can't", 'contraction']

# Stripping stop words from text
clean_text = [word for word in word_text if word not in english_stop]


### Wordnet ###
""" 
Wordnet is a lexical database for the english language. It groups words into sets of 
synonyms called synsets, provides short definitions ans usage exmaples, and records
a number of relations among these synonym sets
-Source: Wikipedia
"""

from nltk.corpus import wordnet as wn   # Imports the wordnet corpus
word = 'chair'
word_synset = wn.synset(word)       # Returns a list with the word synsets
synset.definition()                 # Returns the synset definition
synset.lemma_names()                # Returns sysnet lemma/synonymous words
synset.examples()                   # Returns sysnset usage examples


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

# Word tokenization details
# When tokenizing words, the punctiation and contraction symbols receive special treatemnt:
nlkt.word_tokenize('Hello World.')  # Returns ['Hello', 'World', '.']
nltk.word_tokenize("can't")         # Returns ['ca', "n't"]

# Word Tokenization alternatives

# PunktWordTokenizer
# Splits on punctuation, but keeps it with the word
from nltk.tokenize import PunktWordTokenizer        # Imports the tokenizer
tokenizer = PunktWordTokenizer()                    # Instanciates the tokenizer
tokenizer.tokenize("Can't is a contraction")        # Returns ['Can', "'t", 'is', 'a', 'contraction.']

# WordPunctTokenizer
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
tokenize.tokenizer("Can't is a contraction")        # Returns ['Can', "'", 't', 'is', 'a', 'contraction', '.']

# Tokenizing (sentences) in different languages (Spanish)
para = "Hola amigos. Gracias por ver este video. Saludos"       # Defines the text to tokenize
tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')   # Loads the spanish sentence tokenizer
print (tokenizer.tokenize(para))                                # Tokenizes the text

# Tokenize based on lines, spaces or tweets (special class)
from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

# Line tokenizer
longSentence = 'My name is Maximus Decimus Meridius, Commander of the Armies '\
'of the North, General of the Felix Legions, loyal servant to '\
'the true emperor, Marcus Aurelius. Father to a murdered son, '\
'husband to a murdered wife. And I will have my vengeance, in '\
'this life or the next.'

lTokenizer = LineTokenizer()
sentenceTokens = lTokenizer.tokenize(longSentence)
print (sentenceTokens)

# Space tokenizer
sTokenizer = SpaceTokenizer()
spaceTokens = sTokenizer.tokenize(longSentence)
print (spaceTokens)

# Tweet tokenizer
tweet = 'This is a coool #dummysmiley: :-) :) :-P <3'
tTokenizer = TweetTokenizer()
tTokens = tTokenizer.tokenize(tweet)
print ('Tweet tokenizer outpur:')
print (tTokens)

# Word tokenizer
wTokenizer = word_tokenize(longSentence)
print (wTokenizer)

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


### POS tagging ###
'''
The process of classifying words into their parts of speech and labeling them accordingly 
is known as part-of-speech tagging, POS-tagging, or simply tagging. Parts of speech are also 
known as word classes or lexical categories. The collection of tags used for a particular 
task is known as a tagset.

Universal part of speech tagset
ADJ     Adjective               new, good, high, special, big, local
ADP     Adpoisition             on, of, at, with, by, into, under
ADV     Adverb                  really, already, still, early, now
CONJ    Conjuction              and, or, but, if, while, although
DET     Determiner, article     the, a, some, most, every, no, which
NOUN    NOUN                    year, home, cost, time, Africa
NUM     Numeral                 twenty-four, fourth, 1191, 14:24
PRT     Particle                at, on, out, over, per, that, up, with
PRON    Pronoun                 he, their, her, its, my, I, us
VERB    VERB                    is, say, told, given, playing, would
.       Punctuation marks       . , ; !
X       Other                   ersatz, espirit, dunno, gr8, univeristy
'''
text = 'And now for something completely different'
posTags = nltk.pos_tags(text, tagset='universal') # Returns list of tupples with
                                                  # token (words) and tags using
                                                  # universal tagset

posTags = nltk.pos_tags(text)   # Returns a list of tuples with the token (word) and tag

# Getting help to describe the tagset
nltk.help.upenn_tagset('RB')    # Returns help on the RB tag
nltk.help.upenn_tagset('NN.*')  # Returns help on any tag starting with NN

### Chuncking ###
'''
Chunking segments and labels multi-token sequences
'''
words = ntlk.word_tokenize(sentence)
tags = ntlk.pos_tag(words)
chunks = ntlk.ne_chunk(tags)
print (chunks)

### Frequency distribution ###
'''
Tally of number of times each unique word is used in a text
'''

fdist = FreqDist(text1)         # Calculates the frequency distribution of text1 (Moby Dick by Herman Melville 1851)
                                # Returns a mapword and respective frequency in the input word list
len(fdist)                      # Returns the number of unique types (tokens) in text1 - includes punctuation symbols
fdist.max()                     # Returns the most common token in the word list
fdist.N()                       # Returns the number of tokens in the word list 
fdist.most_common(50)           # Returns the 50 most common words of text1
fdist.plot(50, cumulative=True) # Returns the cumulative frequency plot. Helps determine the total number of filler words
fdist.hapaxes()                 # Retunrs the hapaxes (words with one occurrence only)
fdist['whale']                  # Returns the number of occurrences of the word 'whale'
fdist['what']                   # Returns the number of occurrences of the word 'what'
fdist[fdist.max()]              # Returns the number of ocurrences of the most common token
                                # This method can be uses with a pre-polulated ontology list


# Searching for long unique words:
ex = set(text1)
big_words = [w for w in ex if len(w)>15]
sorted(big_words)

### Latent semantic analysis ###

# Case study, using Bible-kjv.txt from Gutemberg corpus
from sklearn.feature_extraction.text import TfidfVectorizer

# Instanciate the vectorizer
tfidf = TfidfVectorizer()

# Model fitting method 1
tfidf.fit([gutenberg.raw(file_id) for file_id in gutenberg.fileids()])

# Model fitting method 2
tfidf.fit([gutenberg.raw('bible-kjv.txt')])

# Transform the model
X = tfidf.transform([gutenberg.raw('bible-kjv.txt')])

# Evaluate the model
# The higher the weight indicates a rarer or more important word
print ([X[0, tfidf.vocabulary_['lord']]])   # Returns  0.09
print ([X[0, tfidf.vocabulary_['god']]])    # Returns  0.04
print ([X[0, tfidf.vocabulary_['sword']]])  # Returns  0.005


### Sentiment analysis (LSA) ###

# NLTK
from nltk.sentiment.vader import SentimentIntensityAnalyzer     # Import the sentiment analyzer

sid = SentimentIntensityAnalyzer()      # Initializes the sentiment analyzer

ss = sid.polarity_scores(sentnce)      # Analizes the sentiment of the sentence

# ss is a dictionary with the sentiment analysis results:
# ss['neg', 'neu', 'pos', 'compound']
# ['compound'] returns the sentiment analisys. (-1 >= x <= 1)
# x = 0: Neutral, x > 0: Pos, x<0: Neg

print (ss['compound'])      # Returns the compund sentiment analysis
