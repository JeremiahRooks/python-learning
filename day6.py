player_level = 40
required_level = 40

if player_level >= required_level:
    print("You can access this area.")
else:
    print("You need to level up before accessing this area.")



total_spent = 150
discount_requirement = 100

if total_spent >= discount_requirement:
    print("Discount Unlocked!")
else:
    print("Spend more to unlock a discount.")


invetory_weight = 50
weight_limit = 100

if invetory_weight <= weight_limit:
    print("You can cross the bridge.")
else:
    print("Your inventory is too heavy.")


player_health = 20
if player_health >= 70:
    print("Health is good")
elif player_health >= 30:
    print("Health is low")
else:
    print("Health is critical!")


player_level = 15
if player_level >= 50:
    print("Rank: Elite")
elif player_level >= 30:
    print("Rank: Advanced")
elif player_level >= 15:
    print("Rank: Intermediate")
else:
    print("Rank: Beginner")