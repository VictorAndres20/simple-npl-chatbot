import nltk


def build_freq(data):
    return nltk.FreqDist(data)


def print_freq(data):
    for key, val in data.items():
        print(str(key) + ':' + str(val))
