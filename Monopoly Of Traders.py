import random
from rapidfuzz import process

print('WELCOME TO MONOPOLY OF TRADERS')
print('In this game, you will have 100 coins, with which you can buy wood, iron, stainless steel, petrol, silver, gold and diamond.')
print('There may be as many rounds as you will want. In each round you will get info about the current prices and the amount of material in stock.')
print('You can buy or sell the materials to earn money.')
print('The person with the maximum coins will be the winner after all the rounds have completed')

# Valid lists
actions = ["buy", "sell", "skip"]
resources = ["wood", "iron", "stainless steel", "silver", "petrol", "gold", "diamond"]

# Fuzzy match helper
def nearest_match(user_input, valid_list, threshold=60):
    match = process.extractOne(user_input, valid_list)
    if match and match[1] >= threshold:
        return match[0].lower()
    return None

# Input players
while True:
    try:
        no_of_players = int(input('Enter no. of players: '))
        if no_of_players > 0:
            break
        else:
            print("Please enter a positive number of players.")
    except ValueError:
        print("Invalid number. Please enter an integer.")

players = []
coins = []
inventory = []

for i in range(no_of_players):
    name = input(f'Enter name for player {i+1}: ').strip()
    if not name:
        name = f'Player{i+1}'
    players.append(name)
    coins.append(100)  # each player starts with 100 coins
    inventory.append({res: 0 for res in resources})

print("Players are:", players)

# Input rounds
while True:
    try:
        n = int(input('Enter the no. of rounds: '))
        if n > 0:
            break
        else:
            print("Please enter a positive number of rounds.")
    except ValueError:
        print("Invalid number. Please enter an integer.")

