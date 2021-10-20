
# Python Program to Map two lists into a Dictionary

keys = ["name", "age", "job"]
values = ["John", 25, "Developer"]

myDict = {k: v for k, v in zip(keys, values)}
print("Dictionary Items  :  ",  myDict)

# Updating dictionaries

bio_data = {"Name": "Bena", "Age": 18, "Class": "First"}
print(bio_data)
bio_data["Age"] = 20  # update existing entry
bio_data["School"] = "Lakeside School"  # Add new entry
print(bio_data)

# Iterating dictionaries

names_ages = {"Andrew": 50,
              "Liz": 28,
              "Mark": 30,
              "Peter": 76}

for element in names_ages:
    print(element)
