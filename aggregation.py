

class Apartment:
    def __init__(self, owner: str):
        self.owner = owner
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
    def list_rooms(self):
        return [f"{room.roomtype}" for room in self.rooms]

class Room:
    def __init__(self, roomtype: str):
        self.roomtype = roomtype
        

apartment = Apartment("Kostya")
print(apartment.owner)

dining_room = Room("dining-room")
kitchen = Room("kitchen")
bathroom = Room("bathroom")
bedroom = Room("bedroom")

apartment.add_room(dining_room)
apartment.add_room(kitchen)
apartment.add_room(bathroom)
apartment.add_room(bedroom)

# print(apartment.list_rooms())

for room in apartment.list_rooms():
    print(room)


    
