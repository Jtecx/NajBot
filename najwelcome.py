# bot.py

import os
import discord
import random
from dotenv import load_dotenv


def main():
    load_dotenv()
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')

    @client.event
    async def on_message(message):
        # Checks if it's from a bot (tatsu), has mentions(which it should), if it mentions Naj, and prevents it from
        # self triggering.
        if message.author.bot and message.mentions and message.mentions[0].name == "Naj":
            with open("najcount.txt", "r") as najs:
                najtimes = int(najs.read())
                najtimes += 1

            with open("najcount.txt", "w") as najs2:
                najs2.write(str(najtimes))
                najs2.truncate()

            wittyquotes = ["Planning on staying a while this time?",
                           "You've been here " + str(najtimes) + " times Naj, wanna stay this time?", ""]

            wittyreply = random.choice(wittyquotes)
            await message.channel.send("Hi " + message.mentions[0].name + "! " + wittyreply)
        # else:
        # print (message.author.name + "|" + client.user.name)
        #    await message.channel.send("<@" + str() + ">")

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    main()
