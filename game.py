player = {"name": "slo", "attack": 10, "heal": 16, "health": 100}
monster = {"name": "geza", "attack": 12, "health": 100}

print("Please select action")
print("1. Attack")
print("2. Heal")

player_choice = input()

if player_choice == "1":
    print("Attack")
