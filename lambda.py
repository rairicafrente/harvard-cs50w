people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cho", "house": "Ravenclaw"}
]

#def sort_by_name(person) :
    #return person["name"]
    #return person["house"]

#people.sort(key=sort_by_name)

#ABOVE IS EQUIVALENT TO LAMBDA FUNCTION BELOW

people.sort(key=lambda person: person["name"])

print(people)
