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
        description = "You walk into the room, the entrance closes imediatly behind you. There is a lone wooden chest in the room. With nothing else, no were to go."
        options = ["Approach the Chest", "Try to open that entrance"]

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

# TODO implement a Boss Fight
# make a random generator for the enemyChosen()
# each level can possibly have a boss fight 
class Cathulu:
    name = "Cathulu"
    description = "The baddest of Bad"
    weapon = "The souls of the worlds"
    health = 100
    damage = 20
class GrimReaper:
    name = "Grim Reaper"
    description = "Reaper of Souls"
    weapon = "Scythe"
    health = 50
    damage = 25
# Used to put the enemies in an array for random number generator
class Enemy:
    theGoblin = Goblin
    theTroll = Troll
    theNecromancer = Necromancer
    enemies = [theGoblin,theTroll,theNecromancer]

class Boss:
    theCathulu = Cathulu
    theGrimReaper = GrimReaper
    bosses = [theCathulu,theGrimReaper]