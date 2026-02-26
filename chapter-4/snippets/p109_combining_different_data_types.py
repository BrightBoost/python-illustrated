cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}


cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna",
    "hobbies": ["napping", "programming", "playing"]
}

print(cat_attributes["hobbies"])

print(cat_attributes["hobbies"][1])



cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna",
    "hobbies": ["napping", "programming", "playing"],
    "friends": [],
}



cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna",
    "hobbies": ["napping", "programming", "playing"],
    "friends": [{"name": "Wiesje", "age": 7}]
}

print(cat_attributes["friends"][0]["name"])



cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna",
    "hobbies": ["napping", "programming", "playing"],
    "friends": [
        {
            "name": "Wiesje",
            "age": 7
        }
    ]
}


cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna",
    "hobbies": ["napping", "programming", "playing"],
    "friends": [
        {
            "name": "Wiesje",
            "age": 7,
            "hobbies": ["napping", "visiting the forest"]
        }
    ]
}

print(cat_attributes["friends"][0]["hobbies"][1])



cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna",
    "hobbies": ["napping", "programming", "playing"],
    "friends": [
        {
            "name": "Wiesje",
            "age": 7,
            "hobbies": ["napping", "visiting the forest"]
        },
        {
            "name": "Muchu",
            "age": 0,
            "hobbies": [
                "napping in the couch",
                "chasing anything",
                "exploring new things"
            ] 
        }
    ]
}

print(cat_attributes["friends"][1]["name"], "loves", 
cat_attributes["friends"][1]["hobbies"][0])

print(cat_attributes["friends"][1])
