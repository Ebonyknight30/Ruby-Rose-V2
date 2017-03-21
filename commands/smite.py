import asyncio
import random
import os
import youtube_dl
import subprocess
import shutil
import openpyxl

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

    @commands.command(pass_context=True)
    async def godStats(self, ctx, *,GodName:str):
        classColum = 'D'
        dmgtypeColum = 'E'
        nameColum = 'C'
        firstRow = 112
        lastRow = 197
        foundRow = False
        currentRow = firstRow
        wb = openpyxl.load_workbook('/Users/Jack/PycharmProjects/Ruby-Rose-V2/utils/fun/SmiteBaseStats.xlsx')
        names = wb.get_sheet_names()
        sheet = wb.get_sheet_by_name('All Gods')
        while not foundRow:
            cellCord = nameColum + str(currentRow)
            if sheet[cellCord].value == GodName:
                foundRow = True
                await self.bot.say('Found god name {} in Cell {}'.format(GodName, cellCord))
            elif currentRow >= lastRow:
                await self.bot.say('Could not find God Name {}, in list.'.format(GodName))
                return
            else:
                currentRow += 1
        currentRow = str(currentRow)
        print(sheet['C'+currentRow].value)
        await self.bot.say('God Name: {} \n God Class: {} \n Damage Type: {} \n HP: {} \n HP per LVL: {} \n MP: {} \n MP per LVL: {} \n Speed: {} \n Attacks/sec: {} \n'.format(sheet['C'+currentRow].value, sheet['D'+currentRow].value,sheet['E'+currentRow].value,sheet['F'+currentRow].value,sheet['G'+currentRow].value,sheet['H'+currentRow].value,sheet['I'+currentRow].value,sheet['J'+currentRow].value,sheet['N'+currentRow].value))
        await self.bot.say('Attacks/sec per LVL: {} \n Damage: {} \n Damage per LVL: {} \n Physical Protections: {} \n Physical Protections per LVL: {} \n'.format(sheet['O'+currentRow].value,sheet['P'+currentRow].value,sheet['Q'+currentRow].value,sheet['S'+currentRow].value,sheet['T'+currentRow].value,))
        await self.bot.say('HP5: {} \n HP5 per LVL: {} \n MP5: {} \n MP5 per LVL: {}'.format(sheet['W'+currentRow].value,sheet['X'+currentRow].value,sheet['Y'+currentRow].value,sheet['Z'+currentRow].value))
        GodClass = sheet['D'+currentRow].value
        DamageType = sheet['E'+currentRow].value
        BaseHp = sheet['F'+currentRow].value
        HpPerLvl = sheet['G'+currentRow].value
        BaseMP = sheet['H'+currentRow].value
        MpPerLvl = sheet['I'+currentRow].value
        BaseSpeed = sheet['J'+currentRow].value
        BaseAttackSpeed = sheet['N'+currentRow].value
        AttackSpeedPerLvl = sheet['O'+currentRow].value
        BaseDamage = sheet['P'+currentRow].value
        DamagePerLvl = sheet['Q'+currentRow].value
        BasePhysProt = sheet['S'+currentRow].value
        PhysProtPerLvl = sheet['T'+currentRow].value
        BaseHp5 = sheet['W'+currentRow].value
        Hp5PerLvl = sheet['X'+currentRow].value
        BaseMp5 = sheet['Y'+currentRow].value
        Mp5PerLvl = sheet['Z'+currentRow].value


    @commands.command(pass_context=True)
    async def godStatsAtLvl(self, ctx, GodName: str, *, Lvl:int):
        classColum = 'D'
        dmgtypeColum = 'E'
        nameColum = 'C'
        firstRow = 112
        lastRow = 197
        foundRow = False
        currentRow = firstRow
        wb = openpyxl.load_workbook('/Users/Jack/PycharmProjects/Ruby-Rose-V2/utils/fun/SmiteBaseStats.xlsx')
        names = wb.get_sheet_names()
        sheet = wb.get_sheet_by_name('All Gods')
        while not foundRow:
            cellCord = nameColum + str(currentRow)
            if sheet[cellCord].value == GodName:
                foundRow = True
                await self.bot.say('Found god name {} in Cell {}'.format(GodName, cellCord))
            elif currentRow >= lastRow:
                await self.bot.say('Could not find God Name {}, in list.'.format(GodName))
                return
            else:
                currentRow += 1
        currentRow = str(currentRow)
        GodClass = sheet['D' + currentRow].value
        DamageType = sheet['E' + currentRow].value
        BaseHp = sheet['F' + currentRow].value
        HpPerLvl = sheet['G' + currentRow].value
        BaseMP = sheet['H' + currentRow].value
        MpPerLvl = sheet['I' + currentRow].value
        BaseSpeed = sheet['J' + currentRow].value
        BaseAttackSpeed = sheet['N' + currentRow].value
        AttackSpeedPerLvl = sheet['O' + currentRow].value
        BaseDamage = sheet['P' + currentRow].value
        DamagePerLvl = sheet['Q' + currentRow].value
        BasePhysProt = sheet['S' + currentRow].value
        PhysProtPerLvl = sheet['T' + currentRow].value
        BaseMagProt = sheet['U' + currentRow].value
        MagProtPerLvl = sheet['V' + currentRow].value
        BaseHp5 = sheet['W' + currentRow].value
        Hp5PerLvl = sheet['X' + currentRow].value
        BaseMp5 = sheet['Y' + currentRow].value
        Mp5PerLvl = sheet['Z' + currentRow].value

        HP = float(BaseHp) + (float(HpPerLvl)*Lvl)
        MP = float(BaseMP) + (float(MpPerLvl)*Lvl)
        AttackSpeed = float(BaseAttackSpeed) + (float(AttackSpeedPerLvl)*Lvl)
        Damage = float(BaseDamage) + (float(DamagePerLvl)*Lvl)
        PhysProt = float(BasePhysProt) + (float(PhysProtPerLvl)*Lvl)
        MagProt = float(BaseMagProt) + (float(MagProtPerLvl)*Lvl)
        HP5 = float(BaseHp5) + (float(Hp5PerLvl)*Lvl)
        MP5 = float(BaseMp5) + (float(Mp5PerLvl)*Lvl)

        await self.bot.say('Name: {} \n Level: {} \n HP: {} \n MP: {} \n Attack Speed: {} \n Damage: {} \n Physical Protections: {} \n Magical Protections: {} \n HP5: {} \n MP5: {}'.format(GodName,Lvl,str(HP),str(MP),str(AttackSpeed),str(Damage),str(PhysProt),str(MagProt),str(HP5),str(MP5)))

def setup(bot):
    bot.add_cog(Smite(bot))


