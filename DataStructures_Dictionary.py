"""Data Structure_Dictionary"""

tdict = {"class":"Tuesday" , "workshop":"Python" , "year":"2021" , "year":"2021")
print(tdict)
x = tdict["class"] # Indexing does not work with numbers but with keys.
print(x)

y = tdict.get("class")
print(y)

tdict["class"] = "Friday" # changing the value of a specific key in the dictionary
print(tdict)

tdict["Captain"] = "Harini" # adding a key-value pair in the dictionary
print(tdict)

del tdict["class"]
print(tdict)

tdict.pop("workshop")
print(tdict)

del tdict
print(tdict)
