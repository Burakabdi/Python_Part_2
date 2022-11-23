# Create two tuples representing the two lists of first and last names described below:
# names: Numa, Tullio, Anco;
# surnames: Pompilio, Ostilio, Marzio
# Get a list in which each element is a dictionary {'first name': first name, 'last name': last name},
# which matches first and last names according to order.


names = ("Numa", "Tullio", "Anco")
surnames = ('Pompilio', 'Ostilio', 'Marzio')

l = []

for name, surname in zip(names,surnames):
    l.append({"name": name, "surname": surname}) in zip(names,surnames)

print(l)
