# TODO add: Dodge Chance
# TODO add: Diffrent Attacks
class Ranger:
    name = "Ranger"
    description = "I use bows"
    weapon = "Bow"
    health = 15
    damage = 10
    items = []
    
class Warrior :
    name = "Warrior"
    description = "I use swords and sheilds"
    weapon = "Sword"
    health = 25
    damage = 5
    items = []

class Wizard:
    name = "Wizard"
    description = "I use magic"
    weapon = "Staff"
    health = 10
    damage = 15
    items = []

# TODO Rework health potion
# TODO add: Health upgrade
class HealthPotion:
    name = "Health Potion"
    description = "Increases Health"

class WeaponUpgrade:
    name = "Weapon Upgrade"
    description = "Upgrades Weapon Quality"

# TODO add: Chest Trap, user takes damage from trap
class Chest:
    name = "Chest"
    description = "A peculiar looking chest"
    items = [HealthPotion, WeaponUpgrade]