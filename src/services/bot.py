from src.steps.first_corpus_definition.corpus import read_raw
from src.steps.second_text_preprocess_corpus.nltk_corpus import lower, build_sentences
from src.steps.third_similar_response.manual_responses import hello_response, bye_response, ty_response, haha_response
from src.steps.third_similar_response.process_similar_response import response
import os


def build_sent_tokens():
    dir_name = os.path.dirname(__file__)
    path_corpus = os.path.join(dir_name, "../../resources/corpus.txt")
    raw = read_raw(path_corpus)
    raw = lower(raw)
    return build_sentences(raw)


def build_response(user_msg, sent_tokens):
    if hello_response(user_msg):
        return hello_response(user_msg)
    elif ty_response(user_msg):
        return ty_response(user_msg)
    elif bye_response(user_msg):
        return bye_response(user_msg)
    elif haha_response(user_msg):
        return haha_response(user_msg)
    else:
        return response(user_msg, sent_tokens)
