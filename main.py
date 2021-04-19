import random
import Rooms
import Enemies
import User
# Updated the upgrade damage to an update the attacks damage with a choice
# TODO found a bug when user input if their is a special character in the input it crashes

# Main executable that controls flow
def main():
    userCharacter = chooseYourCharacter()
    insertPrintBreaks()
    doorChosen = chooseADoor()
    firstRoomChosen(doorChosen,userCharacter)

# Function to insert line breaks for easier reading in console
def insertPrintBreaks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Function to choose Character
def chooseYourCharacter():
    insertPrintBreaks()
    # input is converted into lower case so the choice isnt case sensative
    choice = input("What class would you like, the choices are Ranger, Warrior or Wizard? ").lower()
    insertPrintBreaks()
    # Connects users choise to the correct class
    if choice == "ranger":
        print("You chose",choice)
        userCharacter = User.Ranger
        print(userCharacter.description)
    elif choice == "warrior":
        print("You chose",choice)
        userCharacter = User.Warrior
        print(userCharacter.description)
    elif choice == "wizard":
        print("You chose",choice)
        userCharacter = User.Wizard
        print(userCharacter.description)
    # If input is not one of the above it will call the function again
    else:
        print("The class inputed does not match the options. Try Again.")
        chooseYourCharacter()
    return userCharacter

# Simple would you like to look around, leads to choosing the 3 doors
def wouldYouLikeToLookAround():
    # originRooms is the class that contains all info for the doors and their descriptions
    entrance = Rooms.originRooms
    print("You drop into a peculiar room, almost no light but a lone candle`")
    insertPrintBreaks()
    # choise is converted to lower case to remove case sensitivity 
    choice = input("Would you like to look around? (Yes or No): ").lower()
    if choice == "yes":
        print(entrance.description)
        insertPrintBreaks()
    elif choice == "no":
        print("Well what else are you going to do?")
        print("Lets look around the room")
        print(entrance.description)
        insertPrintBreaks()
    else:
        insertPrintBreaks()
        print("That is not an option")
        wouldYouLikeToLookAround()

# Origin Room that leads to the door choise 
def chooseADoor():
    wouldYouLikeToLookAround()
    doorChoice = int(input("Which Door do you want to look at? 1, 2, 3 or 4 for the Test Arena: "))
    insertPrintBreaks()
    if doorChoice == 1:
        doorObject = Rooms.door1
        print(doorObject.description)
        doorChoice1 = input("Would you like to go through the door? (Yes or No): ").lower()
        insertPrintBreaks()
        if doorChoice1 == "yes":
            return doorObject
        elif doorChoice1 == "no":
            print("Okay which door?")
            insertPrintBreaks()
            return chooseADoor()
        else:
            print("You did not choose a valid option. Try Again.")
            chooseADoor()
    elif doorChoice == 2:
        doorObject = Rooms.door2
        print(doorObject.description)
        doorChoice1 = input("Would you like to go through the door? (Yes or No): ").lower()
        if doorChoice1 == "yes":
            return doorObject
        elif doorChoice1 == "no":
            print("Okay which door?")
            insertPrintBreaks()
            return chooseADoor()
        else:
            print("You did not input a valid option. Try Again.")
            chooseADoor()
        print(doorObject.description)
    elif doorChoice == 3:
        doorObject = Rooms.door3
        print(doorObject.description)
        doorChoice1 = input("Would you like to go through the door? (Yes or No): ").lower()
        insertPrintBreaks()
        if doorChoice1 == "yes":
            return doorObject
        elif doorChoice1 == "no":
            print("Okay which door?")
            insertPrintBreaks()
            return chooseADoor()
        else:
            print("You didnt not input a vaild option. Try Again.")
            chooseADoor()
    elif doorChoice == 4:
        doorObject = Rooms.TestArena
        return doorObject
    else:
        print("You did not input an option, try again")
        insertPrintBreaks()
        chooseADoor()

# Allow the door chosen to open the correct room
def firstRoomChosen(doorChosen,userCharacter):
    if doorChosen == Rooms.door1:
        print(Rooms.door1.room1.description)
        insertPrintBreaks()
        redOrbRoom()
    elif doorChosen == Rooms.door2:
        print(Rooms.door2.room2.description)
        insertPrintBreaks()
        chestRoom(userCharacter)
    elif doorChosen == Rooms.door3:
        print(Rooms.door3.room3.description)
        insertPrintBreaks()
    elif doorChosen == Rooms.TestArena:
        insertPrintBreaks()
        battleRoom(userCharacter)

