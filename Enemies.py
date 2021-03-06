# TODO add: dodge chance
# TODO REWORK: damage and health... THE PLAYER SHOULD BE ABLE TO LOSE
# TODO add: different attacks
class Goblin:
    name = "Goblin"
    description = "An ugly little creature that is not looking at you to kind"
    weapon = "Axe"
    health = 20
    damage = 5

class Troll:
    name = "Troll"
    description = "Holy cow thats big"
    weapon = "Club"
    health = 50
    damage = 15

class Necromancer:
    name = "Necromancer"
    description = "Has an erie auroa"
    weapon = "Possessed Staff"
    health = 30
    damage = 10

# TODO implement a Boss Fight
# make a random generator for the enemyChosen()
# each level can possibly have a boss fight 
class Cathulu:
    name = "Cathulu"
    description = "The baddest of Bad"
    weapon = "The souls of the worlds"
    health = 250
    damage = 20
class GrimReaper:
    name = "Grim Reaper"
    description = "Reaper of Souls"
    weapon = "Scythe"
    health = 100
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