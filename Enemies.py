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