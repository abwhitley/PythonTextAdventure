# This line needs to be worked on to import the classes
# from Python Practice.Text-Based Adventure import class.py
import random
# Main executable that controls flow
def main():
    userCharacter = chooseYourCharacter()
    print(userCharacter.description)
    insertPrintBreaks()
    doorChosen = chooseADoor()
    firstRoomChosen(doorChosen,userCharacter)

# Function to insert line breaks for easier reading in console
def insertPrintBreaks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Function to choose Character
def chooseYourCharacter():
    insertPrintBreaks()
    print("What class would you like?")
    choice = input("Ranger, Warrior or Wizard?")
    insertPrintBreaks()
    print("You chose ", choice)
    insertPrintBreaks()
    # Connects users choise to the correct class
    if choice == "Ranger":
        userCharacter = Ranger
    elif choice == "Warrior":
        userCharacter = Warrior
    elif choice == "Wizard":
        userCharacter = Wizard
    return userCharacter

def wouldYouLikeToLookAround():
    # originRooms is the class that contains all info for the doors and their descriptions
    entrance = originRooms
    print("You drop into a peculiar room, almost no light but a lone candle`")
    print("Would you like to look around?")
    insertPrintBreaks()
    choice = input("Yes or No")
    if choice == "Yes":
        print(entrance.description)
        insertPrintBreaks()
    elif choice == "No":
        print("Well what else are you going to do?")
        print("Lets look around the room")
        print(entrance.description)
        insertPrintBreaks()

# Origin Room that leads to the door choise 
def chooseADoor():
    wouldYouLikeToLookAround()
    print("Which Door do you want to look at?")
    doorChoice = int(input("1,2 or 3 or 4 for Test Arena?"))
    insertPrintBreaks()
    if doorChoice == 1:
        doorObject = door1
        print(doorObject.description)
        print("Would you like to go through the door?")
        insertPrintBreaks()
        doorChoice1 = input("Yes or No")
        insertPrintBreaks()
        if doorChoice1 == "Yes":
            return doorObject
        elif doorChoice1 == "No":
            print("Okay which door?")
            insertPrintBreaks()
            return chooseADoor()
    elif doorChoice == 2:
        doorObject = door2
        print(doorObject.description)
        print("Would you like to go through the door?")
        insertPrintBreaks()
        doorChoice1 = input("Yes or No")
        if doorChoice1 == "Yes":
            return doorObject
        elif doorChoice1 == "No":
            print("Okay which door?")
            insertPrintBreaks()
            return chooseADoor()
        print(doorObject.description)
    elif doorChoice == 3:
        doorObject = door3
        print(doorObject.description)
        print("Would you like to go through the door?")
        doorChoice1 = input("Yes or No")
        insertPrintBreaks()
        if doorChoice1 == "Yes":
            return doorObject
        elif doorChoice1 == "No":
            print("Okay which door?")
            insertPrintBreaks()
            return chooseADoor()
    elif doorChoice == 4:
        doorObject = TestArena
        return doorObject

# Allow the door chosen to open the correct room and Secret Room
def firstRoomChosen(doorChosen,userCharacter):
    if doorChosen == door1:
        print(door1.room1.description)
        insertPrintBreaks()
        redOrbRoom()
    elif doorChosen == door2:
        print(door2.room2.description)
        insertPrintBreaks()
    elif doorChosen == door3:
        print(door3.room3.description)
        insertPrintBreaks()
    elif doorChosen == TestArena:
        insertPrintBreaks()
        secretArenaRoom(userCharacter)

# 1st door Room
def redOrbRoom():
    redOrb = door1.room1
    print("1:", redOrb.options[0])
    print("2:", redOrb.options[1])
    choice = int(input("1 or 2?"))
    insertPrintBreaks()
    if choice == 1:
        choice1 = orbTaken
        print(choice1.description)
    elif choice == 2:
        choice2 = searchForWayOut
        print(choice2.description)

