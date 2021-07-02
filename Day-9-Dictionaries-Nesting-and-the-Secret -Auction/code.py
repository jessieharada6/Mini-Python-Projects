# dictionary
# key-value pair
# {key: value, key: value, key: value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
    }

# retrieving items from dictionary
print(programming_dictionary)
print(programming_dictionary["Bug"])

# add new items
programming_dictionary["Loop"] = "Thr action of doing something over and over again"
print(programming_dictionary)

# edit
programming_dictionary["Loop"] = "booo"
print(programming_dictionary)

# loop through dictionary
for key in programming_dictionary:
    print(key) # give you keys: Bug, Function Loop
    print(programming_dictionary[key]) # get values

# init dictionary
empty_dictionary = {}
empty_dictionary["check"] = "woohoo"

# clear dictionary
programming_dictionary = {}


# NESTING
# Nesting lists and dictionaries
# {key: [List], key2: {Dictionary}}

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburge", "Stuttgart"]
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburge", "Stuttgart"], "total_visits": 10} 
}

# Nest dict inside a single list
# list is ordered
# dict is accessed by the key
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburge", "Stuttgart"], 
        "total_visits": 10
    } 
]
