# This line needs to be worked on to import the classes
# from Python Practice.Text-Based Adventure import class.py

# Main executable that controls flow
def main():
    character = chooseYourCharacter()
    print(character.description)
    insertPrintBreaks()
    doorChosen = originRoom()
    firstRoomChosen(doorChosen)
    print(character.description)

# Function to insert line breaks for easier reading in console
def insertPrintBreaks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Function to choose Character
def chooseYourCharacter():
    insertPrintBreaks()
    print("What class would you like?")
    choise = input("Ranger, Warrior or Wizard?")
    insertPrintBreaks()
    print("You chose ", choise)
    insertPrintBreaks()
    # Connects users choise to the correct class
    if choise == "Ranger":
        character = Ranger
    elif choise == "Warrior":
        character = Warrior
    elif choise == "Wizard":
        character = Wizard
    return character

# Origin Room that leads to the door choise 
def originRoom():
    # originRooms is the class that contains all info for the doors and their descriptions
    entrance = originRooms
    print("You drop into a peculiar room, almost no light but a lone candle`")
    print("Would you like to look around?")
    insertPrintBreaks()
    choise = input("Yes or No")
    if choise == "Yes":
        print(entrance.description)
        insertPrintBreaks()
    elif choise == "No":
        print("Well what else are you going to do?")
        print("Lets look around the room")
        print(entrance.description)
        insertPrintBreaks()

    print("Which Door do you want to look at?")
    doorChoise = int(input("1,2 or 3?"))
    insertPrintBreaks()
    if doorChoise == 1:
        doorObject = door1
        print(doorObject.description)
        print("Would you like to go through the door?")
        insertPrintBreaks()
        doorChoise1 = input("Yes or No")
        insertPrintBreaks()
        if doorChoise1 == "Yes":
            return doorObject
        elif doorChoise1 == "No":
            print("Okay which door?")
            insertPrintBreaks()
            return originRoom()
    elif doorChoise == 2:
        doorObject = door2
        print(doorObject.description)
        print("Would you like to go through the door?")
        insertPrintBreaks()
        doorChoise1 = input("Yes or No")
        if doorChoise1 == "Yes":
            return doorObject
        elif doorChoise1 == "No":
            print("Okay which door?")
            insertPrintBreaks()
            return originRoom()
        print(doorObject.description)
    elif doorChoise == 3:
        doorObject = door3
        print(doorObject.description)
        print("Would you like to go through the door?")
        doorChoise1 = input("Yes or No")
        insertPrintBreaks()
        if doorChoise1 == "Yes":
            return doorObject
        elif doorChoise1 == "No":
            print("Okay which door?")
            insertPrintBreaks()
            return originRoom()

# Allow the door chosen to open the correct room
def firstRoomChosen(doorChosen):
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

# 1st door Room
def redOrbRoom():
    redOrb = door1.room1
    print("1:", redOrb.options[0])
    print("2:", redOrb.options[1])
    choise = int(input("1 or 2?"))
    insertPrintBreaks()
    if choise == 1:
        choise1 = orbTaken
        print(choise1.description)
    elif choise == 2:
        choise2 = searchForWayOut
        print(choise2.description)


class Ranger:
    description = "I use bows"
    weapon = "Bow"
    health = 15
    

# Used while the import statement is done correctly, remove once it is
class Warrior:
    description = "I use swords and sheilds"
    weapon = "Sword"

class Wizard:
    description = "I use magic"
    weapon = "Staff"

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


main()