# 1st door Room
# TODO lead to the procedure generated rooms
# TODO make the orb change up the gameplay
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
    else:
        print("You did not input a vaild option. Try again.")
        redOrbRoom()

# Works up until you choose to either Approach Chest or not
# Reused in procedure generated rooms
# TODO allow game play to be easier against enemies for not getting the chest
def chestRoom(userCharacter):
    chestRoom = Rooms.door2.room2
    print("1: ", chestRoom.options[0])
    print("2: ", chestRoom.options[1])
    choice = int(input("1 or 2?"))
    insertPrintBreaks()
    if choice == 1:
        approach = Rooms.ApproachChest
        print("1: ", approach.options[0])
        print("2: ", approach.options[1])
        choice1 = int(input("1 or 2?"))
        insertPrintBreaks()
        if choice1 == 1:
            itemReceived = openChest(userCharacter)
            print("You recieved: ", itemReceived.name)
            print(itemReceived.description)
            powerUp(itemReceived,userCharacter)
            displayUserInfo(userCharacter)
            insertPrintBreaks()
            print("After scavaging the chest a door appears on the opposite side you entered from, you think at least, everything looks the same")
            keepGoing = input("Would you like to go deeper in the dungeon? (Enter yes or no): ").lower()
            if keepGoing == "yes":
                # TODO!!!!!!! After dying the code drops right here... 
                print("You walk to the door and open it")
                userCharacter.summary.roomsTraveled = userCharacter.summary.roomsTraveled + 1
                randomRoom(userCharacter)
            elif keepGoing == "no":
                # TODO make a quit screen that shows the play throughs progress
                print("What else are you going to do? There is no way back")
                userCharacter.summary.roomsTraveled = userCharacter.summary.roomsTraveled + 1
                randomRoom(userCharacter)
            else:
                print("The only way is forward...")
                randomRoom(userCharacter)
        elif choice1 == 2:
            return chestRoom(userCharacter)
        else:
            print("You did not insert a valid option. Try Again.")
            chestRoom(userCharacter)

    elif choice == 2:
        print("You cant find anyway out")
        return chestRoom(userCharacter)
    else:
        print("You did not insert a valid option. Try Again.")
        chestRoom(userCharacter)


# Random chance of it being a chest room or a battle room.
# TODO dont allow more than 2 chest rooms to appear
def randomRoom(userCharacter):
    # make a funtion to decide if it will be a battle room or a chest room
    nextRoom = Rooms.RandomRoom
    print(nextRoom.description)
    nextRoomChosen = randomRoomGenerator()
    if nextRoomChosen == Rooms.BattleRoom:
        print(nextRoomChosen.description)
        battleRoom(userCharacter)
    elif nextRoomChosen == Rooms.ChestRoom:
        print(nextRoomChosen.description)
        chestRoom(userCharacter)
    elif nextRoomChosen == Rooms.CampSite:
        campSite(userCharacter)

# Used to deceided which of the two rooms it will be
# TODO add check to make sure 2 chest rooms in a row cant happen
def randomRoomGenerator():
    room = Rooms.Rooms
    roomList = room.roomList
    roomCount = len(roomList)
    randomNumber = randomNumberGeneratorForLists(roomCount)
    if randomNumber == 0:
        battleRoomObject = Rooms.BattleRoom
        return battleRoomObject
    elif randomNumber == 1:
        chestRoomObject = Rooms.ChestRoom
        return chestRoomObject
    elif randomNumber == 2:
        campSiteRoomObject = Rooms.CampSite
        return campSiteRoomObject

# Used to allow the chest item to add to the characters stats
def powerUp(itemReceived, userCharacter):
    if itemReceived == User.HealthPotion:
        userCharacter.health = userCharacter.health + 10
    elif itemReceived == User.WeaponUpgrade:
        attacksToUpgrade = userCharacter.attacks
        print("Which attack would you like to upgrade?")
        print("1: ", attacksToUpgrade[0].name)
        print("2: ", attacksToUpgrade[1].name)
        attackChosenToUpgrade = int(input("Choose: "))
        if attackChosenToUpgrade == 1:
            print("Youre attack damage was:", userCharacter.attacks[0].damage)
            userCharacter.attacks[0].damage = userCharacter.attacks[0].damage + 2
            print("Youre attack damage is now: ", userCharacter.attacks[0].damage)
        elif attackChosenToUpgrade == 2:
            print("Youre attack damage was:", userCharacter.attacks[1].damage)
            userCharacter.attacks[1].damage = userCharacter.attacks[1].damage + 2
            print("Youre attack damage is now: ", userCharacter.attacks[1].damage)
        else:
            print("You did not insert a valid option. Try Again.")
            powerUp(itemReceived, userCharacter)


