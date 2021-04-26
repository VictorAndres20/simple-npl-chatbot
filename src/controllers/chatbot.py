from src.services.bot import build_sent_tokens, build_response
from src.services.discord_bot import DiscordBot


def start_bot_test():
    sent_tokens = build_sent_tokens()

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
            print("VitiBot: ", end="")
            print(build_response(user_msg, sent_tokens))


def start_bot_discord():
    client = DiscordBot()
    client.run('token')
