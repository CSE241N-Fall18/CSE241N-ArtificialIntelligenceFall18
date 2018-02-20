"""
features.py

This file implements functions for feature extraction from text documents.
"""


import os
import numpy as np
import re
import string
import unicodedata


def readfiles(dir):
    """
    Function to read all the files in a directory.

    @dir: Directory to read files from.

    returns: A list containing the text of each file in @dir.
    """

    pwd = os.getcwd()
    os.chdir(dir)

    files = os.listdir('.')
    files_text = []

    for i in files:
        try:
            f = open(i, 'r', encoding='utf-8')
            files_text.append(f.read())
        except:
            print("Could not read %s." % i)
        finally:
            f.close()

    os.chdir(pwd)

    return files_text


# Regex for removing punctuation
_regex = re.compile('^[{0}]+|[{0}]+$'.format(string.punctuation))

# Read stopwords from file
_stopwords_file = open('stopwords', 'r')
_stopwords = set(_stopwords_file.read().split())
_stopwords_file.close()


def extract_words(s):
    """
    Function to split a sentence into a list of words.
    It will replace all punctuation, by a space. Very crude.
    See https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words.

    @s: The string.

    returns: A list of words.
    """

    # Convert the data the data into normal for (Eg: 'ç' to 'c') and lowercase it.
    s = unicodedata.normalize('NFKD', s).lower()

    # Replace the punctuation with a space using the _regex and filter stopwords.
    wordlist = [w for w in _regex.sub(' ', s).split() if w not in _stopwords]

    return wordlist


class BagOfWordsFeatureExtractor(object):
    """
    A bag of words feature extractor.
    """

    def __init__(self, min_freq = 20):
        """
        Initialise the bag of words model.

        @min_freq: Mininum frequency of words to consider as feature.
                   This is extremely important to prevent spurious words
                   (Eg. named entities) from enlarging our dataset too much.
        """

        # A dict that maps a word to an index.
        self.word_to_idx = {}

        # A dict that maps an index to it's word.
        self.idx_to_word = {}

        # Store the min_freq.
        self.min_freq = min_freq

    def preprocess(self, documents):
        """
        Preprocess a list of documents to prepare a bag of words model. It is
        used only once while training.

        Input is a list of strings each of which is a document, this function
        splits those into words and calculates the frequency of each unique word.

        Words with frequencies less than 'self.min_freq' are discarded.

        Then the 'self.word_to_idx' and 'self.idx_to_word' dictionaries are
        created to create a feature vector.

        @documents: A list of strings.
        """

        # A dict storing the frequency of each word
        word_freq = {}

        # Iterate for each document
        for doc in documents:
            # Split the document into a list of words and iterate on it
            for w in extract_words(doc):
                # Update word frequencies
                '''YOUR CODE HERE'''


                ''' END CODE FOR THIS LOOP '''


        # A set of words with frequency less than 'self.min_freq'
        remove_words = set()

        # Check frequency of each word and add to 'remove_words'
        # if it's frequency is below self.min_freq

        ''' YOUR CODE HERE '''


        # Delete the words in 'remove_words' from 'word_freq'


        # Fill 'self.word_to_idx' and 'self.idx_to_word' for
        # each word in 'word_freq' (dicts are explained above)




        ''' END YOUR CODE HERE '''



    def extract(self, documents):
        """
        Extract features from the bag of words extractor using the
        preprocessed dicts. It is called each time we need to calculate
        features from text dataset, i.e both at test and train time.

        For each document 'n', return a vector of size D, where each element
        at index 'i' is the the frequency of the word 'w_i' in 'n'
        divided by the total number of the words in document 'n'.

        @documents: A list of strings.

        returns: A numpy array of size NxD, where N is the length
                 of @documents and D is the number of words which
                 have been processed in the preprocess step.
        """

        # Feature vector to return
        features = np.zeros((len(documents), len(self.idx_to_word)))

        # Raise an exception if 'extract' is called before 'preprocess'
        if len(self.word_to_idx) == 0 or len(self.idx_to_word) == 0:
            raise Exception("Dictionary not initialised.")

        # Iterate over all documents
        for idx, doc in enumerate(documents):
            # Split the doc into a list of words
            words = extract_words(doc)

            # For each word
            for w in words:
                # Calculate it's frequency, however, keep in mind
                # that this word may not have been in the training
                # corpus. In that case, ignore the word.
                ''' YOUR CODE HERE '''


                ''' END CODE FOR THIS LOOP '''

            # Divide the vector by the total number of words in the document to
            # normalize the frequencies.
            ''' YOUR CODE HERE '''

            ''' END CODE FOR THIS LOOP '''

        return features


