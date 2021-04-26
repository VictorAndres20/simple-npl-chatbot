import random

HELLO_INPUTS = ['hola', 'cómo estas', 'como estas', 'ola', 'oye', 'ey', 'q mas', 'buenas', 'buenos']
HELLO_OUTPUTS = ['Hola!', 'Cómo te encuebtras hoy?', 'Ey! Que gusto que me escribas!', 'Panita!']

BYE_INPUTS = ['Chao', 'bye', 'adios', 'adiós', 'cuidate', 'chao']
BYE_OUTPUTS = ['Hasta pronto!', 'Fue un placer hablar contigo', 'Un abrazo, saludos']

TY_INPUTS = ['gracias', 'que buena ayuda', 'entendido']
TY_OUTPUTS = ['No hay de qué!', 'Un placer ayudarte!']

HAHA_INPUTS = ['haha', 'jaja', 'JAJA']
HAHA_OUTPUTS = ['jajajajaja', 'jaja', 'JAJA', 'JAJAJAAJA']


def find_coincidence(user_msg, arr_in, arr_out):
    for word in user_msg.split():
        if word.lower() in arr_in:
            return random.choice(arr_out)


def find_start_coincidence(user_msg, arr_in, arr_out):
    for word in user_msg.split():
        for c in arr_in:
            if word.lower()[0:4] == c:
                return random.choice(arr_out)


def hello_response(user_msg):
    return find_coincidence(user_msg, HELLO_INPUTS, HELLO_OUTPUTS)


def bye_response(user_msg):
    return find_coincidence(user_msg, BYE_INPUTS, BYE_OUTPUTS)


def ty_response(user_msg):
    return find_coincidence(user_msg, TY_INPUTS, TY_OUTPUTS)


def haha_response(user_msg):
    return find_start_coincidence(user_msg, HAHA_INPUTS, HAHA_OUTPUTS)
