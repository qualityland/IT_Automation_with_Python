# manually
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

# list comprehension
multiples = [ x*7 for x in range(1, 11)]
print(multiples)


languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

# multiples of 3
multiples_of_3 = [x for x in range(0, 101) if x % 3 == 0]
print(multiples_of_3)