
from location import *
from util import *

# room Laundry('Laundry','A place where clothes are not washed.', [True, True, True])


KitchenState1 = True
KitchenState2 = True
KitchenState3 = True

BallroomState1 = True
BallroomState2 = True
BallroomState3 = True

DiningState1 = True
DiningState2 = True
DiningState3 = True

AlcoveState1 = True
AlcoveState2 = True
AlcoveState3 = True

LabState1 = True
LabState2 = True
LabState3 = True

ShopState1 = True
ShopState2 = True
ShopState3 = True

ArmoryState1 = True
ArmoryState2 = True
ArmoryState3 = True

RangeState1 = True
RangeState2 = True
RangeState3 = True

SculleryState1 = True
SculleryState2 = True
SculleryState3 = True

suggBallroomFalseFalseFalse = ['sugg', 'string', 'list']
suggBallroomFalseFalseTrue  = ['sugg', 'string', 'list']
suggBallroomFalseTrueFalse = ['sugg', 'string', 'list']
suggBallroomFalseTrueTrue  = ['sugg', 'string', 'list']
suggBallroomTrueFalseFalse = ['sugg', 'string', 'list']
suggBallroomTrueFalseTrue  = ['sugg', 'string', 'list']
suggBallroomTrueTrueFalse = ['sugg', 'string', 'list']
suggBallroomTrueTrueTrue  = ['sugg', 'string', 'list']

suggDiningFalseFalseFalse = ['sugg', 'string', 'list']
suggDiningFalseFalseTrue  = ['sugg', 'string', 'list']
suggDiningFalseTrueFalse = ['sugg', 'string', 'list']
suggDiningFalseTrueTrue  = ['sugg', 'string', 'list']
suggDiningTrueFalseFalse = ['sugg', 'string', 'list']
suggDiningTrueFalseTrue  = ['sugg', 'string', 'list']
suggDiningTrueTrueFalse = ['sugg', 'string', 'list']
suggDiningTrueTrueTrue  = ['sugg', 'string', 'list']

suggKitchenFalseFalseFalse = ['sugg', 'string', 'list']
suggKitchenFalseFalseTrue  = ['sugg', 'string', 'list']
suggKitchenFalseTrueFalse = ['sugg', 'string', 'list']
suggKitchenFalseTrueTrue  = ['sugg', 'string', 'list']
suggKitchenTrueFalseFalse = ['sugg', 'string', 'list']
suggKitchenTrueFalseTrue  = ['sugg', 'string', 'list']
suggKitchenTrueTrueFalse = ['sugg', 'string', 'list']
suggKitchenTrueTrueTrue  = ['sugg', 'string', 'list']

suggPantryFalseFalseFalse = ['sugg', 'string', 'list']
suggPantryFalseFalseTrue  = ['sugg', 'string', 'list']
suggPantryFalseTrueFalse = ['sugg', 'string', 'list']
suggPantryFalseTrueTrue  = ['sugg', 'string', 'list']
suggPantryTrueFalseFalse = ['sugg', 'string', 'list']
suggPantryTrueFalseTrue  = ['sugg', 'string', 'list']
suggPantryTrueTrueFalse = ['sugg', 'string', 'list']
suggPantryTrueTrueTrue  = ['sugg', 'string', 'list']

suggCellarFalseFalseFalse = ['sugg', 'string', 'list']
suggCellarFalseFalseTrue  = ['sugg', 'string', 'list']
suggCellarFalseTrueFalse = ['sugg', 'string', 'list']
suggCellarFalseTrueTrue  = ['sugg', 'string', 'list']
suggCellarTrueFalseFalse = ['sugg', 'string', 'list']
suggCellarTrueFalseTrue  = ['sugg', 'string', 'list']
suggCellarTrueTrueFalse = ['sugg', 'string', 'list']
suggCellarTrueTrueTrue  = ['sugg', 'string', 'list']

suggDungeonFalseFalseFalse = ['sugg', 'string', 'list']
suggDungeonFalseFalseTrue  = ['sugg', 'string', 'list']
suggDungeonFalseTrueFalse = ['sugg', 'string', 'list']
suggDungeonFalseTrueTrue  = ['sugg', 'string', 'list']
suggDungeonTrueFalseFalse = ['sugg', 'string', 'list']
suggDungeonTrueFalseTrue  = ['sugg', 'string', 'list']
suggDungeonTrueTrueFalse = ['sugg', 'string', 'list']
suggDungeonTrueTrueTrue  = ['sugg', 'string', 'list']

