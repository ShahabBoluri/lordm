import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick(name):
    
    for i in range (2):
        name.append (random.choice (cards))
    return name
salaam =[]
pick(salaam)
print(salaam)