# Utility methods
import sys
import time

# 0.05 is nice for effect
sleepInterval = 0.00


def WhatDoYouDo(prompt, suggestions, suggestionsOn, inventory):

    p(prompt, 2)

    keepAsking = True
    a = suggestions
    while keepAsking:
        keepAsking = False
        p('\nWhat do you do?')
        if suggestionsOn:
            p('(here are some possibilities...)', 2)
            for i in range(len(a)):
                p('... ' + a[i])
        p(n = 2)
        thisAnswer = raw_input('> ')
        strippedAnswer = stripString(thisAnswer)
        l = strippedAnswer.split()

        # Do meta-processing on the answer
        if len(l) == 1:
            if 'quit' in l:
                p(n = 2)
                Quit()
            elif 'inv' in l or 'inven' in l or 'invent' in l or 'inventory' in l:
                PrintInventory(inventory) 
                keepAsking = True
            elif 'budumpckin' in l or 'budump' in l or 'bud' in l:
                p("Oh, Hello Boom!! Happy Birthday!!!!", 2)
                keepAsking = True
            elif 'sugg' in l or 'suggest' in l or 'suggestion' in l or 'suggestions' in l:
                if suggestionsOn == True: 
                    suggestionsOn = False
                    p('Suggestions off...', 2)
                else: 
                    suggestionsOn = True
                    p('Suggestions on...', 2)
                keepAsking = True
            elif 'look' in l:
                p(n = 1)
                p('Ok here is the situation...')
            elif 'com' in l or 'command' in l or 'commands' in l: 
                p(n = 2)
                p('commands:')
                p("  mostly just try to use important words from the descriptions to indicate what you want to do")
                p("  single words like 'staircase' should carry you to other places")
                p("  naming inventory items may work but better is to try and use them in combination")
                p("    for example 'light torch using match' might be helpful")
                p("    but 'match torch' will probably accomplish the same thing")
                p("  you can use relative directions like 'left' and 'up'")
                p("    try and qualify these with 'look' to examine something and 'go' or 'move' to move")
                p("  you can also say 'inventory' and 'quit' and 'suggest' (to turn suggestions on/off)")
                p("  you can use 'look' and 'say' and 'go' and 'get' and 'use' to some effect.")
                p("good luck!")
                p(n = 2)
                keepAsking = True

    p(n = 2)
    return l

# p() is a utility print statement
def p(m = '', n = 0):
    time.sleep(sleepInterval)
    if len(m) > 0: print(m)
    for i in range(n):
        time.sleep(sleepInterval)
        print("\n"),
    
# sorry is the default 'I couldn't figure out what you want to do' reply
def sorry():
    p("sorry I'm afraid I didn't quite understand that...", 2)
    return

# stripString() removes non-essential characters from a reply
def stripString(a):
    irrelevantChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', \
                       '+', '_', '=', '[', ']', '{', '}', ',', '.', '?', '/', \
                       ';', ':', '|', "'", '\"', '\\']
    d = ''
    for c in a:
        if c not in irrelevantChars:
            if c.isupper():
                d += c.lower()
            else:
                d += c
    return d


# PrintInventory(inventory) lets you see what you have on hand
def PrintInventory(inventory):
    p(n = 2)
    p('Your inventory is ' + str(inventory), 2)
    return


# BasicParse() does some basic command parsing
def BasicParse(a):
    if len(a) == 0:
        return 'enter'
    elif len(a) == 1 and 'look' in a: 
        return 'looked'
    elif a[0] == 'say':
        print "you say",
        if len(a) > 1:
            for q in range(1,len(a)):
                print a[q],
        else:
            print "nothing.\n"
            p(n = 1);
        return 'spoke'
    return 'nothing'


def Clarify(a):
    p('How praytell to you propose to ' + a + '?')
    return

def Quit():
    p('ok, bye!!!', 3)
    q = raw_input('hit enter to halt . . .')
    sys.exit(0)
