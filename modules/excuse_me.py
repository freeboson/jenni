#!/usr/bin/env python
'''
excuse_me.py -- Excuse me! Module
Copyright 2015 Sujeet Akula (sujeet@freeboson.org)
Licensed under the Eiffel Forum License 2.

More info:
 * jenni-misc: https://github.com/freeboson/jenni-misc/
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
'''

lead_ins = ["I'm sorry but",
    "Please forgive me —",
    "Beg you a thousand pardons...",
    "I apologize, however,",
    "I'm never usually like this —",
    "You're never going to believe this —",
    "Guess what happened?!?",
    "Holy shit! Get this —",
    "Boy do I have a story for you —",
    "So I was minding my own business and boom!",
    "The most unbelievable thing just happened —",
    "I couldn't be more apologetic, but",
    "Sorry I'm late —",
    "I couldn't go because",
    "I couldn't help it —",
    "This is a terrible excuse but",
    "This is going to sound crazy but",
    "Holy Moses!",
    "Blimey! Sorry I'm late guv'na —",
    "My bad —",
    "I swear it wasn't my fault —",
    "I lost track of time because",
    "I feel terrible, but",
    "Don't blame me —"]

perps = ["your mom",
    "Princess Peach",
    "Godzilla",
    "the offensive line of the '76 Dallas Cowboys",
    "a handicapped gentleman",
    "a triceratops named Penelope",
    "the inventor of the slanket",
    "the director of 101 Dalmations",
    "the little Asian kid from Indiana Jones",
    "a man with six fingers on his right hand",
    "my mom",
    "Raiden from Mortal Kombat",
    "Mayor McCheese",
    "Scrooge McDuck",
    "the ghost of Margaret Thatcher",
    "the ghost of Hitler",
    "Ghost Dad",
    "the entire Roman Empire",
    "Kevin Ware's leg bone",
    "a British chap",
    "a Hasidic Jew",
    "Kevin Spacey",
    "Kevin Costner's stunt double",
    "Kevin McCallister's real life fake tarantula",
    "the editors at BuzzFeed",
    "the hockey team from Iceland in Mighty Ducks 2"]

delays = ["gave me a hickey!",
    "tried to kill me!",
    "ran me over with a diesel backhoe!",
    "died in front of me!",
    "ate my homework!",
    "tried to seduce me!",
    "beat me into submission!",
    "had my Trapper Keeper!",
    "stole my bicycle!",
    "slept with my uncle!",
    "called me 'too gay to fly a kite' -- whatever that means.",
    "stole my identity!",
    "broke into my house!",
    "put me in a Chinese finger trap!",
    "came after me!",
    "came on me!",
    "texted racial slurs from my phone!",
    "spin-kicked me in the collar bone!",
    "tried to sell me vacuum cleaners!",
    "crapped in my gas tank!",
    "made me golf in shoes filled with macaroni and cheese!",
    "pulled me over in a stolen cop car and demanded fellatio!",
    "made me find Cthulu. Praise Cthulu!",
    "kept telling me knock-knock jokes."]

import random

def excuse_me(jenni, *_):
    excuse = ' '.join(map(random.choice, [lead_ins, perps, delays]))
    jenni.say(excuse)

excuse_me.commands = ['excuse_me', 'excuse-me']
excuse_me.priority = 'high'

if __name__ == '__main__':
    print __doc__.strip()


