import sys
import time
import items
import enemies

# Global state variables
printSuggestions = False
foyerSpiderAsleep = False
inventory = ['torch', 'sword', 'biscuit', 'match']
libraryBooksPiled = False
libraryFireLit = False


# Suggestions
suggEntrance = ['light my torch with my last match',\
                'run back down the path I came here on',\
                'knock on the front door',\
                'try to open the front door',\
                'wait for something to happen']
suggFoyerSpiderAsleep = ['take a nap', 'go up the stairs', 'go back outside', \
                         'go through the doors', 'tickle the spider']
suggFoyerSpiderAwake = ['Pull out the little sword and attack the spider', \
                        'Run back outside in terror',\
                        'Pull out my last remaining biscuit and throw it at the spider',\
                        'Run forward to give ths spider a big kiss', \
                        'Wait and see what happens']
suggLibraryPileFire = ['x', 'y', 'z']
suggLibraryPileNoFire = ['x', 'y', 'z']
suggLibraryNoPileFire = ['x', 'y', 'z']
suggLibraryNoPileNoFire = ['read some books','search the shelves for interesting clues',\
                           'do my best Hermione impersonation','light a book on fire',\
                           'talk really really loud','stack up the books in a pile']
suggHall = ['x', 'y', 'z']

sleepInterval = 0.20
# 0.05 is nice for effect


# methods


# rooms 
def Entrance():
    while True:

        p('You are outside an old castle. It looks very creepy.')
        p('There are bats flying here and there in the late dusk.')
        p('There is a lone light shining from one window at the top tower.')
 
        PrintInventory()

        a = WhatDoYouDo(suggEntrance)

        if LookCheck(a): DoNothing()
        elif 'match' in a or ('light' in a and 'torch' in a):
	    if 'match' in inventory:
                p('A bat flies by and the wind from its wings puts out your match before you can light your torch! Oh no!', 2)
	        inventory.remove('match')
	        inventory.append('burnt match')
	    else:
 	        p("You actually don't have a match for some reason... maybe you already used it?", 2)
        elif ('go' in a or 'walk' in a or 'run' in a) and 'path' in a:
	    p('You head back down the path into the forest where you are devoured by wolves. You lose! Sorry...', 2)
	    sys.exit()
        elif 'door' in a or 'knock' in a or 'foyer' in a:
	    p('As you touch the door it easily swings open with a creak... it was not fastened.', 2)
	    Foyer()
        elif 'wait' in a:
   	    p('The night deepens.  Off in the distance a wolf howls in the forest. The wolf sounds hungry.', 2)
        elif 'biscuit' in a: 
            p("You eat some of the biscuit but as you're rather full you save some for later.", 2)
        else:
            sorry()
    
    Foyer()
    return


def Foyer():
    global foyerSpiderAsleep
    p(n = 2)
    p('This is the foyer, a chamber filled with gigantic decorative stuffed spiders.')
    stuckFoyer = True
    firstTimeWithAwake = True
    firstTimeWithAsleep = True
    while stuckFoyer:
        if foyerSpiderAsleep:

            if firstTimeWithAsleep:
                p('There is one fat snoring real spider here who gently burps biscuit odors.')
                p('There is a staircase here leading up to the left and a set of double doors leading inwards.', 2)
                firstTimeWithAsleep = False
            else:
                p('The foyer. There is a snoring spider, a staircase going up to the left, double doors leading inwards.', 2)

            a = WhatDoYouDo(suggFoyerSpiderAsleep)

            if LookCheck(a): DoNothing()
            elif 'nap' in a:
                p('Child Services sees you napping and takes you off to Juvie. You lose.', 3) 
                sys.exit()
            elif 'upstairs' in a or 'stairs' in a or 'stair' in a or 'staircase' in a or 'left' in a or ('go' in a and 'up' in a):
                p('Going up the stairs takes you to the library.', 1)
                Library()
            elif 'outside' in a or 'out' in a or 'back' in a:
                Entrance()
            elif 'through' in a or 'doors' in a or 'inwards' in a:
                p('Going through the double doors takes you to the main hall.', 1)
                Hall()
            elif 'tickle' in a:
                p("The spider giggles quietly in its sleep and says something that sounds like 'rutabaga'", 3)
            else:
                sorry()

        else:
            if firstTimeWithAwake:
                p('...at least you assume they are all stuffed. Suddenly one of them moves, though!')
                p('It is clambering down the wall and advancing towards you in that creepy spider way.')
                p('It looks like it means business! It is hissing and singing a song about eating you!')
                firstTimeWithAwake = False
            else:
                p('The foyer. A menacing spider is attacking you!!', 2)

            a = WhatDoYouDo(suggFoyerSpiderAwake)

            if LookCheck(a): DoNothing()
            elif 'sword' in a:
                if 'sword' in inventory:
                    p('The spider takes your sword from you and eats it!', 2)
                    inventory.remove('sword')
                else:
                    p("Oh shoot you don't have a sword!")
            elif 'run' in a and ('away' in a or 'back' in a or 'outside' in a):
                Entrance()
            elif 'biscuit' in a:
                p('The spider grabs and gobbles that biscuit, licks her appendages and falls fast asleep', 2)
                foyerSpiderAsleep = True
                inventory.remove('biscuit')
            elif 'kiss' in a or 'lips' in a:  
                p('The spider bites you on your outstretched lips... you fall asleep for the remainder of the game.', 3)
                sys.exit()
            elif 'wait' in a: 
                p('The spider bites you on your lazy bumpkin... you fall asleep for the remainder of the game.', 3)
                sys.exit()
            else:
                sorry()
    return