# using to test combat
# The random number generator is working i just need to parse the day
def secretArenaRoom(userCharacter):
    testArena1 = TestArena
    print(testArena1.description)
    enemyChosen = randomEnemy()
    battle(userCharacter, enemyChosen)

def battle(userCharacter,enemyChosen):
    displayUserInfo(userCharacter)
    displayEnemyInfo(enemyChosen)
    userHealth = userCharacter.health
    userDamage = userCharacter.damage
    enemyHealth = enemyChosen.health
    enemyDamage = enemyChosen.damage
    while (userHealth > 0 or enemyHealth > 0):
        if enemyHealth > 0:
            enemyHealth = userAttack(userDamage, enemyHealth)
            print("Enemy Health: ", enemyHealth)
        if userHealth > 0:
            userHealth = enemyAttack(userHealth, enemyDamage)
            print("User Health: ", userHealth)

def userAttack(userDamage, enemyHealth):
    damageDone = int(enemyHealth - userDamage)
    return damageDone
def enemyAttack(userHealth, enemyDamage):
    damageDone = userHealth - enemyDamage
    return damageDone

def displayUserInfo(userCharacter):
    insertPrintBreaks()
    print(userCharacter.name)
    print(userCharacter.weapon)
    print(userCharacter.health)
    insertPrintBreaks()

def displayEnemyInfo(enemyChosen):
    insertPrintBreaks()
    print(enemyChosen.name)
    print(enemyChosen.description)
    print(enemyChosen.weapon)
    print(enemyChosen.health)
    insertPrintBreaks()

# Random Enemy Generator if more enemies added the random number generator needs to be adjusted
# Or find a way to show how long the list is
def randomEnemy():
    enemyObject = Enemy
    enemylist = enemyObject.enemies
    number = random.uniform(0,2)
    roundNumber = int(round(number))
    enemyChosen = enemylist[roundNumber]
    return enemyChosen

# I need to find a way to move the classes to another folder
class Ranger:
    name = "Ranger"
    description = "I use bows"
    weapon = "Bow"
    health = 15
    damage = 10
    
class Warrior:
    name = "Warrior"
    description = "I use swords and sheilds"
    weapon = "Sword"
    health = 25
    damage = 5

class Wizard:
    name = "Wizard"
    description = "I use magic"
    weapon = "Staff"
    health = 10
    damage = 15

class TestArena:
    description = "Whats going on here?"
    
class originRooms:
    description = "I lone dark room with 3 door ways, each one marked in blood"

class door1:
    description = "A wooden door, with a 1 on it. The door has a glowing red light comming underneath it"
    class room1:
        description = "You walk into the room and find a red glowing orb engraved in ancient wrighting"
        options = ["Take Orb", "Search for a way out"]

class orbTaken:
    description = "The orb glows with emense light, and they energy flows into your spirit"

class searchForWayOut:
    description = "While looking around the glowing room, you find a hole in the ground."

class door2:
    description = "A stone door with a 2 on it. No light can be seen comming from it"
    class room2:
        description = "You walk into a room with that holds nothing, simply one giant room with no exits it seems. The door suddenly closes behind you."
        options = ["Search for a way out", "Try to open that entrance"]

class door3:
    description = "A beaten up door with a 3 on it. Their is no light coming from it, but you feel wind blowing through the cracks."
    class room3:
        description = "You walk into a black errie room. When you try to close the half destroyed door the doorway caves in and your left in the dark."
        options = ["Allow to your eyes to adjust","Feel around for something"]

class Goblin:
    name = "Goblin"
    description = "An ugly little creature that is not looking at you to kind"
    weapon = "Axe"
    health = 10
    damage = 1

class Troll:
    name = "Troll"
    description = "Holy cow thats big"
    weapon = "Club"
    health = 30
    damage = 2

class Necromancer:
    name = "Necromancer"
    description = "Has an erie auroa"
    weapon = "Possessed Staff"
    health = 10
    damage = 3

# Used to put the enemies in an array for random number generator
class Enemy:
    theGoblin = Goblin
    theTroll = Troll
    theNecromancer = Necromancer
    enemies = [theGoblin,theTroll,theNecromancer]
main()
