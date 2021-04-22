from src.steps.first_corpus_definition.corpus import read_raw
from src.steps.second_text_preprocess_corpus.nltk_corpus import lower, build_sentences
from src.steps.third_similar_response.manual_responses import hello_response, bye_response, ty_response, haha_response
from src.steps.third_similar_response.process_similar_response import response
import os


def start_bot_test():
    dir_name = os.path.dirname(__file__)
    path_corpus = os.path.join(dir_name, "../../resources/corpus.txt")
    raw = read_raw(path_corpus)
    raw = lower(raw)
    sent_tokens = build_sentences(raw)

    flag = True
    print('VitiBot: Mi nombre es VitiBot. Puedo hablar contigo sobre comida, fútbol, mi colegio y mi familia. '
          'Si quieres salir, escribe salir')
    while flag:
        user_msg = input()
        user_msg = user_msg.lower()
        if user_msg == 'salir':
            flag = False
            print('VitiBot: Espero haberte ayudado! Un abrazo')
        else:
            if hello_response(user_msg):
                print("VitiBot: " + hello_response(user_msg))
            elif ty_response(user_msg):
                print("VitiBot: " + ty_response(user_msg))
            elif bye_response(user_msg):
                print("VitiBot: " + bye_response(user_msg))
            elif haha_response(user_msg):
                print("VitiBot: " + haha_response(user_msg))
            else:
                print("VitiBot: ", end="")
                print(response(user_msg, sent_tokens))
