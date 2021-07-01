#class Point() :
#
#p = Point(2, 8)
#print(p.y)


class Flight() :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name) :
        if not self.open_seats() :
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        print(self.passengers)
        return self.capacity - len(self.passengers)

flight = Flight(3) #this line means Flight has value 3 for capacity in (self, capacity)

print(flight.capacity)

list_of_people = ["Tito", "Vic", "Joey", "Dolphy"]

for name_of in list_of_people :
    if flight.add_passenger(name_of):
        print(f"Successfully added {name_of} to flight.")
    else :
        print(f"No available seats for {name_of}")