for round_no in range(1, n+1):
    print(f"\n--- Round {round_no} ---")

    # Shared market prices and stock for this round
    gold_buy_price = random.randint(95, 115)
    wood_buy_price = random.randint(5, 30)
    iron_buy_price = random.randint(30, 70)
    diamond_buy_price = random.randint(100, 300)
    stainless_steel_buy_price = random.randint(35, 75)
    petrol_buy_price = random.randint(15, 45)
    silver_buy_price = random.randint(60, 100)

    gold_sell_price = random.randint(100, 165)
    wood_sell_price = random.randint(20, 45)
    iron_sell_price = random.randint(40, 85)
    diamond_sell_price = random.randint(150, 350)
    stainless_steel_sell_price = random.randint(45, 90)
    petrol_sell_price = random.randint(25, 55)
    silver_sell_price = random.randint(75, 120)

    gold_stock = random.randint(0, 5)
    wood_stock = random.randint(0, 20)
    iron_stock = random.randint(0, 10)
    diamond_stock = random.randint(0, 2)
    stainless_steel_stock = random.randint(0, 12)
    petrol_stock = random.randint(0, 15)
    silver_stock = random.randint(0, 10)

    # Function to show current market
    def show_market():
        print('\nCurrent Market:')
        print('Gold buy:', gold_buy_price, '          | Sell:', gold_sell_price, '| Stock:', gold_stock)
        print('Wood buy:', wood_buy_price, '           | Sell:', wood_sell_price, ' | Stock:', wood_stock)
        print('Iron buy:', iron_buy_price, '           | Sell:', iron_sell_price, ' | Stock:', iron_stock)
        print('Diamond buy:', diamond_buy_price, '       | Sell:', diamond_sell_price, '| Stock:', diamond_stock)
        print('Stainless Steel buy:', stainless_steel_buy_price, '| Sell:', stainless_steel_sell_price, ' | Stock:', stainless_steel_stock)
        print('Silver buy:', silver_buy_price, '| Sell:', silver_sell_price, '| Stock:', silver_stock)
        print('Petrol buy:', petrol_buy_price, '| Sell:', petrol_sell_price, '| Stock:', petrol_stock)

    show_market()

    # Each player acts in turn with shared stock
    for p in range(no_of_players):
        print(f"\n{players[p]}'s turn")
        print("Coins:", coins[p], "Inventory:", inventory[p])

        # Persistent loop for action
        while True:
            action_input = input("Do you want to buy, sell, or skip? ").strip().lower()
            action = nearest_match(action_input, actions)
            if action:
                break
            else:
                print("Invalid action. Please type buy, sell, or skip.")

        if action == "buy":
            # Persistent loop for resource
            while True:
                res_input = input("Which resource? (wood/iron/stainless steel/silver/petrol/gold/diamond): ").strip().lower()
                res = nearest_match(res_input, resources)
                if res:
                    break
                else:
                    print("Invalid resource. Please try again.")

            # Quantity input
            while True:
                try:
                    amt = int(input("How many units? "))
                    if amt > 0:
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid quantity. Please enter a number.")

            # Buying logic
            if res == "wood" and amt <= wood_stock:
                cost = wood_buy_price * amt
                if coins[p] >= cost:
                    coins[p] -= cost
                    inventory[p]["wood"] += amt
                    wood_stock -= amt
                    print(players[p], "bought", amt, "wood.")
                else:
                    print("Not enough coins!")
            elif res == "iron" and amt <= iron_stock:
                cost = iron_buy_price * amt
                if coins[p] >= cost:
                    coins[p] -= cost
                    inventory[p]["iron"] += amt
                    iron_stock -= amt
                    print(players[p], "bought", amt, "iron.")
                else:
                    print("Not enough coins!")
            elif res == 'stainless steel' and amt <= stainless_steel_stock:
                cost = stainless_steel_buy_price * amt
                if coins[p] >= cost:
                    coins[p] -= cost
                    inventory[p]['stainless steel'] += amt
                    stainless_steel_stock -= amt
                    print(players[p], "bought", amt, "stainless steel")
                else:
                    print('Not enough coins')
            elif res == 'silver' and amt <= silver_stock:
                cost = silver_buy_price * amt
                if coins[p] >= cost:
                    coins[p] -= cost
                    inventory[p]['silver'] += amt
                    silver_stock -= amt
                    print(players[p], "bought", amt, "silver")
                else:
                    print('Not enough coins')
            elif res == 'petrol' and amt <= petrol_stock:
                cost = petrol_buy_price * amt
                if coins[p] >= cost:
                    coins[p] -= cost
                    inventory[p]['petrol'] += amt
                    petrol_stock -= amt
                    print(players[p], "bought", amt, "petrol")
                else:
                    print('Not enough coins')
            elif res == "gold" and amt <= gold_stock:
                cost = gold_buy_price * amt
                if coins[p] >= cost:
                    coins[p] -= cost
                    inventory[p]["gold"] += amt
                    gold_stock -= amt
                    print(players[p], "bought", amt, "gold.")
                else:
                    print("Not enough coins!")
            elif res == "diamond" and amt <= diamond_stock:
                cost = diamond_buy_price * amt
                if coins[p] >= cost:
                    coins[p] -= cost
                    inventory[p]["diamond"] += amt
                    diamond_stock -= amt
                    print(players[p], "bought", amt, "diamond.")
                else:
                    print("Not enough coins!")
            else:
                print("Invalid resource or not enough stock.")

        elif action == "sell":
            # Persistent loop for resource
            while True:
                res_input = input("Which resource? (wood/iron/stainless steel/silver/petrol/gold/diamond): ").strip().lower()
                res = nearest_match(res_input, resources)
                if res:
                    break
                else:
                    print("Invalid resource. Please try again.")

            # Quantity input
            while True:
                try:
                    amt = int(input("How many units? "))
                    if amt > 0:
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid quantity. Please enter a number.")

            # Selling logic
            if res == "wood" and amt <= inventory[p]["wood"]:
                inventory[p]["wood"] -= amt
                coins[p] += wood_sell_price * amt
                wood_stock += amt
                print(players[p], "sold", amt, "wood.")
            elif res == "iron" and amt <= inventory[p]["iron"]:
                inventory[p]["iron"] -= amt
                coins[p] += iron_sell_price * amt
                iron_stock += amt
                print(players[p], "sold", amt, "iron.")
            elif res == "stainless steel" and amt <= inventory[p]["stainless steel"]:
                inventory[p]["stainless steel"] -= amt
                coins[p] += stainless_steel_sell_price * amt
                stainless_steel_stock += amt
                print(players[p], "sold", amt, "stainless steel")
            elif res == "silver" and amt <= inventory[p]["silver"]:
                inventory[p]["silver"] -= amt
                coins[p] += silver_sell_price * amt
                silver_stock += amt
                print(players[p], "sold", amt, "silver.")
            elif res == "petrol" and amt <= inventory[p]["petrol"]:
                inventory[p]["petrol"] -= amt
                coins[p] += petrol_sell_price * amt
                petrol_stock += amt
                print(players[p], "sold", amt, "petrol.")
            elif res == "gold" and amt <= inventory[p]["gold"]:
                inventory[p]["gold"] -= amt
                coins[p] += gold_sell_price * amt
                gold_stock += amt
                print(players[p], "sold", amt, "gold.")
            elif res == "diamond" and amt <= inventory[p]["diamond"]:
                inventory[p]["diamond"] -= amt
                coins[p] += diamond_sell_price * amt
                diamond_stock += amt
                print(players[p], "sold", amt, "diamond.")
            else:
                print("Not enough inventory!")

        elif action == "skip":
            print(players[p], "skipped this round.")

        # Show updated market after each player's action
        show_market()

# Final results
print("\n--- Game Over ---")
for p in range(no_of_players):
    print(players[p], "has", coins[p], "coins and inventory:", inventory[p])

winner_index = coins.index(max(coins))
print("\n🏆 Winner is", players[winner_index], "with", coins[winner_index], "coins!")