# Used to randomly select an item in the chest
def openChest(userCharacter):
    chestObject = User.Chest
    randomNumber = random.uniform(0,1)
    roundedNumber = int(round(randomNumber))
    itemsList = chestObject.items
    itemChosen = itemsList[roundedNumber]
    userCharacter.summary.chestsOpened = userCharacter.summary.chestsOpened + 1
    return itemChosen

# Used in procedure generated room
def battleRoom(userCharacter):
    testArena1 = Rooms.TestArena
    print(testArena1.description)
    enemyChosen = randomEnemy()
    battle(userCharacter, enemyChosen)

def campSite(userCharacter):
    restRoom = Rooms.CampSite
    print(restRoom.name)
    print(restRoom.description)
    healAmount = userCharacter.health * .5
    userCharacter.health = userCharacter.health + healAmount
    print("After resting a door appears on the opposite side you entered from, you think at least, everything looks the same")
    keepGoing = input("Would you like to go deeper in the dungeon? (Enter yes or no): ").lower()
    if keepGoing == "yes":
        # TODO!!!!!!! After dying the code drops right here... 
        print("You walk to the door and open it")
        userCharacter.summary.roomsTraveled = userCharacter.summary.roomsTraveled + 1
        randomRoom(userCharacter)
    elif keepGoing == "no":
        # TODO make a quit screen that shows the play throughs progress
        print("What else are you going to do? There is no way back")
        userCharacter.summary.roomsTraveled = userCharacter.summary.roomsTraveled + 1
        randomRoom(userCharacter)
    else:
        print("The only way is forward...")
        randomRoom(userCharacter)


# Battle system this is Auto Battle, no choice purly based on damage and health
# TODO add: Dodge Chance
# TODO add: Missed Chance
# TODO add: Choice to use items in battle, health potions
def battle(userCharacter,enemyChosen):
    displayUserInfo(userCharacter)
    displayEnemyInfo(enemyChosen)
    while(userCharacter.health >= 0) or (enemyChosen.health >= 0):
        enemyChosen.health = userAttack(userCharacter,enemyChosen.health)
        displayEnemyInfoInBattle(enemyChosen)
        if enemyChosen.health <= 0:
            break
        # choses a random enemy attack
        enemyAttackChosen = randomEnemyAttack(enemyChosen)
        userCharacter.health = enemyAttack(userCharacter.health, enemyAttackChosen, userCharacter)
        displayUserInfoInBattle(userCharacter)
        if userCharacter.health <= 0:
            break
    if userCharacter.health <= 0:
        print("You died")
        gameSummary(userCharacter)
    elif enemyChosen.health <= 0:
        userCharacter.experiance = userCharacter.experiance + enemyChosen.experiance
        updateLevel(userCharacter)
        print("The enemy has perished")
        insertPrintBreaks()
        print("A door opens behind where the ", enemyChosen.name ,"stood.")
        userCharacter.summary.battlesWon = userCharacter.summary.battlesWon + 1
        userCharacter.summary.roomsTraveled = userCharacter.summary.roomsTraveled + 1
        keepGoing = input("Would you like to continue? (Enter yes or no)").lower()
        if keepGoing == "yes":
            randomRoom(userCharacter)
            print("You walk to the door and open it")
        elif keepGoing == "no":
            # TODO make a quit screen that shows the play throughs progress
            print("What else are you going to do? There is no way back")
            randomRoom(userCharacter)
        else:
            print("The only way is forward...")
            randomRoom(userCharacter)

