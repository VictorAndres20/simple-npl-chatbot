import nltk
import string

lemmer = nltk.stem.WordNetLemmatizer()


def lower(raw):
    return raw.lower()


def build_sentences(raw):
    return nltk.sent_tokenize(raw)


def build_words(raw):
    return nltk.word_tokenize(raw)


def lem_tokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


def build_punctuation_dict():
    return dict((ord(punct), None) for punct in string.punctuation)


def lem_normalize(text):
    remove_punctuation_dict = build_punctuation_dict()
    return lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_dict)))
