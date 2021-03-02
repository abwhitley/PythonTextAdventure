class Ranger:
    description = "I use bows"
    weapon = "Bow"
    health = 15
    

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
