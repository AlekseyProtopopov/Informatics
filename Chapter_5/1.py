sea_fish = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

combined_fish = sea_fish + freshwater_fish

sorted_fish = sorted(combined_fish, key=lambda fish: fish.lower())

print(sorted_fish)
