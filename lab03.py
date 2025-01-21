import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# Input combat strength of the hero
try:
    mCombatStrength = int(input("Enter your combat strength (1-6): "))
    if mCombatStrength < 1 or mCombatStrength > 6:
        print("Invalid input. Combat strength should be between 1 to 6.")
        combatStrength = 1  # Default value for invalid input
    else:
        combatStrength = mCombatStrength
except ValueError:
    print("Invalid input. Please enter an integer.")
    combatStrength = 1  # Default value for invalid input

# Simulate Battle rounds
for j in range(1, 21):  # Simulation of 20 rounds
    # Dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Calculate the weapons
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    # Calculate total strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = combatStrength + monsterRoll

    # Print round details
    print(f"\nRound {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}")
    print(f"Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}")

    # Determine winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round!")
    else:
        print("It's a tie!")
    if j == 11:
        print("\n Battle Truce declared in Round 11. Game Over!")
        break
if j != 11:
    print("\n Battle concluded after 20 rounds!")