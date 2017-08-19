
def shire():
    action = raw_input("Your journey begins at the Shire however there is evil afoot! Type GO to escape with the ring to the Ford of Burien! ")
    if action == "GO":
        ford()
    else:
        print '''
        Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        shire()
        
def ford():
    action = raw_input('''
Head toward the Ford of Burien once you escape the Shire, but hurry! The Ring Wraiths are close on your trail! 
    Type SWIM if you wish to swim across the water 
    Type FERRY to cross the water on a ferry
    ''')
    if action == "SWIM":
        print '''
You drowned. Back to the Ford you go!
        '''
        ford()
    elif action == "FERRY":
        print '''
You made it across to Bree and escaped the Ring Wraiths
'''
        inn()
    else:
        print '''
Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        shire()

def inn():
    action = raw_input('''Once in Bree, head to the Prancing Pony Inn where you will meet with Strider aka Aragorn
    Type STAY if you plan on staying at the Prancing Pony Inn in the lovely village of Bree that night
    Type ESCAPE if you choose to follow Strider's instruction to escape the sneak attack of the Ring Wraiths
    ''')
    if action == "STAY":
        print '''
You are stabbed brutally to death in your slumber. Go back to the Inn.
        '''
        inn()
    elif action == "ESCAPE":
        print '''
Made it to Weathertop with Strider ahead of Ring Wraiths!
        '''
        weathertop()
    else:
        print '''
Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        shire()

def weathertop():
    action = raw_input('''You made it to Weathertop with Strider, but the enemy has caught up with you!
    Type OUTRUN if you are going to try to OUTRUN the Ring Wraiths
    Type FIGHT if you choose to follow Strider's instruction to escape the sneak attack of the Ring Wraiths
    ''')
    if action == "OUTRUN":
        print '''
Not so fast! The enemy is faster. You die, back to the Prancing Pony Inn you go!
        '''
        weathertop()
    elif action == "FIGHT":
        print '''
A ring wraith stabbed you with its poisonous sword, but lucky you, Arwen of Rivendell is there to save you and take you to Rivendell.
        '''
        rivendell()
    else:
        print '''
Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        shire()


def rivendell():
    action = raw_input('''When you wake up in Rivendell after healing from your wound with the power of Elvish medicine, you join in on 
the Counsil of Elrond. This is where the Fellowship of the Ring is formed in order to travel to Mordor to destroy the one ring that rules all.
    Type FELLOWSHIP if you choose to leave the ring in the trusted hands of the Fellowship.
    Type CARRY if you feel the weight and responsibility to carry the ring to Mordor yourself.
    Type BACK if you choose to abandon the quest and go home to the Shire.
    ''')
    if action == "FELLOWSHIP":
        print '''
Whoops! they lost it the moment they walked out the gates. Start over at Rivendell at the Counsil of Elrond.
        '''
        rivendell()
    elif action == "CARRY":
        print '''
You will take the ring to mordor yourself, afterall you can't trust nobody! Off on your quest to Mordor, first stop, Moria
        '''
        moria()
    elif action == "BACK":
        print '''
Peace! back to the Shire for you. Screw all these crazies.
        '''
        shire()
    else:
        print '''
Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        shire()


def moria():
    action = raw_input('''You and the rest of the Fellowship take off for the cames of Moria. your sword from Bilbo starts glowing a brilliant blue! 
A massive Orc army is swarming the caves headed towards you!
    Type RUN to run for your life towards the exit of the cave
    Type BATTLE to try to fight through the orcs and troll
    ''')
    if action == "RUN":
        print '''
Oh no! Wrong turn! You are cornered and killed by the troll. Go back towards the entrance.
        '''
        moria()
    elif action == "BATTLE":
        print '''
You made it! Although Gandalf falls into the shadow after battling the fire demon Balrog, your journey continues!
        '''
        gollum()
    else:
        print '''Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        rivendell()


