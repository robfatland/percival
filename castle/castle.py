# Planning...
# Entrance 
#  |
#  |
# Foyer - Library - Ledge - Drainpipe - Battlements - Trebuchet - Wall - Tower - Belfry - Dumb Waiter - Pantry - Kitchen - Pens
#  |
#  |
# Hall - { Ballroom, Archery Range, -- Triple -- { Alcove / Lab / Shop } }
#  |
#  |
# Armory - Range (Archery)
#  |
#  |
# Forge
#  |
#  |
# Loading Dock
#  |
#  | 
# Kitchen -- Pantry, Scullery (dishes), Dining, { Pens to Garden }
#  | 
#  | 
# Cellar -- Dungeon
#
#
#
# To pass Ledge need Goatmeal so all the way to the Kitchen
# To pass Drainpipe need Ballroom Chandelier grappling hook, arrive Battlements
#   To get Chandelier (Ballroom) need Axe from Armory
#     To get into the Armory from the Hall need X from Alcove triple: Alcove, Laboratory, Shop
#
# Birds? Bats? 
# 

import location
from rooms import *
from util import *

##########################
##########################
#####
#####     Room template
#####
##########################
##########################

# Boolean state variables up at the top
RoomState1 = False
RoomState2 = False
RoomState3 = False

# Room suggestions
suggRoomFalseFalseFalse = ['sugg', 'string', 'list']
suggRoomFalseFalseTrue  = ['sugg', 'string', 'list']
suggRoomFalseTrueFalse = ['sugg', 'string', 'list']
suggRoomFalseTrueTrue  = ['sugg', 'string', 'list']
suggRoomTrueFalseFalse = ['sugg', 'string', 'list']
suggRoomTrueFalseTrue  = ['sugg', 'string', 'list']
suggRoomTrueTrueFalse = ['sugg', 'string', 'list']
suggRoomTrueTrueTrue  = ['sugg', 'string', 'list']


# Global state variables
suggestionsOn = False
inventory = ['torch', 'sword', 'biscuit', 'match']


# Room states
foyerAsleep = False

libraryPile = False
libraryFire = False

ledgeGoatmeal = False



# Suggestions
suggEntrance = ['light my torch with my last match',\
                'run back down the path I came here on',\
                'knock on the front door',\
                'try to open the front door',\
                'wait for something to happen']


suggFoyerAsleep = ['take a nap', 'go up the stairs', 'go back outside', \
                         'go through the doors', 'tickle the spider']
suggFoyerAwake = ['I could attack the spider...', \
                        'Maybe I should run back outside in terror',\
                        'I could run forward to give ths spider a big kiss', \
                        'Maybe I should just wait and see what happens...']

suggLibraryPileFire = ['The pile of books tops out by the window...', 'the fire is nice and warm...', 'the books could be interesting...']
suggLibraryPileNoFire = ['The pile of books tops out by the window...', 'It is rather chilly... a fire would be nice', 'the books could be interesting...']
suggLibraryNoPileFire = ['the window is too high up to conveniently reach...', '', 'the books could be interesting...']
suggLibraryNoPileNoFire = ['the window is too high up to conveniently reach...', 'I could read some books','I could search the shelves for interesting clues',\
                           'I could try out my Hermione impersonation','I could light a book on fire...',\
                           'no Librarians... this is my chance to talk really really loud!!']

suggLedgeGoatmeal = ['that drainpipe looks climbable...']
suggLedgeNoGoatmeal = ['that drainpipe is just across this loose crumbly masonry... hmmm...', 'I feel a bit hungry']

suggHall = ['x', 'y', 'z']


# methods


# Entrance: Foyer
def Entrance():
    while True:

        promptEntrance = 'You are outside an old castle. It looks very creepy.\n' + \
                         'There are bats flying here and there in the late dusk.\n' + \
                         'There is a lone light shining from one window at the top tower.\n'
 
        PrintInventory(inventory)

        a = WhatDoYouDo(promptEntrance, suggEntrance, suggestionsOn, inventory)

        if BasicParse(a) != 'nothing': pass
        elif 'match' in a or ('light' in a and 'torch' in a):
            if 'match' in inventory:
                p('A bat flies by and the wind from its wings puts out your match before you can light your torch! Oh no!', 2)
                inventory.remove('match')
                inventory.append('burnt match')
            else:
                p("You actually don't have a match for some reason... maybe you already used it?", 2)
        elif ('go' in a or 'walk' in a or 'run' in a) and 'path' in a:
            p('You head back down the path into the forest where you are devoured by wolves. You lose! Sorry...', 2)
            Quit()
        elif 'door' in a or 'knock' in a or 'foyer' in a:
            p('As you touch the door it easily swings open with a creak... it was not fastened.', 2)
            Foyer()
        elif 'wait' in a:
            p('The night deepens.  Off in the distance a wolf howls in the forest. The wolf sounds hungry.', 2)
        elif 'biscuit' in a: 
            p("You eat some of the biscuit but as you're rather full you save some for later.", 2)
        elif 'destroy' in a and 'castle' in a:
            Clarify('destroy the castle')
        elif 'kitchen' in a:
            rooms.Kitchen()
        else: sorry()
    
    return


