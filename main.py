# This line needs to be worked on to import the classes
from Python Practice.Text-Based Adventure import class.py

# Red\
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


def main():
    character = chooseYourCharacter()
    print(character.description)
    insertPrintBreaks()
    doorChosen = originRoom()
    firstRoomChosen(doorChosen)
    print(character.description)

def insertPrintBreaks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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

def chooseYourCharacter():
    insertPrintBreaks()
    print("What class would you like?")
    choise = input("Ranger, Warrior or Wizard?")
    insertPrintBreaks()
    print("You chose ", choise)
    insertPrintBreaks()
    if choise == "Ranger":
        character = Ranger
    elif choise == "Warrior":
        character = Warrior
    elif choise == "Wizard":
        character = Wizard
    return character

def originRoom():
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







main()