def gollum():
    action = raw_input('''As your journey continues, you and Sam separate from the rest of the fellowship. Once off by yourselves, you notice someone or 
something following you...You catch Gollum! As your prisoner, you force him to show you the way to Mordor. He takes you to this secret passage way through
a tunnel. But Gollum disappears once you step into that secret tunnel. As you work your way through the cobwebs, you hear something moving in the dark corner...
Quick! Shelob the (huge ass) spider is after you! You almost make it out until Gollum reappears and attacks you trying to get the ring. Trusted friend Sam 
knocked off Gollum and was able to fight off Shelob back into the cave. But it was a moment too late, you were stung. Hearing orcs approaching and thinking
you were as dead as a doornail, Sam takes the ring and...
    Type KEEP if you believe Sam keeps the ring for himself.
    Type FOLLOW if you think Sam will follow the orcs (that have taken your body) up to Mordor.
    ''')
    if action == "KEEP":
        print '''
With the ring, Sam becomes the most powerful hobbit ever to walk middle earth. Try again at the beginning of the cave.
        '''
        gollum()
    elif action == "FOLLOW":
        print '''
Sam overhears the orcs saying you are only paralyzed (whew!) so Sam follows you and the two orcs up to Mordor. 
        '''
        mordor()
    else:
        print '''Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        rivendell()



def mordor():
    action = raw_input('''Being wrapped up in all that webbing from Shelob, Sam had to cut you free when the orcs were distracted. Now, the question is, how 
will you get through the long, tough and dangerous path towards Mt. Doom?
    Type WING IT it you are just going to go for it and sneak through in the shadows
    Type DISGUISE, you and Sam found orcish armor! Will you chance walking through Mordor in the open with the disguise on?
    ''')
    if action == "WING IT":
        print '''
Nope. With the thousands of orcs about, you are immediatly recognized. Start over at the beginning of Mordor.
        '''
        mordor()
    elif action == "DISGUISE":
        print '''
Orcs are idiots and didn't recognize you, of course you made it through to Mt. Doom!
        '''
        doom()
    else:
        print '''Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        rivendell()



def doom():
    action = raw_input('''You collapse on the journey up Mt. Doom due to the stron, powerful hold the ring has over you. But loyal Sam carries you almost the 
rest of the way up to the crack of doom. Nearly at the end that damn Gollum sneaks up and attacks again. Out of fear of losing the ring you start running towards
the firey pits of Mt. Doom as Sam stabs Gollum. You finally make it to the end, now all you need to do is throw the ring into the fire...
    Type POWER if you choose to embrace the power of the ring and use that power for good rather than evil.
    Type FREE if you wish to finish the long quest of destroying the ring that you originally set out to accomplish.
    ''')
    if action == "POWER":
        print '''
You believed wrong. It isn't possible to use that ring for good, it is the most powerful ring that anybody would eventually succumb to its evil power.
        '''
        doom()
    elif action == "FREE":
        print '''
YOU DID IT!!!! The enemy Sauron and the ring have been destroyed! 
        '''
        end()
    else:
        print '''Maybe a change of mind? Go on, run back to the Shire...
        
        '''
        rivendell()


def end():
    action = raw_input('''You have completed the Quest of the Ring, the Journey of Frodo Baggins. Now its time to go back to the Shire to your comfortable hobbit hole where everething is peaceful and quiet and HOME.
    
    Type START OVER if you wish to start the game from the beginning.
    ''')
    if action == "START OVER":
        shire()







        
print '''
It began with the forging of the Great Rings. Three were given to the Elves, immortal, wisest and fairest of all beings. Seven to the Dwarf-Lords, 
great miners and craftsmen of the mountain halls. And nine, nine rings were gifted to the race of Men, who above all else desire power. For within these 
rings was bound the strength and the will to govern each race. But they were all of them deceived, for another ring was made. Deep in the land of Mordor, 
in the Fires of Mount Doom, the Dark Lord Sauron forged a master ring in secret, and into this ring he poured his cruelty, his malice and his will to 
dominate all life. One ring to rule them all.


You have been chosen to take the journey to the depths of Mordor to destroy the ring of power. Beware, do not succumb to its temptation of greed and power 
for it in turn will destroy you.
'''
shire()

        