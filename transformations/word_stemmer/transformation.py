import re

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

from nltk.tokenize import sent_tokenize, word_tokenize

from interfaces.SentenceOperation import SentenceOperation
from tasks.TaskTypes import TaskType

# a set of stemmers to select from
porter = PorterStemmer()
lancaster = LancasterStemmer()

class SimpleWordStemmer(SentenceOperation):
    """
    This class offers method for applying a simple word stemmer to transform
    the text. Stemming is the process of producing morphological variants of 
    a root/base word.

    For example: 
    A word stemmer reduces the words “chocolates”, “chocolatey”, “choco” to 
    the root word, “chocolate” and “retrieval”, “retrieved”, “retrieves” reduce 
    to the stem “retrieve”.
    
    Attributes:

    """

    def stem_text(text, max_outputs = 1):
        tokenized_text = word_tokenize(text)
        stemmed = [porter.stem(word) for word in word_tokenize(raw_text)]
        
        detokenized_text = " ".join(stemmed)
        res_text = re.sub(r'\s([?,.!"](?:\s|$))', r'\1', detokenized_text)
        
        return res

    def __init__(self, seed=0, max_outputs=1):
        super().__init__(seed, max_outputs=max_outputs)

    def generate(self, raw_text: str):
        pertubed_text = stem_text(
            text = raw_text,
            max_outputs = self.max_outputs
        )

        return pertubed_text

"""
# Sample code to demonstrate:

"""