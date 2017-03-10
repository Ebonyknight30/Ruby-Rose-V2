import asyncio
import random
import os
import youtube_dl
import subprocess
import shutil

from discord.ext import commands
from utils.tools import *
from utils.mysql import *
from utils.logger import log
from utils.opus_loader import load_opus_lib
from utils import checks
from utils.fun.SmiteGods import *

class Smite():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def randomgod(self, ctx, GodClass:str, *, exclude:str=None, invertExclude:bool=None):
        GodList = []
        print(type(exclude))
        print(len(exclude))
        print(exclude)
        if exclude:
            exclude = exclude.split()
            print(exclude)
            print(type(exclude))
        if invertExclude:
            GodList = exclude
        elif GodClass.upper() == 'ALL' and not invertExclude:
            GodList = AllGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'ASSASSIN' and not invertExclude:
            GodList = AssassinGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'GUARDIAN' and not invertExclude:
            GodList = GuardianGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'HUNTER' and not invertExclude:
            GodList = HunterGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'MAGE' and not invertExclude:
            GodList = MageGods
            if exclude:
                print('i am here!!!!')
                for x in exclude:
                    print(x)
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'WARRIOR' and not invertExclude:
            GodList = WarriorGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        else:
            await self.bot.say("I am sorry {} but {} isn't a God Class(Mage, Assassin, Warrior, Guardian and Hunter)".format(ctx.message.author.name, GodClass))
            return
        await self.bot.delete_message(ctx.message)
        await self.bot.say("{}{}{}".format(ctx.message.author.name, random.choice(phrases),random.choice(GodList)))

    @commands.command(pass_context=True)
    async def randomgodinlist(self, ctx, GodClass:str, *, exclude:str=None, invertExclude:bool=True):
        GodList = []
        print(type(exclude))
        print(len(exclude))
        print(exclude)
        if exclude:
            exclude = exclude.split()
            print(exclude)
            print(type(exclude))
        if invertExclude:
            GodList = exclude
        elif GodClass.upper() == 'ALL' and not invertExclude:
            GodList = AllGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'ASSASSIN' and not invertExclude:
            GodList = AssassinGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'GUARDIAN' and not invertExclude:
            GodList = GuardianGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'HUNTER' and not invertExclude:
            GodList = HunterGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'MAGE' and not invertExclude:
            GodList = MageGods
            if exclude:
                print('i am here!!!!')
                for x in exclude:
                    print(x)
                    if x in GodList:
                        GodList.remove(x)

        elif GodClass.upper() == 'WARRIOR' and not invertExclude:
            GodList = WarriorGods
            if exclude:
                for x in exclude:
                    if x in GodList:
                        GodList.remove(x)

        else:
            await self.bot.say("I am sorry {} but {} isn't a God Class(Mage, Assassin, Warrior, Guardian and Hunter)".format(ctx.message.author.name, GodClass))
            return
        await self.bot.delete_message(ctx.message)
        await self.bot.say("{}{}{}".format(ctx.message.author.name, random.choice(phrases),random.choice(GodList)))

def setup(bot):
    bot.add_cog(Smite(bot))