def Library():
    p('The Library. There are hundreds of books here... maybe thousands.')
    if libraryBooksPiled:
        if libraryFireLit:
            p('There are stairs going down, a big pile of books under a high window, a door, and a fireplace with a fire in it.')
            a = WhatDoYouDo(suggLibraryPileFire)
            if LookCheck(a): DoNothing()
            else:
                sorry()
        else:
            p('There are stairs going down, a big pile of books under a high window, a door, and a fireplace but no fire.')
            a = WhatDoYouDo(suggLibraryPileNoFire)
            if LookCheck(a): DoNothing()
            else:
                sorry()
    else:
        if libraryFireLit:
            p('There are stairs leading down, a high window, a door, and a fireplace with a fire in it.')
            a = WhatDoYouDo(suggLibraryNoPileFire)
            if LookCheck(a): DoNothing()
            else:
                sorry()
        else:
            p('There are stairs leading down, a high window, a door, and a fireplace but no fire.')
            a = WhatDoYouDo(suggLibraryNoPileNoFire)
            if LookCheck(a): DoNothing()
            else:
                sorry()

    return

def Hall():
    p('This is the main hall.', 3)
    a = WhatDoYouDo(suggHall)
    if LookCheck(a): DoNothing()
    else:
        sorry()
    return


# Utility methods


# Kilroy To Do List
# Implement all the blankline prints usling slp

def p(m = '', n = 0):
    time.sleep(sleepInterval)
    if len(m) > 0: print(m)
    for i in range(n):
        time.sleep(sleepInterval)
        print("\n"),
    

def sorry():
    p("sorry I'm afraid I didn't quite understand that...", 2)
    return

def stripString(a):
    irrelevantChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', \
                       '+', '_', '=', '[', ']', '{', '}', ',', '.', '?', '/', \
                       ';', ':', '|', "'", '\\']
    d = ''
    for c in a:
        if c not in irrelevantChars:
            d += c
    print 'here is a:', a
    print 'here is d:', d
    return d


def WhatDoYouDo(suggestions):

    # must declare a global if you intend to modify it
    global printSuggestions

    keepAsking = True
    a = suggestions
    while keepAsking:
        keepAsking = False
        p('\nWhat do you do?')
        if printSuggestions:
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
                p('...ok, bye!', 2)
	        sys.exit()
            elif 'inv' in l or 'inven' in l or 'invent' in l or 'inventory' in l:
                PrintInventory() 
                keepAsking = True
            elif 'budumpckin' in l or 'budump' in l or 'bud' in l:
                p("Oh, Hello Boom!! Happy Birthday!!!!", 2)
                keepAsking = True
            elif 'sugg' in l or 'suggest' in l or 'suggestion' in l or 'suggestions' in l:
                if printSuggestions == True: 
                    printSuggestions = False
                    p('Suggestions off...', 2)
                else: 
                    printSuggestions = True
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
                p("good luck!")
                p(n = 2)
                keepAsking = True

    p(n = 2)
    return l


def PrintInventory():
    p(n = 2)
    p('Your inventory is ' + str(inventory), 2)
    return


def LookCheck(a):
    if len(a) == 1 and 'look' in a: 
        return True
    return False


def DoNothing():
    return
    

# main

# Items are not working yet...
# torch = Item('torch','something that burns','1')

p(n = 3)

p('                                                             *         ')
p('                                                            ***        ')
p('                                                           *****       ')
p('                                                          ** ****      ')
p('        **  **                                           **   ****     ')
p('        *******                                         *** o *****    ')
p('        *******                                       *****   ******   ')
p('       ***   ***                                     ****************  ')
p('      ****   ****                                      ************    ')
p('     *************                                     ************    ')
p('       *********                       ***   ***   *** *** ********    ')
p('       *********                       *************** **   *******    ')
p('       *********                       *************** **   *******    ')
p(' ***   ***   ***   ***                    ***   ****** ************    ')
p(' *********************                    ***   ****** ********  **    ')
p(' ****  ***************                    ************ ********  **    ')
p(' ****  ***************                    *********  * ********  **    ')
p(' *********************                    ************ ************    ')
p('***   ***   ***   ***   ***   ***   ***   ***   ***   ***   ***  ***   ')
p('********************************************************************   ')
p('********************************************************************   ')
p('********************************************************************   ')
p('*********                               ****************************   ')
p('*********    The Castle of Mystery!!!   ****************************   ')
p('*********                               ****************************   ')
p('*********                               ****************************   ')
p('************************************************ --------- *********   ')
p('************************************************|    |    |*********   ')
p('****     A text adventure     ******************|    |    |*********   ')
p('****       by The Daddy       ******************|  o | o  |*********   ')
p('************************************************|    |    |*********   ')
p('************************************************|___ |____|*********   ')
p(n = 3)

# main
# name = raw_input('enter your name: ')
name = 'Flibbity Poopety'
p(n = 3)
p('Welcome to the Castle of Mystery, ' + name + '!!', 2)
Entrance()
sys.exit()
