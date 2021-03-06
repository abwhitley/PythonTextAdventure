# TODO add: dodge chance
# TODO REWORK: damage and health... THE PLAYER SHOULD BE ABLE TO LOSE
class Goblin:
    name = "Goblin"
    description = "An ugly little creature that is not looking at you to kind"
    weapon = "Axe"
    health = 20
    damage = 5
    class Slash:
        name = "Slash"
        description = "Slashed with the blunt blade of the axe"
        damage = 15
    class ThrowingAxe:
        name = "Throwing Axe"
        description = "Axe thrown with intensity"
        damage = 10
    attacks = [Slash, ThrowingAxe]

class Troll:
    name = "Troll"
    description = "Holy cow thats big"
    weapon = "Club"
    health = 50
    damage = 15
    class Smash:
        damage = 25
    class GrabAndThrow:
        damage = 15
    attacks = [Smash, GrabAndThrow]

class Necromancer:
    name = "Necromancer"
    description = "Has an erie auroa"
    weapon = "Possessed Staff"
    health = 30
    damage = 10
    class DarkMagic:
        name = "Dark Magic"
        description = "It feels like a heart attack"
        damage = 15
    class ResurectionStab:
        name = "Ressurection Stab"
        description = "Used to resurect a boney figure that rushes at you"
        damage = 20
    attacks = [DarkMagic, ResurectionStab]

# Bosses
class Cathulu:
    name = "Cathulu"
    description = "The baddest of Bad"
    weapon = "The souls of the worlds"
    health = 250
    damage = 20
    class SoulEater:
        name = "Soul Eater"
        description = "You feel no light inside"
        damage = 25
    class EderithSlash:
        name = "Ederith Slash"
        description = "Cathulu arms lashes at you"
        damage = 15
    attacks = [SoulEater, EderithSlash]
class GrimReaper:
    name = "Grim Reaper"
    description = "Reaper of Souls"
    weapon = "Scythe"
    health = 100
    damage = 25
    class ScytheSlice:
        name = "Scythe Slice"
        description = "The edge of its blade is unlike anything you have ever seen"
        damage = 25
    class BoneThrow:
        name = "Bone Throw"
        description = "The Grim Reaper throws one of its bone at you"
        damage = 10
    attacks = [ScytheSlice, BoneThrow]
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