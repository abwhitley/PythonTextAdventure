# TODO: THIS WHOLE THING NEEDS TO BE BETTER ORGANIZED... ITS A MESS
class TestArena:
    description = "Whats going on here?"
    
class originRooms:
    description = "A lone dark room with 3 door ways, each one marked in blood"

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
class ApproachChest:
    description = "The chest doesnt look so special"
    options = ["Open chest", "Walk Away"]

class RandomRoom:
    description = "A unknown room"

class ChestRoom:
    name = "Chest Room"
    description = "This is a chest Room"

class BattleRoom:
    name = "Battle Room"
    description = "This is a battle room"

class CampSite:
    name = "Camp Site"
    description = "A room to rest"

class Rooms:
    aChestRoom = ChestRoom
    aBattleRoom = BattleRoom
    aCampSite = CampSite
    roomList = [aChestRoom,aBattleRoom, aCampSite]

class door3:
    description = "A beaten up door with a 3 on it. Their is no light coming from it, but you feel wind blowing through the cracks."
    class room3:
        description = "You walk into a black errie room. When you try to close the half destroyed door the doorway caves in and your left in the dark."
        options = ["Allow to your eyes to adjust","Feel around for something"]