def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())

print(highlight_word("Ich bin ein Berliner!", "Berliner"))
print(highlight_word("Have a nice day!", "nice"))



def alphabetize_lists(list1, list2):

  new_list = list1 # Initialize a new list.
  mew_list.extend(list2) # Combine the lists.
  new_list.sort() # Sort the combined lists.
  new_list = ___ # Assign the combined lists to the "new_list".
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]

listA = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
listB = ["Loik", "Gabriel", "Ahmed", "Soraya"]

listA.extend(listB)
print(listA)
listA.sort()
print(listA)


print(alphabetize_lists(Aniyahs_list, Imanis_list))

car_make = "Lamborghini"
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]