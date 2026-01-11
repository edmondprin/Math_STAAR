import random

# set_generator for add & mult with little hardcoding

def build_set_mult():
    mi = 1
    ma = 10
    my_set = set()
    while len(my_set) < int((ma * (ma + 1) / 2)):
        n1 = random.randint(mi, ma)
        n2 = random.randint(mi, ma)
        key = (min(n1, n2), max(n1, n2))

        if key in my_set:
            continue
        
        my_set.add(key)
    return my_set, len(my_set)

print(f"Set(x):{build_set_mult()}\n")



def build_set_add():
    mi = 1
    ma = 100
    my_set = set()
    while len(my_set) < int((ma * (ma + 1) / 2)):
        n1 = random.randint(mi, ma)
        n2 = random.randint(mi, ma)
        key = (min(n1, n2), max(n1, n2))

        if key in my_set:
            continue
        
        my_set.add(key)
    return my_set, len(my_set)

print(f"Set(+):{build_set_add()}\n")

print("Done!")

'''
def go():
    my_set = set()
    while len(my_set) < 3:
        n1 = int(input("Number 1: "))
        n2 = int(input("Number 2: "))
        key = (min(n1, n2), max(n1, n2))

        if key in my_set:
            print("Duplicate pair, try again.")
            continue

        my_set.add(key)

    return my_set

print(go())





# use a set to scale

my_numbers = []

while len(my_numbers) < 3:
    try:
        numb = int(input("Enter number: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if numb in my_numbers:
        print("Please enter a new number!")
        continue

    my_numbers.append(numb)

print(my_numbers)



while True:
    nombre = input("Cual es tu nombre? ")
    if nombre.strip().capitalize() == "Caca":
        print("Ese nombre no es válido. Intenta otra vez.")
        continue
    break


name = input("Enter your name: ")

while name.strip().lower() == "caca":
    print("That name is not allowed.")
    name = input("Enter your name: ")



while True:
    name = input("Enter your name: ")
    if name.strip().lower() != "caca":
        break



“Can I write the stop condition before the loop starts?”
	•	Yes → use while condition
	•	No → use while True with an explicit break or return

    
def get_name():
     word = []
     while len(word) < 6:
         letter = input("Enter a letter: ")
         word.append(letter)
     name_str = "".join(word)
     return name_str
     
get_name()

'''