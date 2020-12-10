meal = {
    "drink": "beer",
    "appetizer": "nachos",
    "entree": "tacos",
    "dessert": "churros"
}

print(meal)

meal["drink"] = "green tea"

if "water" in meal:
    del meal["water"]

print(meal)