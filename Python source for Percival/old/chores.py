



chores = ['feed Maia', 'clean room', 'stow dishes']

print chores

print len(chores)


chores.append('chop wood')

print chores

print len(chores)

happy = False

thisChore = 0

while not happy:
    print 'i am not happy because my chores are not done.'
    print '    now i am doing this:', chores[thisChore]
    thisChore = thisChore + 1
    if thisChore == len(chores): 
        happy = True

print ''
print ''
print 'now i am happy!!! ;)'
 
 
