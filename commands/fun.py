import asyncio
import cat
import random
import os

from discord.ext import commands
from utils.tools import *
from utils.unicode import *
from utils.fun.lists import *
#from cleverbot import Cleverbot

class Fun():
    def __init__(self, bot):
        self.bot = bot
        #self.cb = Cleverbot()

    @commands.command(pass_context=True)
    async def say(self, ctx, *, message:str):
        """Make the bot say whatever you want it to say"""
        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass
        await self.bot.say(message)

    @commands.command(pass_context=True)
    async def cat(self, ctx):
        """Sends a random cute cat gif because cats are soooo cuteeee <3 >.<"""
        await self.bot.send_typing(ctx.message.channel)
        cat.getCat(directory="data", filename="cat", format="gif")
        await asyncio.sleep(1) # This is so the bot has enough time to download the file
        await self.bot.send_file(ctx.message.channel, "data/cat.gif")
        # Watch Nero spam this command until the bot crashes

    @commands.command(pass_context=True)
    async def f(self, ctx):
        """Press F to pay your respects"""
        await self.bot.say("`{}` has paid their respects! Respects paid: {}".format(ctx.message.author, random.randint(1, 10000)))

    @commands.command()
    async def nicememe(self):
        """Nice Meme!"""
        await self.bot.say("http://niceme.me")

    @commands.command(pass_context=True)
    async def allahuakbar(self, ctx):
        """ALLAHU AKBAR!"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/allahuakbar.gif")

    @commands.command(pass_context=True)
    async def yiffinhell(self, ctx):
        """snek yiff"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/yiffinhell.png")

    @commands.command(pass_context=True)
    async def spam(self, ctx):
        """SPAM SPAM SPAM"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/spam.png")

    @commands.command(pass_context=True)
    async def internetrules(self, ctx):
        """The rules of the internet"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/InternetRules.txt")

    @commands.command(pass_context=True)
    async def quoteaf(self, ctx):
        """Don't quote me on that"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/quotes/{}.png".format(random.randint(1, len([file for file in os.listdir("assets/imgs/quotes")]))))

    @commands.command(pass_context=True)
    async def b1nzy(self, ctx):
        """b1nzy pls no ;-;"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/b1nzy_with_banhammer.png")

    @commands.command(pass_context=True)
    async def cykablyat(self, ctx):
        """Cyka blyat!"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/cykablyat.jpg")

    @commands.command()
    async def sombra(self):
        """Boop me Sombra <3"""
        await self.bot.say(sombra)

    @commands.command()
    async def lenny(self):
        """<Insert lenny face here>"""
        await self.bot.say(lenny)

    @commands.command()
    async def psat(self):
        """Please."""
        await self.bot.say(random.choice(psat_memes))

    @commands.command(pass_context=True)
    async def hoodaf(self, ctx):
        """Me in my hood"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/TheHood.gif")
        await self.bot.say("I look good in a hood, amirite?")

    @commands.command(pass_context=True, name="8ball")
    async def ball(self, ctx, *, question:str):
        """It's just python random don't take it seriously kthx"""
        await self.bot.say("{}: {}".format(ctx.message.author.name, random.choice(magic_conch_shell)))

    @commands.command()
    async def insult(self, *, user:str):
        """Insult those ass wipes"""
        #if user == "EbonyKnight30" or user == '@Ivory' or user == 'Jack' or user == 'Ivory':
        if user.upper() in ["EBONYKNIGHT30", "@IVORY", "JACK", "IVORY", "BALLSBS2", "BALL_SBS2", "MAN-PRI", "MANPRI", "@MAN-PRI", "SAM"]:
            await self.bot.say("{} {}".format(user, random.choice(compliments)))
            return
        elif user.upper() in "RUBY ROSE":
             await self.bot.say('Bitch I am awesome!')
             return
        elif user.upper() in "YANG XIAO LONG":
            await self.bot.say('Yang can sometimes cause things to get a bit out of HAND')
            return
        elif user.upper() in "WEISS SCHNEE":
            await self.bot.say('Weiss is a bitch')
            return
        elif user.upper() in "BLAKE BELLADONNA":
            await self.bot.say('Let\'s just say Gambol Shroud isn\'t the ONLY katana she likes')
            return
        await self.bot.say("{} {}".format(user, random.choice(insults)))

    @commands.command()
    async def actdrunk(self):
        """I got drunk on halloween in 2016 it was great"""
        await self.bot.say(random.choice(drunkaf))

    @commands.command()
    async def talk(self, *, message=None):
        """Talk to the bot"""
        #await self.bot.say(self.cb.ask(message))
        await self.bot.say("Disabled because 5,000 calls won't cut it and I'm not paying money to get more. See https://cleverbot.com/api")

    @commands.command(pass_context=True)
    async def rate(self, ctx, user:discord.User=None):
        """Have the bot rate yourself or another user (rigged af)"""
        if user is None or user.id == ctx.message.author.id:
            await self.bot.say("I rate you a 10/10")
        elif user == self.bot.user:
            await self.bot.say("I rate myself a -1/10")
        elif user.name == 'EbonyKnight30' or user.name == '@Ivory' or user.name == 'Jack' or user.name == 'Ivory':
            await self.bot.say("I rate Jack a -10000/10 because he can't spell")
        else:
            await self.bot.say("I rate {} a {}/10".format(user.name, random.randint(0, 10)))

    @commands.command()
    async def honk(self):
        """Honk honk mother fucka"""
        await self.bot.say(random.choice(honkhonkfgt))

    @commands.command(pass_context=True)
    async def plzmsgme(self, ctx, *, message:str):
        """Makes the bot DM you with the specified message"""
        await self.bot.send_message(ctx.message.author, message)
        await self.bot.say(":ok_hand: check your DMs")

    @commands.command()
    async def fuckherrightinthepussy(self):
        """FUCK HER RIGHT IN THE PUSSY! #FHRITP"""
        await self.bot.say("https://www.youtube.com/watch?v=x7-nzLx4Oa0")

    @commands.command(pass_context=True)
    async def quote(self, ctx, id:str):
        """Quotes a message with the specified message ID"""
        message = await self.bot.get_message(ctx.message.channel, id)
        if message is None:
            await self.bot.say("I could not find a message with an ID of `{}` in this channel".format(id))
            return
        embed = make_message_embed(message.author, message.author.color, message.content, formatUser=True)
        embed.timestamp = message.timestamp
        await self.bot.say(embed=embed)

    @commands.command()
    async def twentyoneify(self, ctx,*, input:str):
        """EVERYTHING NEEDS TWENTY ØNE PILØTS!"""
        await self.bot.say(input.replace("O", "Ø").replace("o", "ø"))

    @commands.command(pass_context=True)
    async def roll(self, ctx, *, sides:str):
        """Rolls a Dice with the spesified number of sides, and critical hit and fail thuresh holds"""
        sides = sides.split()
        if len(sides) >= 3:
            hit = int(sides[0])
            critical = int(sides[1])
            fail = int(sides[2])
        else:
            hit = int(sides[0])
            critical = int(sides[0])
            fail = 1
        roll = random.randint(1, hit)
        if(roll <= fail):
             await self.bot.say("{} rolled a {} CRITICAL FAILURE".format(ctx.message.author.name, roll))
        elif(roll >= critical):
            await self.bot.say("{} rolled a {} CRITICAL HIT".format(ctx.message.author.name, roll))
        else:
            await self.bot.say("{} rolled a {}".format(ctx.message.author.name, roll))

    @commands.command(pass_context=True)
    async def Gasm(self, ctx):
        await self.bot.delete_message(ctx.message)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/Emotes/pGasm.png")

    @commands.command(pass_context=True)
    async def Gasm2(self, ctx):
        await self.bot.delete_message(ctx.message)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/Emotes/pGasm2.png")

    @commands.command(pass_context=True)
    async def emote(self, ctx, *, em: str):
        emote = em
        if '.' not in emote:
            emote += '.png'
        else:
            checkEmote = emote.split('.')
            if 'png' not in checkEmote:
                emote = checkEmote[0]+'.png'
        files = [f for f in os.listdir("assets/Emotes/") if os.path.isfile(os.path.join("assets/Emotes/", f))]
        path = "assets/Emotes/"
        fileList = []
        for pl in files:
            fileList.append(pl.upper())

        if emote.upper() in fileList:
            z = fileList.index(emote.upper())
            z2 = files[z]
            path += z2
        else:
            await self.bot.say("The Emote {} was not found, try checking your spelling".format(emote))
            return
        await self.bot.delete_message(ctx.message)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, path)

    @commands.command()
    async def joke(self):
        """I got drunk on halloween in 2016 it was great"""
        await self.bot.say(random.choice(jokes))






        

def setup(bot):
    bot.add_cog(Fun(bot))
