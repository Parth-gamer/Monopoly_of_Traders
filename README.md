🎩 Monopoly of Traders
Monopoly of Traders is a strategic command-line trading simulator. Players compete to accumulate the most wealth by navigating a volatile market of raw materials and precious metals.

🎮 Game Flow
Starting Capital: Every player begins the game with 100 coins.

Market Dynamics: Each round, the "Buy" prices, "Sell" prices, and "Stock" levels for all resources are randomized.

Turn Options: During their turn, a player may choose to buy, sell, or skip.

Shared Economy: All players trade from a global stock; once a resource is bought by one player, it is removed from the market for others during that round.

Winning Condition: The winner is the player with the highest coin count after the final round is completed.

📦 Tradable Resources
Players can buy and sell the following materials:

🌳 wood

⚙️ iron

🏗️ stainless steel

⛽ petrol

🥈 silver

🥇 gold

💎 diamond

✨ Key Mechanics
Fuzzy Input Recognition: The game utilizes the rapidfuzz library to handle user typos and approximate string matching for actions and resources.

Validation: Built-in logic prevents players from overdrawing coins, selling non-existent inventory, or purchasing beyond market stock.

Multiplayer: Supports a custom number of players with unique name entry.

🛠️ Technical Stack
Language: Python 3.

Dependencies: rapidfuzz.

Core Modules: random.

Developed by Parth