# Foyer: Hall, Library, Entrance
def Foyer():

    global foyerAsleep

    p(n = 2)
    p('This is the foyer, a chamber filled with gigantic decorative stuffed spiders.')

    firstTimeWithAwake = True
    firstTimeWithAsleep = True

    while True:
        if foyerAsleep:

            if firstTimeWithAsleep:
                msg = 'There is one fat snoring real spider here who gently burps biscuit odors.\n' + \
                      'There is a staircase here leading up to the left and a set of double doors leading inwards.'
                firstTimeWithAsleep = False
            else:
                msg = 'The foyer. There is a snoring spider, a staircase going up to the left, double doors leading inwards.'

            a = WhatDoYouDo(msg, suggFoyerAsleep, suggestionsOn, inventory)

            if BasicParse(a) != 'nothing': pass
            elif 'nap' in a:
                p('Child Services sees you napping and takes you off to Juvie. You lose.', 3) 
                Quit()
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
            else: sorry()

        else:
            if firstTimeWithAwake:
                msg = '...at least you assume they are all stuffed. Suddenly one of them moves, though!\n' + \
                      'It is clambering down the wall and advancing towards you in that creepy spider way.\n' + \
                      'It looks like it means business! It is hissing and singing a song about eating you!'
                firstTimeWithAwake = False
            else:
                msg = 'The foyer. A menacing spider is attacking you!!'

            a = WhatDoYouDo(msg, suggFoyerAwake, suggestionsOn, inventory)

            if BasicParse(a) != 'nothing': pass
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
                foyerAsleep = True
                inventory.remove('biscuit')
            elif 'kiss' in a or 'lips' in a:  
                p('The spider bites you on your outstretched lips... you fall asleep for the remainder of the game.', 3)
                Quit()
            elif 'wait' in a: 
                p('The spider bites you on your lazy bumpkin... you fall asleep for the remainder of the game.', 3)
                Quit()
            else: sorry()
    return


# Library: LibraryLedge, Foyer, ClockRoom (fireplace affects FrozenRoom)
def Library():

    global libraryPile 
    global libraryFire 

    while True:
        p('The Library. There are hundreds of books here... maybe thousands.')
        if libraryPile:
            if libraryFire:
                msg = 'There are stairs going down, a big pile of books under a high window, a door, and a fireplace with a fire in it.'
                a = WhatDoYouDo(msg, suggLibraryPileFire, suggestionsOn, inventory)
                if BasicParse(a) != 'nothing': pass
                elif 'stair' in a or 'stairs' in a or 'down' in a or 'foyer' in a or 'staircase' in a: 
                    Foyer()
                elif 'pile' in a or 'climb' in a or 'books' in a or 'up' in a or 'ledge' in a or 'window' in a: 
                    Ledge()
                else: sorry()
            else:
                msg = 'There are stairs going down, a big pile of books under a high window, a door, and a fireplace but no fire.'
                a = WhatDoYouDo(msg, suggLibraryPileNoFire, suggestionsOn, inventory)
                if BasicParse(a) != 'nothing': pass
                elif 'stair' in a or 'stairs' in a or 'down' in a or 'foyer' in a or 'staircase' in a: 
                    Foyer()
                elif 'pile' in a or 'climb' in a or 'books' in a or 'up' in a or 'ledge' in a or 'window' in a: 
                    Ledge()
                else: sorry()
        else:
            if libraryFire:
                msg = 'There are stairs leading down, a high window, a door, and a fireplace with a fire in it.'
                a = WhatDoYouDo(msg, suggLibraryNoPileFire, suggestionsOn, inventory)
                if BasicParse(a) != 'nothing': pass
                elif 'stair' in a or 'stairs' in a or 'down' in a or 'foyer' in a or 'staircase' in a: 
                    Foyer()
                elif ('pile' in a or 'stack' in a) and 'books' in a:
                    p("You make an enormous pile of books against the wall under the window. Looks like you could climb it.", 2)
                    libraryPile = True
                else: sorry()
            else:
                msg = 'There are stairs leading down, a high window, a door, and a fireplace but no fire.'
                a = WhatDoYouDo(msg, suggLibraryNoPileNoFire, suggestionsOn, inventory)
                if BasicParse(a) != 'nothing': pass
                elif 'stair' in a or 'stairs' in a or 'down' in a or 'foyer' in a or 'staircase' in a: 
                    Foyer()
                elif ('piling' in a or 'pile' in a or 'stack' in a) and 'books' in a:
                    p("You make an enormous pile of books against the wall under the window. Looks like you could climb it.", 2)
                    libraryPile = True
                else: sorry()
    return


