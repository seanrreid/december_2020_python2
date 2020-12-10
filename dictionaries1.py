meal = {
    "drink": "beer",
    "appetizer": "nachos",
    "entree": "tacos",
}

if "dessert" in meal:
    print("For dinner I'm having %s with %s to drink and %s for dessert!" % (meal["entree"], meal["drink"], meal["dessert"]))
else:
    print("For dinner I'm having %s with %s to drink!" % (meal["entree"], meal["drink"]))

