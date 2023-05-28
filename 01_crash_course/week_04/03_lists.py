fruits = ["Pineapple", "Banana", "Apple", "Melon"]
print(fruits)

# append to the end
fruits.append("Kiwi")
"Kiwi" in fruits
print(fruits)

# insert at index
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(25, "Peach")      # out of bound index! but works!
print(fruits)

# remove value
fruits.remove("Melon")
print(fruits)
fruits.remove("Pear")           # ValueError: not in list

# pop of at index (returns element)
fruit_3 = fruits.pop(3)
print(fruit_3)
print(fruits)

# replace (index notation)
fruits[2] = "Strawberry"
print(fruits)

# iterate through list
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# enumerate
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))