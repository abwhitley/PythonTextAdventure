class Ranger:
    description = "I use bows"

class Warrior:
    description = "I use swords and sheilds"

class Wizard:
    description = "I use magic"

class originRooms:
    description = "I lone dark room with 3 door ways, each one marked in blood"

class door1:
    description = "A wooden door, with a 1 on it. The door has a glowing red light comming underneath it"
    class room1:
        description = "You walk into the room and find a red glowing orb engraved in ancient wrighting"
class door2:
    description = "A stone door with a 2 on it. No light can be seen comming from it"
    class room2:
        description = "You walk into a room with that holds nothing, simply one giant room with no exits it seems. The door suddenly closes behind you."
class door3:
    description = "A beaten up door with a 3 on it. Their is no light coming from it, but you feel wind blowing through the cracks."
    class room3:
        description = "You walk into a black errie room. When you try to close the half destroyed door the doorway caves in and your left in the dark."

def main():
    character = chooseYourCharacter()
    print(character.description)
    insertPrintBreaks()
    doorChosen = originRoom()
    firstRoomChosen(doorChosen)

def insertPrintBreaks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def firstRoomChosen(doorChosen):
    if doorChosen == door1:
        print(door1.room1.description)
        insertPrintBreaks()
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
