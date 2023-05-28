x = {}
type(x)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

# access entry
file_counts["txt"]

# key present?
"jpg" in file_counts
"html" in file_counts

# add entry
file_counts["cfg"] = 8
print(file_counts)

# update entry
file_counts["csv"] = 17
print(file_counts)

# remove entry
del file_counts["cfg"]
print(file_counts)

# iterate over keys
for extension in file_counts:
    print(extension)

# iterate over keys and values
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

# keys
file_counts.keys()

# values
file_counts.values()
for value in file_counts.values():
    print(value)