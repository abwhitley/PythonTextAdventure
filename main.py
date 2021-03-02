class Ranger:
    description = "I use bows"

class Warrior:
    description = "I use swords and sheilds"

class Wizard:
    description = "I use magic"

def main():
    character = chooseYourCharacter()
    print(character.description)



def chooseYourCharacter():
    print("What class would you like?")
    choise = input("Ranger, Warrior or Wizard?")
    print("You chose ", choise)
    if choise == "Ranger":
        character = Ranger
    elif choise == "Warrior":
        character = Warrior
    elif choise == "Wizard":
        character = Wizard
    return character
main()