suggLoadingFalseFalseFalse = ['sugg', 'string', 'list']
suggLoadingFalseFalseTrue  = ['sugg', 'string', 'list']
suggLoadingFalseTrueFalse = ['sugg', 'string', 'list']
suggLoadingFalseTrueTrue  = ['sugg', 'string', 'list']
suggLoadingTrueFalseFalse = ['sugg', 'string', 'list']
suggLoadingTrueFalseTrue  = ['sugg', 'string', 'list']
suggLoadingTrueTrueFalse = ['sugg', 'string', 'list']
suggLoadingTrueTrueTrue  = ['sugg', 'string', 'list']


# Kitchen 
def Kitchen():

    global KitchenState1
    global KitchenState2
    global KitchenState3

    while True:
        if KitchenState1:
            if KitchenState2:
                if KitchenState3:
                    msg = 'You are in a kitchen. There is a pot of goatmeal on the stove; it looks very unctuous.\n' + \
                          'Doors to the pantry, scullery, dining room and loading dock; as well as a trap door in the floor. \n' + \
                          'There is also a short hall leading to a door to the outside and down some steps to the animal pens.\n'
                    a = WhatDoYouDo(msg, suggKitchenTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'eat' in a and 'goatmeal' in a: 
                        p("Well all you can say is 'bleccchhhh'... it tastes like wet cement.")
                        p("Although how do you know what wet cement tastes like??")
                        p("Anyway at least it seems to be authentic goatmeal made from real goats.", 2)
                    elif ('get' in a or 'take' in a) and 'goatmeal' in a:
                        print 'You put some goatmeal in a bowl and bring it with you for some strange reason.'
                        inventory.append('goatmeal')
                    elif 'dining' in a:
                        Dining()
                    elif 'pantry' in a:
                        Pantry()
                    elif 'scullery' in a:
                        Scullery()
                    elif 'trap' in a:
                        Cellar()
                    elif 'pen' in a or 'pens' in a:
                        Pens()
                    elif 'loading' in a or 'dock' in a or 'docks' in a:
                        Loading()
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggKitchen = ['Kitchen suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggKitchenTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if KitchenState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggKitchen = ['Kitchen suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggKitchenTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggKitchen = ['Kitchen suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggKitchenTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if KitchenState2:
                if KitchenState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggKitchen = ['Kitchen suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggKitchenFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggKitchen = ['Kitchen suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggKitchenFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if KitchenState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggKitchen = ['Kitchen suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggKitchenFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggKitchen = ['Kitchen suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggKitchenFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return




# Alcove 
def Alcove():

    global AlcoveState1
    global AlcoveState2
    global AlcoveState3

    while True:
        if AlcoveState1:
            if AlcoveState2:
                if AlcoveState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggAlcoveTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggAlcove = ['Alcove suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggAlcoveTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if AlcoveState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggAlcove = ['Alcove suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggAlcoveTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggAlcove = ['Alcove suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggAlcoveTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if AlcoveState2:
                if AlcoveState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggAlcove = ['Alcove suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggAlcoveFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggAlcove = ['Alcove suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggAlcoveFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if AlcoveState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggAlcove = ['Alcove suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggAlcoveFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggAlcove = ['Alcove suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggAlcoveFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Lab 
def Lab():

    global LabState1
    global LabState2
    global LabState3

    while True:
        if LabState1:
            if LabState2:
                if LabState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggLabTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggLab = ['Lab suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLabTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if LabState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggLab = ['Lab suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLabTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggLab = ['Lab suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLabTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if LabState2:
                if LabState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggLab = ['Lab suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLabFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggLab = ['Lab suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLabFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if LabState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggLab = ['Lab suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLabFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggLab = ['Lab suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLabFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Shop 
def Shop():

    global ShopState1
    global ShopState2
    global ShopState3

    while True:
        if ShopState1:
            if ShopState2:
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggShopTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if ShopState2:
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Shop 
def Shop():

    global ShopState1
    global ShopState2
    global ShopState3

    while True:
        if ShopState1:
            if ShopState2:
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggShopTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if ShopState2:
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ShopState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggShop = ['Shop suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggShopFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Armory 
def Armory():

    global ArmoryState1
    global ArmoryState2
    global ArmoryState3

    while True:
        if ArmoryState1:
            if ArmoryState2:
                if ArmoryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggArmoryTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggArmory = ['Armory suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggArmoryTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ArmoryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggArmory = ['Armory suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggArmoryTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggArmory = ['Armory suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggArmoryTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if ArmoryState2:
                if ArmoryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggArmory = ['Armory suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggArmoryFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggArmory = ['Armory suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggArmoryFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ArmoryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggArmory = ['Armory suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggArmoryFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggArmory = ['Armory suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggArmoryFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Range 
def Range():

    global RangeState1
    global RangeState2
    global RangeState3

    while True:
        if RangeState1:
            if RangeState2:
                if RangeState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggRangeTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggRange = ['Range suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRangeTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if RangeState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggRange = ['Range suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRangeTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggRange = ['Range suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRangeTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if RangeState2:
                if RangeState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggRange = ['Range suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRangeFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggRange = ['Range suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRangeFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if RangeState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggRange = ['Range suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRangeFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggRange = ['Range suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRangeFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return


# Ballroom 
def Ballroom():

    global BallroomState1
    global BallroomState2
    global BallroomState3

    while True:
        if BallroomState1:
            if BallroomState2:
                if BallroomState3:
                    msg = 'The ballroom... an ornate door and a large open passage to the dining room.'
                    a = WhatDoYouDo(msg, suggBallroomTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'passage' in a: 
                        Dining()
                    elif 'ornate' in a:
                        Hall()
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggBallroom = ['Ballroom suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBallroomTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if BallroomState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggBallroom = ['Ballroom suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBallroomTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggBallroom = ['Ballroom suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBallroomTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if BallroomState2:
                if BallroomState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggBallroom = ['Ballroom suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBallroomFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggBallroom = ['Ballroom suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBallroomFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if BallroomState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggBallroom = ['Ballroom suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBallroomFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggBallroom = ['Ballroom suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBallroomFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Dining 
def Dining():

    global DiningState1
    global DiningState2
    global DiningState3

    while True:
        if DiningState1:
            if DiningState2:
                if DiningState3:
                    msg = 'The dining room. There are swinging double doors and an open passage to the ballroom.'
                    a = WhatDoYouDo(msg, suggDiningTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'swinging' in a or 'double' in a or 'doors' in a: 
                        rooms.Kitchen()
                    elif 'passage' in a or 'ballroom' in a:
                        Ballroom()
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggDining = ['Dining suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDiningTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if DiningState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggDining = ['Dining suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDiningTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggDining = ['Dining suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDiningTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if DiningState2:
                if DiningState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggDining = ['Dining suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDiningFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggDining = ['Dining suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDiningFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if DiningState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggDining = ['Dining suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDiningFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggDining = ['Dining suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDiningFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Forge 
def Forge():

    global ForgeState1
    global ForgeState2
    global ForgeState3

    while True:
        if ForgeState1:
            if ForgeState2:
                if ForgeState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggForgeTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggForge = ['Forge suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggForgeTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ForgeState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggForge = ['Forge suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggForgeTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggForge = ['Forge suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggForgeTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if ForgeState2:
                if ForgeState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggForge = ['Forge suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggForgeFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggForge = ['Forge suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggForgeFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if ForgeState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggForge = ['Forge suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggForgeFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggForge = ['Forge suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggForgeFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Coal 
def Coal():

    global CoalState1
    global CoalState2
    global CoalState3

    while True:
        if CoalState1:
            if CoalState2:
                if CoalState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggCoalTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggCoal = ['Coal suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCoalTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if CoalState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggCoal = ['Coal suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCoalTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggCoal = ['Coal suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCoalTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if CoalState2:
                if CoalState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggCoal = ['Coal suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCoalFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggCoal = ['Coal suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCoalFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if CoalState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggCoal = ['Coal suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCoalFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggCoal = ['Coal suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCoalFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Loading 
def Loading():

    global LoadingState1
    global LoadingState2
    global LoadingState3

    while True:
        if LoadingState1:
            if LoadingState2:
                if LoadingState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggLoadingTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggLoading = ['Loading suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLoadingTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if LoadingState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggLoading = ['Loading suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLoadingTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggLoading = ['Loading suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLoadingTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if LoadingState2:
                if LoadingState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggLoading = ['Loading suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLoadingFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggLoading = ['Loading suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLoadingFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if LoadingState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggLoading = ['Loading suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLoadingFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggLoading = ['Loading suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggLoadingFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Battlements 
def Battlements():

    global BattlementsState1
    global BattlementsState2
    global BattlementsState3

    while True:
        if BattlementsState1:
            if BattlementsState2:
                if BattlementsState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggBattlementsTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggBattlements = ['Battlements suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBattlementsTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if BattlementsState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggBattlements = ['Battlements suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBattlementsTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggBattlements = ['Battlements suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBattlementsTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if BattlementsState2:
                if BattlementsState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggBattlements = ['Battlements suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBattlementsFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggBattlements = ['Battlements suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBattlementsFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if BattlementsState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggBattlements = ['Battlements suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBattlementsFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggBattlements = ['Battlements suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBattlementsFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Trebuchet 
def Trebuchet():

    global TrebuchetState1
    global TrebuchetState2
    global TrebuchetState3

    while True:
        if TrebuchetState1:
            if TrebuchetState2:
                if TrebuchetState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggTrebuchetTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggTrebuchet = ['Trebuchet suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTrebuchetTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if TrebuchetState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggTrebuchet = ['Trebuchet suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTrebuchetTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggTrebuchet = ['Trebuchet suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTrebuchetTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if TrebuchetState2:
                if TrebuchetState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggTrebuchet = ['Trebuchet suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTrebuchetFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggTrebuchet = ['Trebuchet suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTrebuchetFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if TrebuchetState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggTrebuchet = ['Trebuchet suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTrebuchetFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggTrebuchet = ['Trebuchet suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTrebuchetFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Wall 
def Wall():

    global WallState1
    global WallState2
    global WallState3

    while True:
        if WallState1:
            if WallState2:
                if WallState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggWallTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggWall = ['Wall suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggWallTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if WallState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggWall = ['Wall suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggWallTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggWall = ['Wall suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggWallTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if WallState2:
                if WallState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggWall = ['Wall suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggWallFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggWall = ['Wall suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggWallFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if WallState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggWall = ['Wall suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggWallFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggWall = ['Wall suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggWallFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Tower 
def Tower():

    global TowerState1
    global TowerState2
    global TowerState3

    while True:
        if TowerState1:
            if TowerState2:
                if TowerState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggTowerTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggTower = ['Tower suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTowerTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if TowerState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggTower = ['Tower suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTowerTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggTower = ['Tower suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTowerTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if TowerState2:
                if TowerState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggTower = ['Tower suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTowerFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggTower = ['Tower suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTowerFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if TowerState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggTower = ['Tower suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTowerFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggTower = ['Tower suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggTowerFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Belfry 
def Belfry():

    global BelfryState1
    global BelfryState2
    global BelfryState3

    while True:
        if BelfryState1:
            if BelfryState2:
                if BelfryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggBelfryTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggBelfry = ['Belfry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBelfryTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if BelfryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggBelfry = ['Belfry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBelfryTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggBelfry = ['Belfry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBelfryTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if BelfryState2:
                if BelfryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggBelfry = ['Belfry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBelfryFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggBelfry = ['Belfry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBelfryFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if BelfryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggBelfry = ['Belfry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBelfryFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggBelfry = ['Belfry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggBelfryFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Dumb 
def Dumb():

    global DumbState1
    global DumbState2
    global DumbState3

    while True:
        if DumbState1:
            if DumbState2:
                if DumbState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggDumbTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggDumb = ['Dumb suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDumbTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if DumbState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggDumb = ['Dumb suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDumbTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggDumb = ['Dumb suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDumbTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if DumbState2:
                if DumbState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggDumb = ['Dumb suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDumbFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggDumb = ['Dumb suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDumbFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if DumbState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggDumb = ['Dumb suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDumbFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggDumb = ['Dumb suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDumbFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Pantry 
def Pantry():

    global PantryState1
    global PantryState2
    global PantryState3

    while True:
        if PantryState1:
            if PantryState2:
                if PantryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggPantryTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggPantry = ['Pantry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPantryTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if PantryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggPantry = ['Pantry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPantryTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggPantry = ['Pantry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPantryTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if PantryState2:
                if PantryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggPantry = ['Pantry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPantryFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggPantry = ['Pantry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPantryFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if PantryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggPantry = ['Pantry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPantryFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggPantry = ['Pantry suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPantryFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return


# Pens 
def Pens():

    global PensState1
    global PensState2
    global PensState3

    while True:
        if PensState1:
            if PensState2:
                if PensState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggPensTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggPens = ['Pens suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPensTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if PensState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggPens = ['Pens suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPensTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggPens = ['Pens suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPensTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if PensState2:
                if PensState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggPens = ['Pens suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPensFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggPens = ['Pens suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPensFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if PensState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggPens = ['Pens suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPensFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggPens = ['Pens suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggPensFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Garden 
def Garden():

    global GardenState1
    global GardenState2
    global GardenState3

    while True:
        if GardenState1:
            if GardenState2:
                if GardenState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggGardenTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggGarden = ['Garden suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGardenTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if GardenState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggGarden = ['Garden suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGardenTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggGarden = ['Garden suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGardenTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if GardenState2:
                if GardenState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggGarden = ['Garden suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGardenFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggGarden = ['Garden suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGardenFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if GardenState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggGarden = ['Garden suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGardenFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggGarden = ['Garden suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGardenFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Quarters 
def Quarters():

    global QuartersState1
    global QuartersState2
    global QuartersState3

    while True:
        if QuartersState1:
            if QuartersState2:
                if QuartersState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggQuartersTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggQuarters = ['Quarters suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggQuartersTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if QuartersState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggQuarters = ['Quarters suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggQuartersTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggQuarters = ['Quarters suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggQuartersTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if QuartersState2:
                if QuartersState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggQuarters = ['Quarters suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggQuartersFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggQuarters = ['Quarters suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggQuartersFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if QuartersState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggQuarters = ['Quarters suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggQuartersFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggQuarters = ['Quarters suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggQuartersFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Grand 
def Grand():

    global GrandState1
    global GrandState2
    global GrandState3

    while True:
        if GrandState1:
            if GrandState2:
                if GrandState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggGrandTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggGrand = ['Grand suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGrandTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if GrandState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggGrand = ['Grand suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGrandTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggGrand = ['Grand suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGrandTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if GrandState2:
                if GrandState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggGrand = ['Grand suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGrandFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggGrand = ['Grand suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGrandFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if GrandState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggGrand = ['Grand suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGrandFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggGrand = ['Grand suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggGrandFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Scullery 
def Scullery():

    global SculleryState1
    global SculleryState2
    global SculleryState3

    while True:
        if SculleryState1:
            if SculleryState2:
                if SculleryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggSculleryTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggScullery = ['Scullery suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggSculleryTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if SculleryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggScullery = ['Scullery suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggSculleryTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggScullery = ['Scullery suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggSculleryTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if SculleryState2:
                if SculleryState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggScullery = ['Scullery suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggSculleryFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggScullery = ['Scullery suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggSculleryFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if SculleryState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggScullery = ['Scullery suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggSculleryFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggScullery = ['Scullery suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggSculleryFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Dungeon 
def Dungeon():

    global DungeonState1
    global DungeonState2
    global DungeonState3

    while True:
        if DungeonState1:
            if DungeonState2:
                if DungeonState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggDungeonTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggDungeon = ['Dungeon suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDungeonTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if DungeonState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggDungeon = ['Dungeon suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDungeonTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggDungeon = ['Dungeon suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDungeonTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if DungeonState2:
                if DungeonState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggDungeon = ['Dungeon suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDungeonFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggDungeon = ['Dungeon suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDungeonFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if DungeonState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggDungeon = ['Dungeon suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDungeonFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggDungeon = ['Dungeon suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggDungeonFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

# Cellar 
def Cellar():

    global CellarState1
    global CellarState2
    global CellarState3

    while True:
        if CellarState1:
            if CellarState2:
                if CellarState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggCellarTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggCellar = ['Cellar suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCellarTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if CellarState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggCellar = ['Cellar suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCellarTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggCellar = ['Cellar suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCellarTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if CellarState2:
                if CellarState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggCellar = ['Cellar suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCellarFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggCellar = ['Cellar suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCellarFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if CellarState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggCellar = ['Cellar suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCellarFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggCellar = ['Cellar suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggCellarFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return

















# Room 
def Room():

    global RoomState1
    global RoomState2
    global RoomState3

    while True:
        if RoomState1:
            if RoomState2:
                if RoomState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    a = WhatDoYouDo(msg, suggRoomTrueTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggRoom = ['Room suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRoomTrueTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if RoomState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggRoom = ['Room suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRoomTrueFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggRoom = ['Room suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRoomTrueFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

        else:
            if RoomState2:
                if RoomState3:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 true.'
                    suggRoom = ['Room suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRoomFalseTrueTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 true state 3 false.'
                    suggRoom = ['Room suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRoomFalseTrueFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

            else: 
                if RoomState3:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 true.'
                    suggRoom = ['Room suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRoomFalseFalseTrue)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()

                else:
                    msg = 'You are in a basic room with state 1 true state 2 false state 3 false.'
                    suggRoom = ['Room suggestions', 'as', 'a', 'list', 'of', 'strings']
                    a = WhatDoYouDo(msg, suggRoomFalseFalseFalse)
                    if BasicParse(a) != 'nothing': pass
                    elif 'good idea' in a: pass
                    else: sorry()
    return