# Shows the user a summary of the game after death
def gameSummary(userCharacter):
    insertPrintBreaks()
    insertPrintBreaks()
    print("END OF GAME SUMMARY")
    insertPrintBreaks()
    insertPrintBreaks()
    print("Character Level: ", userCharacter.level)
    print("Eperiance Points: ", userCharacter.experiance)
    print("Rooms Survived: ", userCharacter.summary.roomsTraveled)
    print("Chests Openned: ", userCharacter.summary.chestsOpened)
    print("Battles Won: ", userCharacter.summary.battlesWon)
    print("Damage Dealt: ", userCharacter.summary.damageDealt)
    print("Damage Received: ", userCharacter.summary.damageRecieved)

# Choses randomEnemyAtack
def randomEnemyAttack(enemyChosen):
    attacks = enemyChosen.attacks
    numberOfAttacks = len(attacks)
    randomNumber = randomNumberGeneratorForLists(numberOfAttacks)
    attackChosen = attacks[randomNumber]
    print(attackChosen.name)
    print(attackChosen.description)
    return attackChosen


# User Attack
def userAttack(userCharacter, enemyHealth):
    attacks = userCharacter.attacks
    print("Attacks:")
    print("1: ", attacks[0].name)
    print("2: ", attacks[1].name)
    choice = int(input("Choose attack: "))
    if choice == 1:
        attackChosen = attacks[0]
    elif choice == 2:
        attackChosen = attacks[1]
    else:
        print("You did not insert a valid option. Try Again.")
        userAttack(userCharacter, enemyHealth)

    print("You used: ", attackChosen.name)
    print(attackChosen.description)
    remainingHealth = int(enemyHealth - attackChosen.damage)
    userCharacter.summary.damageDealt = userCharacter.summary.damageDealt + attackChosen.damage
    return remainingHealth

# Enemy Attack
def enemyAttack(userHealth, attackChosen, userCharacter):
    print("The enemy attacks")
    print("The enemy used: ", attackChosen.name)
    print("Damage: ", attackChosen.damage)
    remainingHealth = userHealth - attackChosen.damage
    userCharacter.summary.damageRecieved = userCharacter.summary.damageRecieved + attackChosen.damage
    return remainingHealth

# Displays All User Info
def displayUserInfo(userCharacter):
    insertPrintBreaks()
    print(userCharacter.name)
    print("Weapon: ", userCharacter.weapon)
    print("Health: ", userCharacter.health)
    print("Attack: ", userCharacter.attacks[0].name," Damage: ", userCharacter.attacks[0].damage)
    print("Attack: ", userCharacter.attacks[1].name," Damage: ", userCharacter.attacks[1].damage)
    insertPrintBreaks()

# DIsplays user info mid battle
def displayUserInfoInBattle(userCharacter):
    insertPrintBreaks()
    print(userCharacter.name)
    print("Weapon: ", userCharacter.weapon)
    print("Health: ", userCharacter.health)
    insertPrintBreaks()

# Display Enemy Info
def displayEnemyInfo(enemyChosen):
    insertPrintBreaks()
    print(enemyChosen.name)
    print(enemyChosen.description)
    print("Weapon: ", enemyChosen.weapon)
    print("Health: ", enemyChosen.health)
    insertPrintBreaks()

# Displays enemy info mid battle
def displayEnemyInfoInBattle(enemyChosen):
    insertPrintBreaks()
    print(enemyChosen.name)
    print(enemyChosen.description)
    print("Weapon: ", enemyChosen.weapon)
    print("Health: ", enemyChosen.health)
    insertPrintBreaks()


def updateLevel(userCharacter):
    unroundedLevel = (userCharacter.experiance / 50)
    userCharacter.level = round(unroundedLevel)
    if userCharacter.level < 1:
        userCharacter.level = 1




# Random Enemy Generator and Boss Generator
# Creates a boss if willItBeABoss() evaluates to true
def randomEnemy():
    isBossEncounter = willItBeABoss()
    if isBossEncounter == True:
        bossObject = Enemies.Boss
        bossList = bossObject.bosses
        bossCount = len(bossList)
        randomNumber = randomNumberGeneratorForLists(bossCount)
        bossChosen = bossList[randomNumber]
        return bossChosen
    else:
        enemyObject = Enemies.Enemy
        enemylist = enemyObject.enemies
        enemyCount = len(enemylist)
        randomNumber = randomNumberGeneratorForLists(enemyCount)
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
def randomNumberGeneratorForLists(maxNumber):
    randomNumber = random.randint(0, (maxNumber-1))
    roundedRandomNumber = int(round(randomNumber))
    return roundedRandomNumber

main()
