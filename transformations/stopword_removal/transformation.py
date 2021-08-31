import sys
from transformations.stopword_removal.languages import languages
import nltk

stopword_library = languages

def stopword_extract(language):
    """
    Takes the language desired as a string (i.e. English is 'en', French is 'fr', etc.)
    Default will be English.
    """
    return stopword_library[language]

def stopword_remove(user_input, stop_words):
    """
    Remove stopwords using standard list comprehension.
    Assumes every string in the user_input is normalized to its lower case equivalent.
    Takes a list of strings and returns a list of strings.
    """
    return [word for word in user_input if word not in stop_words]



def main():

    # a list of stop words to be removed
    stop_words = ['the', 'that', 'to', 'as', 'there', 'has', 'and', 'or', 'is', 'not', 'a', 'of', 'but', 'in', 'by', 'on', 'are', 'it', 'if']

    user_input = 'the cat walked down the road.'.split()
    print(stopword_remove(user_input, stop_words))

if __name__ == "__main__":
    main()