# Dictionary
footballer= {
    "name": "Mbuemo",
    "age": 25,
    "height": 175,
    "gender": "male",
    "position": "RWF",
    "bio": {
        "country": "Cameroon",
        "marital_status": "married",
        "current_club": "Manchester United",
        "is_injured": False
    }
}

sentence_with_concatenation = footballer["name"] + " " + "is a great goal scorer for" + " " + footballer["bio"]["current_club"]

sentence_with_interpolation = f"{footballer["name"]} is a great goal scorer for {footballer["bio"]["current_club"]}"

# print("concatenation:", sentence_with_concatenation)
# print("interpolation:", sentence_with_interpolation)

# updating a specific key in a dictionary
footballer["position"] = "RWF, CF, ST" 

#  adding a new key to a dictionary
footballer["jersey_number"] = 19

#  deleting a key and its value in a dictionary
del footballer["bio"]["is_injured"]
footballer.clear()

# print(footballer)

# list
list = ["dapo", "covenant", "joseph","jesse", [1,2,["ate", False, ["go ghana"]]], True, 45]

deep = ["item", False, [4,14,2,9,[1,[2, "jesse"]]]], "wish", ["arsenal", "football", {"league_structure": ["20", "champions league"]}]

print(list [4][2][2][0])
print(deep[2][4][1][1])
print(deep[4][2]["league_structure"][1])