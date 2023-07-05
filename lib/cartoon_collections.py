def roll_call_dwarves(names):
    for i in range (len(names)):
        print (f"{i+1}. {names[i]}")
    pass

def summon_captain_planet(planeteers):
    return [planeter.capitalize()+'!' for planeter in planeteers]
    pass

def long_planeteer_calls(planeteers):
    for planeteer in planeteers:
        if len(planeteer) > 4:
            return True
    return False
    pass

def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None
    pass
