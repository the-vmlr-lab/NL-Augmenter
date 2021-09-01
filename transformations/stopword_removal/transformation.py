from nltk.corpus import stopwords
from nltk.tokenize import ToktokTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from interfaces.SentenceOperation import SentenceOperation


class StopwordRemoval(SentenceOperation):
    """
    This is a class that offers a simple stopword removal function.
    """
    def stopword_remove(self, user_input, stopwords_lang='english', tokenized=False, detokenize=True):
        """
        Remove stopwords using standard list comprehension. Default is English.
        Every string in the user_input is detokenized unless otherwise.
        Returns a detokenized version of the text with stopwords removed unless otherwise.
        """
        stop_words = set(stopwords.words(stopwords_lang))
        if tokenized:
            if detokenize:
                return TreebankWordDetokenizer().detokenize([word for word in user_input if word.lower() not in stop_words])
            else:
                return [word for word in user_input if word.lower() not in stop_words]
        else:
            user_input_tokenized = ToktokTokenizer().tokenize(user_input)
            if detokenize:
                return TreebankWordDetokenizer().detokenize([word for word in user_input_tokenized if word.lower() not in stop_words])
            else:
                return [word for word in user_input_tokenized if word.lower() not in stop_words]