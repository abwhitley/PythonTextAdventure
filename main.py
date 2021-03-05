# This line needs to be worked on to import the classes
# from Python Practice.Text-Based Adventure import class.py
import random
import Rooms
import Enemies
import User
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
        userCharacter = User.Ranger
    elif choice == "Warrior":
        userCharacter = User.Warrior
    elif choice == "Wizard":
        userCharacter = User.Wizard
    return userCharacter

def wouldYouLikeToLookAround():
    # originRooms is the class that contains all info for the doors and their descriptions
    entrance = Rooms.originRooms
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
        doorObject = Rooms.door1
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
        doorObject = Rooms.door2
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
        doorObject = Rooms.door3
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
        doorObject = Rooms.TestArena
        return doorObject

# Allow the door chosen to open the correct room and Secret Room
def firstRoomChosen(doorChosen,userCharacter):
    if doorChosen == Rooms.door1:
        print(Rooms.door1.room1.description)
        insertPrintBreaks()
        redOrbRoom()
    elif doorChosen == Rooms.door2:
        print(Rooms.door2.room2.description)
        insertPrintBreaks()
        loneChestRoom(userCharacter)
    elif doorChosen == Rooms.door3:
        print(Rooms.door3.room3.description)
        insertPrintBreaks()
    elif doorChosen == Rooms.TestArena:
        insertPrintBreaks()
        secretArenaRoom(userCharacter)

# 1st door Room
def redOrbRoom():
    redOrb = Rooms.door1.room1
    print("1:", redOrb.options[0])
    print("2:", redOrb.options[1])
    choice = int(input("1 or 2?"))
    insertPrintBreaks()
    if choice == 1:
        choice1 = Rooms.orbTaken
        print(choice1.description)
    elif choice == 2:
        choice2 = Rooms.searchForWayOut
        print(choice2.description)
# Works up until you choose to either Approach Chest or try open entrance
def loneChestRoom(userCharacter):
    chestRoom = Rooms.door2.room2
    print("1: ", chestRoom.options[0])
    print("2: ", chestRoom.options[1])
    choice = input("1 or 2?")
    insertPrintBreaks()
    # Works until here
    if choice == 1:
        approach = Rooms.ApproachChest
        print("1: ", approach.options[0])
        print("2: ", approach.options[1])
        choice1 = input("1 or 2?")
        if choice1 == 1:
            itemReceived = openChest()
            print("You recieved: ", itemReceived)
            userCharacter.items.append(itemReceived)
        elif choice1 == 2:
            return loneChestRoom(userCharacter)
    elif choice == 2:
        print("You cant find anyway out")
        return loneChestRoom(userCharacter)


# Used to randomly select an item in the chest
# Unsure if it works 
def openChest():
    chestObject = User.Chest
    randomNumber = random.uniform(0,1)
    roundedNumber = int(round(randomNumber))
    itemsList = chestObject.items
    itemChosen = itemsList[roundedNumber]
    return itemChosen

# using to test combat
# The random number generator is working i just need to parse the day
def secretArenaRoom(userCharacter):
    testArena1 = Rooms.TestArena
    print(testArena1.description)
    enemyChosen = randomEnemy()
    battle(userCharacter, enemyChosen)

# Battle system this is Auto Battle, no choice purly based on damage and health
def battle(userCharacter,enemyChosen):
    displayUserInfo(userCharacter)
    displayEnemyInfo(enemyChosen)
    userHealth = userCharacter.health
    userDamage = userCharacter.damage
    enemyHealth = enemyChosen.health
    enemyDamage = enemyChosen.damage
    while(userHealth >= 0) or (enemyHealth >= 0):
        enemyHealth = userAttack(userDamage,enemyHealth)
        displayEnemyInfoInBattle(enemyChosen,enemyHealth)
        if enemyHealth <= 0:
            break
        userHealth = enemyAttack(userHealth, enemyDamage)
        displayUserInfoInBattle(userCharacter, userHealth)
        if userHealth <= 0:
            break
    if userHealth <= 0:
        print("You died")
    if enemyHealth <= 0:
        print("The enemy has perished")

# User Attack
def userAttack(userDamage, enemyHealth):
    print("You attack")
    remainingHealth = int(enemyHealth - userDamage)
    return remainingHealth

# Enemy Attack
def enemyAttack(userHealth, enemyDamage):
    print("The enemy attacks")
    remainingHealth = userHealth - enemyDamage
    return remainingHealth

# Displays All User Info
def displayUserInfo(userCharacter):
    insertPrintBreaks()
    print(userCharacter.name)
    print("Weapon: ", userCharacter.weapon)
    print("Damage: ", userCharacter.damage)
    print("Health: ", userCharacter.health)
    insertPrintBreaks()

def displayUserInfoInBattle(userCharacter, userHealth):
    insertPrintBreaks()
    print(userCharacter.name)
    print("Weapon: ", userCharacter.weapon)
    print("Damage: ", userCharacter.damage)
    print("Health: ", userHealth)
    insertPrintBreaks()

# Display Enemy Info
def displayEnemyInfo(enemyChosen):
    insertPrintBreaks()
    print(enemyChosen.name)
    print(enemyChosen.description)
    print("Weapon: ", enemyChosen.weapon)
    print("Damage: ", enemyChosen.damage)
    print("Health: ", enemyChosen.health)
    insertPrintBreaks()

def displayEnemyInfoInBattle(enemyChosen, enemyHealth):
    insertPrintBreaks()
    print(enemyChosen.name)
    print(enemyChosen.description)
    print("Weapon: ", enemyChosen.weapon)
    print("Damage: ", enemyChosen.damage)
    print("Health: ", enemyHealth)
    insertPrintBreaks()



# Random Enemy Generator and Boss Generator
# Creates a boss if willItBeABoss() evauates to true

def randomEnemy():
    isBossEncounter = willItBeABoss()
    if isBossEncounter == True:
        bossObject = Enemies.Boss
        bossList = bossObject.bosses
        bossCount = len(bossList)
        randomNumber = randomNumberGenerator(bossCount)
        bossChosen = bossList[randomNumber]
        return bossChosen
    else:
        enemyObject = Enemies.Enemy
        enemylist = enemyObject.enemies
        enemyCount = len(enemylist)
        randomNumber = randomNumberGenerator(enemyCount)
        enemyChosen = enemylist[randomNumber]
        return enemyChosen

# Decides if their will be a boss, 1 in 10 odds
def willItBeABoss():
    randomNumber = random.uniform(0,10)
    roundedNumber = int(round(randomNumber))
    if roundedNumber == 1:
        return True
    else:
        return False

# Used to return a random number to choose an item from an array
def randomNumberGenerator(maxNumber):
    randomNumber = random.randint(0, (maxNumber-1))
    roundedRandomNumber = int(round(randomNumber))
    return roundedRandomNumber

main()
