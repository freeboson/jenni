#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
excuse_me.py -- Excuse me! Module
Copyright 2015 Sujeet Akula (sujeet@freeboson.org)
Licensed under the Eiffel Forum License 2.

More info:
 * jenni-misc: https://github.com/freeboson/jenni-misc/
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
'''

lead_ins = [u"I'm sorry but",
    u"Please forgive me —",
    u"Beg you a thousand pardons...",
    u"I apologize, however,",
    u"I'm never usually like this —",
    u"You're never going to believe this —",
    u"Guess what happened?!?",
    u"Holy shit! Get this —",
    u"Boy do I have a story for you —",
    u"So I was minding my own business and boom!",
    u"The most unbelievable thing just happened —",
    u"I couldn't be more apologetic, but",
    u"Sorry I'm late —",
    u"I couldn't go because",
    u"I couldn't help it —",
    u"This is a terrible excuse but",
    u"This is going to sound crazy but",
    u"Holy Moses!",
    u"Blimey! Sorry I'm late guv'na —",
    u"My bad —",
    u"I swear it wasn't my fault —",
    u"I lost track of time because",
    u"I feel terrible, but",
    u"Don't blame me —"]

perps = [u"your mom",
    u"Princess Peach",
    u"Godzilla",
    u"the offensive line of the '76 Dallas Cowboys",
    u"a handicapped gentleman",
    u"a triceratops named Penelope",
    u"the inventor of the slanket",
    u"the director of 101 Dalmations",
    u"the little Asian kid from Indiana Jones",
    u"a man with six fingers on his right hand",
    u"my mom",
    u"Raiden from Mortal Kombat",
    u"Mayor McCheese",
    u"Scrooge McDuck",
    u"the ghost of Margaret Thatcher",
    u"the ghost of Hitler",
    u"Ghost Dad",
    u"the entire Roman Empire",
    u"Kevin Ware's leg bone",
    u"a British chap",
    u"a Hasidic Jew",
    u"Kevin Spacey",
    u"Kevin Costner's stunt double",
    u"Kevin McCallister's real life fake tarantula",
    u"the editors at BuzzFeed",
    u"the hockey team from Iceland in Mighty Ducks 2"]

delays = [u"gave me a hickey!",
    u"tried to kill me!",
    u"ran me over with a diesel backhoe!",
    u"died in front of me!",
    u"ate my homework!",
    u"tried to seduce me!",
    u"beat me into submission!",
    u"had my Trapper Keeper!",
    u"stole my bicycle!",
    u"slept with my uncle!",
    u"called me 'too gay to fly a kite' -- whatever that means.",
    u"stole my identity!",
    u"broke into my house!",
    u"put me in a Chinese finger trap!",
    u"came after me!",
    u"came on me!",
    u"texted racial slurs from my phone!",
    u"spin-kicked me in the collar bone!",
    u"tried to sell me vacuum cleaners!",
    u"crapped in my gas tank!",
    u"made me golf in shoes filled with macaroni and cheese!",
    u"pulled me over in a stolen cop car and demanded fellatio!",
    u"made me find Cthulu. Praise Cthulu!",
    u"kept telling me knock-knock jokes."]

import random

def excuse_me(jenni, *_):
    excuse = ' '.join(map(random.choice, [lead_ins, perps, delays]))
    jenni.say(excuse)

excuse_me.commands = ['excuse_me', 'excuse-me']
excuse_me.priority = 'high'

if __name__ == '__main__':
    print __doc__.strip()