def Ledge():

    global ledgeGoatmeal

    while True: 
        if not ledgeGoatmeal:
            msg = 'You are on a window ledge outside the Library above an 80 foot drop. There is a drainpipe here and some loose masonry.'
            a = WhatDoYouDo(msg, suggLedgeNoGoatmeal, suggestionsOn, inventory)
            if BasicParse(a) != 'nothing': pass
            elif 'goatmeal' in a:
                if 'goatmeal' in inventory:
                    ledgeGoatmeal = True
                    p("You plaster some of that goatmeal into the masonry... it seems to set almost instantly. Good thing you didn't eat any of it!", 2)
                else:
                    p("You don't have any goatmeal handy I'm afraid.", 2)
            elif 'walk' in a or 'drainpipe' in a or 'climb' in a:
                p('You walk carefully along the ledge but that loose masonry fails and you plummet 80 feet to your doom.', 3)
                Quit()
            else: sorry()
        else:
            msg = 'You are on a window ledge outside the Library above an 80 foot drop. There is a drainpipe here and some goatmeal-solid masonry.'
            a = WhatDoYouDo(msg, suggLedgeGoatmeal, suggestionsOn, inventory)
            if BasicParse(a) != 'nothing': pass
            elif 'goatmeal' in a:
                p('Yes indeed, that goatmeal sure is holding that formerly loose masonry together well!', 2)
            elif 'walk' in a or 'climb' in a or 'drainpipe' in a:
                p('You walk carefully along the ledge and begin climbing the drainpipe! Yikes!!!', 2)
                Drainpipe()
    return

def Drainpipe():
    while True:
        msg = 'You are at the top of the drainpipe. There is a parapet here 200 feet above the ground. You win!'
        Quit()
    return

def ClockRoom():
    msg = 'You are in a dark room illuminated only by the glowing faces of many many clocks.'
    suggClockRoom = 'ClockRoom suggestions'
    a = WhatDoYouDo(msg, suggClockRoom, suggestionsOn, inventory)
    if BasicParse(a) != 'nothing': pass
    else: sorry()
    return

def FrozenRoom():
    msg = 'You are in a room filled with ice: Ice over chairs, over tables, across the floor, around the coatracks and sideboard...\n' + \
          'It fills the other half of the room, though through the ice you seem to make out a door and some brickwork, \n' + \
	  'perhaps part of a chimney. The only thing not frozen in this room is you and a small torn piece of paper \n' + \
	  'pinned to the wall that reads "Alwaysbean"'
    suggFrozenRoom = 'FrozenRoom suggestions'
    a = WhatDoYouDo(msg, suggFrozenRoom, suggestionsOn, inventory)
    if BasicParse(a) != 'nothing': pass
    else: sorry()
    return

def Hall():
    while True:
        msg = 'This is the main hall. Double doors behind you lead to the foyer.\n' + \
              'A curtain to your right seems to cover a passage. An ornate door is ahead and to your left.\n' + \
              'There are two doors between the curtain and the ornate door: One is metal, the other is made of wood.\n'
        a = WhatDoYouDo(msg, suggHall, suggestionsOn, inventory)
        if BasicParse(a) != 'nothing': pass
        elif 'ornate' in a:
            Ballroom()
        elif 'double' in a or 'foyer' in a:
            Foyer()
        elif 'curtain' in a:
            Alcove()
        elif 'metal' in a:
            Armory()
        elif 'wood' in a:
            Range()
        else: sorry()
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
Quit()
