pets = "Cats & Dogs"

# index()
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dogs"))

print("Dragons" in pets)
print("Dogs" in pets)

# lower()
answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

# strip()
answer = " yes "
if answer.strip() == "yes":
    print("User said yes")

# lstrip()
print(" yes ".lstrip())


# rstrip()
print(" yes ".rstrip())

# count()
"The number of times e occurs in thsi string is 4".count("e")

# endswith()
"Forest".endswith("rest")

# isnumeric()
"Forest".isnumeric()
"12345".isnumeric()
int("12345")

# join()
" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
":".join(["This", "is", "a", "phrase", "joined", "by", "colons"])

# split()
"This is another great example".split()

# format()
# also converts numbers!
print("Hello {}, your lucky number is {}!".format("Stefan", 7))
print("Hello {name}, your lucky number is {number}!".format(number=777, name="Stefan"))

price = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

