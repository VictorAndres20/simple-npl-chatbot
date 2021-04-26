import discord
from src.services.bot import build_sent_tokens, build_response


class DiscordBot(discord.Client):

    def __init__(self):
        super().__init__()
        self.sent_token = build_sent_tokens()

    async def on_ready(self):
        print('Discord bot logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('!'):
            usr_msg = message.content[1::]
            print("User: " + usr_msg)
            res = build_response(usr_msg, self.sent_token)
            print("Bot: " + res)
            await message.channel.send(res)


# client = DiscordBot()
# client.run('token')
