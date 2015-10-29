# Here are all the rooms
entrance = location('entrance', 'the front entrance to the cold stone creepy castle', 1) 
foyer = room('foyer', 'the small chamber past the front entrance', 1)
library = room('library', 'a room full of mysterious books and a fireplace', 1)
ledge = location('ledge', 'a ledge outside the library window near a drainpipe', 1)
drainpipe = location('drainpipe', 'a vertical pipe from the ledge up to the roof', 1)
battlements = location('battlements', 'the broad roof of the castle with a parapet', 1)
trebuchet = location('trebuchet', 'a trebuchet with several large stones stacked nearby', 1)
wall = location('wall', 'a wall between the battlements and the large tower', 1)
tower = room('tower', 'the highest tower of the castle', 1)
belfry = room('belfry', 'the room at the top of the tower', 1)
dumbwaiter = location('dumbwaiter', 'a hand-operated elevator the size of a suitcase', 1)
pantry = room('pantry', 'a place where squash is stored prior to over-cooking', 1)
scullery = room('scullery', 'many sinks and scrubbers for making dishes clean', 1)
kitchen = room('kitchen', 'a place where squash is over-cooked', 1.0)
laundry = room('laundry','a place where clothes are not washed very well', 1.0)
coalscuttle = room('coal scuttle','little more than a large bin with a few chunks of coal down in one corner', 1.0)
dining = room('dining room', 'a large room with an enormous table', 1)
lodgings = location('lodgings', 'a series of bedrooms and hallways; nothing very interesting, very dark', 1)
pens = location('pens', 'there is a pig here... It appears to be made of oinkment', 1)
garden = location('garden', 'the place where they grow all the squash.', 1)
hall = room('great hall', 'a large opulent room with great chandeliers, mirrors and portraits', 1)
ballroom = room('ballroom', 'a place to dance... well actually you can dance anywhere', 1)
alcove = room('alcove', 'a little room for putting on boots or reading instead of going to bed', 1)
lab = room('laboratory', 'a room with benches and pipes and bottles and foul chemicals', 1)
shop = room('shop', 'a room for building little devices of wood, metal and glass', 1)
armory = room('armory', 'where weapons like swords and bows and arrows are stored', 1)
archeryrange = room('archery range', 'a place to shoot arrows at targets', 1)
forge = room('forge', 'a room for pounding metal into shapes like swords and armor', 1)
loadingdock = room('loading dock', 'a kind of platform where macroinvertebrates abound', 1.0)
cellar = room('cellar', 'filled with wine bottles and stacks of carpets', 1.0)
dungeon = room('dungeon', 'filthy and filled with sounds: distant howls, screams, and rattling chains...', 1.0) 



# Kitchen 
def Kitchen():

    if kitchen.state[0] and kitchen.state[1] and kitchen.state[2]:
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

    return




