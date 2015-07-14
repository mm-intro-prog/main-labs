
import nltk
import re


"""
This function takes in an object of the type PlaintextCorpusReader, and system path.
It returns an nltk corpus

It requires the regular expression package re to work
"""

def create_corpus(wordlist, some_corpus): #process the files so I know what was read in
    for fileid in wordlist.fileids():
        raw = wordlist.raw(fileid)
        raw = re.split(r'\W+', raw) ## split the raw text into appropriate words
        some_corpus.extend(raw)
        #print fileid

    return some_corpus

"""
Create the JayZ Corpus - this is done in the lab walkthrough
"""
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'JayZ'
wordlist = PlaintextCorpusReader(corpus_root, '.*')
the_corpus = create_corpus(wordlist, [])

"""
Exercise 1 - You may want to use the python function set.
"""
def NumberOfUniqueWords(my_text_data):
   return len(set(my_text_data))


"""
Exercise 2 - Lexical diversity score = total word / unique words.
"""
def lexical_diversity(my_text_data):
   word_count = len(my_text_data)
   vocab_size = NumberOfUniqueWords(my_text_data)
   diversity_score = word_count / vocab_size
   return diversity_score

# Output the results
print "The lexical diversity score of JayZ's lyrics is ", lexical_diversity(the_corpus)



"""
Exercise 3 - Compare the lexical diversity of different data sets.
"""
# This is how you see the gutenberg files
files = nltk.corpus.gutenberg.fileids()

# Get a list of the words in Emma & the King James Bible
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
kjv = nltk.corpus.gutenberg.words('bible-kjv.txt')

# Output the lexical diverstity scores
print "The lexical diversity score of emma is ", lexical_diversity(emma)
print "The lexical diversity score of the King James Bible is ", lexical_diversity(kjv)