class TfIdfFeatureExtractor(object):
    """
    A Term frequency-Inverse document frequency feature extractor.
    """

    def __init__(self, min_freq = 20):
        """
        Initialise the Tf-Idf model.

        @min_freq: Mininum frequency of words to consider as feature.
                   This is extremely important to prevent spurious words
                   (Eg. named entities) from enlarging our dataset too much.
        """

        # A dict from word to an index
        self.word_to_idx = {}

        # A dict from an index to a word
        self.idx_to_word = {}

        # A preprocessed vector for storing idf coefficients,
        # which need never be recalculated
        self.idf = None

        # Minimum frequency
        self.min_freq = min_freq

    def preprocess(self, documents):
        """
        Preprocess a list of documents to prepare a Tf-Idf model. It is called only once
        while training.

        Input is a list of strings each of which is a document, this function
        splits those into words and calculates the frequency of each unique word.

        Words with frequencies less than 'self.min_freq' are discarded.

        Then the 'self.word_to_idx' and 'self.idx_to_word' dictionaries are
        created to create a feature vector.

        @documents: A list of strings.
        """

        # Store the total number of documents
        num_docs = np.float(len(documents))

        # A dict storing the frequency of each word across all documents
        total_word_freq = {}

        # A dict storing the number of documents that word appears in
        doc_word_freq = {}

        # Iterate over all documents
        for doc in documents:
            # Split the string into a list of words
            words = extract_words(doc)

            # Update the 'total_word_freq' dict using all words in 'words'
            for w in words:
                ''' YOUR CODE HERE '''


                ''' END CODE FOR THIS LOOP '''

            # Update the 'doc_word_freq' dict. Remember to only add '1' corresponding to
            # each word in a document. In case a word appears twice in a document, then
            # it should be ignored. We use the set() data structure to achieve this.
            for w in set(words):
                ''' YOUR CODE HERE '''


                ''' END CODE FOR THIS LOOP '''

        # A set of words with total frequency less than 'self.min_freq'
        remove_words = set()

        ''' YOUR CODE HERE '''

        # Check frequency of each word and add to 'remove_words'


        # Delete the words in 'remove_words' from 'total_word_freq' and
        # 'doc_word_freq'.


        # Create a numpy array to store frequencies from which
        # we can create the 'self.idf' preprocessed numpy array.
        word_freq_tensor = np.zeros(len(doc_word_freq))

        # For each word in 'doc_word_freq' dict, update
        # 'self.word_to_idx' and 'self.idx_to_word' and
        # 'word_freq_tensor'.


        # Calculate 'self.idf' (see hint.pdf for formula)

        ''' END YOUR CODE HERE '''


    def extract(self, documents):
        """
        Extract features from the Tf-Idf extractor using the
        preprocessed dicts. It is called everytime we need to extract features from
        a dataset, i.e both at training and test time.

        For each document 'n', calculate a vector 'tf' of size D, where each element
        at index 'i' is the the frequency of the word 'w_i' in 'n'
        divided by the total number of the words in document 'n'.

        The output vector is 'tf' multiplied by the 'self.idf' preprocessed vector.

        @documents: A list of strings.

        returns: A numpy array of size NxD, where N is the length
                 of @documents and D is the number of words which
                 have been seen preprocessing step, representing
                 the tf-idf features.
        """

        # Placeholder for return value.
        features = None

        # Create a numpy array of all zeros for storing frequencies.
        tf = np.zeros((len(documents), len(self.idx_to_word)))

        # Raise an exception if 'extract' is called before 'preprocess'
        if len(self.word_to_idx) == 0 or len(self.idx_to_word) == 0:
            raise Exception("Extractor not initialised.")

        # For each document
        for idx, doc in enumerate(documents):
            # Split strig into a list of words
            words = extract_words(doc)

            # Calculate it's frequency, however, keep in mind
            # that this word may not have been in the training
            # corpus. In that case, ignore the word.
            for w in words:
                ''' YOUR CODE HERE '''


                ''' END CODE FOR THIS LOOP '''

            # Divide the frequencies by the number of words in document.
            ''' YOUR CODE HERE '''

            ''' END CODE FOR THIS LOOP '''

        # Calculate the Tf-Idf features.
        features = tf * self.idf

        return features
