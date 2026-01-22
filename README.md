# Monopoly_of_Traders
🎩 Monopoly of Traders
Monopoly of Traders is a Python-based command-line strategy game where players compete to become the wealthiest merchant. Navigate a fluctuating market, manage your stock, and out-trade your opponents to claim victory.

🎮 Game Overview
In this game, players start with 100 coins and must navigate a series of rounds. Each round, market prices for various commodities change and global stock levels shift. Your goal is simple: buy low, sell high, and finish with more coins than anyone else.

Tradable Resources
🪵 Wood

⚙️ Iron

🏗️ Stainless Steel

⛽ Petrol

🥈 Silver

🥇 Gold

💎 Diamond

✨ Features
Multiplayer Support: Play with as many friends as you like.

Dynamic Market: Prices and global stock levels are randomized every round, requiring constant strategy shifts.

Fuzzy Input Matching: Powered by rapidfuzz, the game understands your commands even if you make minor typos (e.g., "dimond" instead of "diamond").

Shared Market: All players trade from the same global stock in a single round—if one player buys all the gold, there's none left for you!

🛠️ Requirements
To run this game, you need:

Python 3.x

rapidfuzz library

Install the dependency via pip:

Bash

pip install rapidfuzz
🚀 How to Run
Download the Monopoly Of Traders.py file.

Open your terminal or command prompt.

Run the script:

Bash

python "Monopoly Of Traders.py"
📝 Rules of the Trade
Setup: Enter the number of players and names. Choose how many rounds the game will last.

Turn Actions: On your turn, you can Buy, Sell, or Skip.

Inventory Management: You cannot sell what you don't have, and you cannot buy more than what is available in the market's current stock.

Winning: Once all rounds are complete, the player with the highest number of coins is declared the winner.

🏗️ Future Roadmap (Planned Features)
[ ] Add a Save/Load game feature.

[ ] Implement "Market Events" (e.g., a "War" event that spikes Petrol prices).

[ ] GUI version using Tkinter or Pygame.

Developed by Parth Feel free to fork this project and add your own trading mechanics!
