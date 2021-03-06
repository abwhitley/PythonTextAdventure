# TODO add: Dodge Chance
class Ranger:
    name = "Ranger"
    description = "I use bows"
    weapon = "Bow"
    health = 15
    damage = 10
    items = []
    class LongShot:
        name = "Long Shot"
        description = "Bow attack with full charge"
        damage = 15
    class DaggerDash:
        name = "Dagger Dash"
        description = "Dashes forward cutting into the enemy"
        damage = 10
    attacks = [LongShot, DaggerDash]

class Warrior :
    name = "Warrior"
    description = "I use swords and sheilds"
    weapon = "Sword"
    health = 25
    damage = 5
    items = []
    class SheildSmash:
        name = "Sheild Smash"
        description = "Back hand the enemy with the sheild"
        damage = 5
    class SwordsEdge:
        name = "Swords Edge"
        description = "Cut into the enemy with the sharp edge of the blade"
        damage = 15
    attacks = [SheildSmash, SwordsEdge]

class Wizard:
    name = "Wizard"
    description = "I use magic"
    weapon = "Staff"
    health = 10
    damage = 15
    items = []
    class FireBall:
        name = "Fireball"
        description = "Blast of skin melting flames"
        damage = 20
    class IceShard:
        name = "Ice Shard"
        description = "Ice spike thrown straight at the enemy"
        damage = 15
    attacks = [FireBall, IceShard]

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