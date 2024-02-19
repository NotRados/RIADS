# RIADS

Welcome to Rados' Item Auction (Dnd) Software!
Could I have chosen a better name? probably.

## What it does
This program simulates auction process for D&D items that it takes from the CSV file.
### Steps:
1. Select a random item from the CSV file.
2. Determine whether the item is under/over-valued, or neither.
3. if mis-valued, change the percieved value and starting bid.
4. Start Bidding:
    1. randomly choose if NPC bids
    2. if NPC bids, increase current bid
    3. decrease chance of NPC bidding
    The user can press the button to also bid.
5. display final bid
6. ask if the program should take another item.

## CSV File
The file can be changed using a text editor if you're bothered, or by using a spreadsheet editor on the ItemList.xlsx file, and exporting as .csv
### Fields contain:
ItemId - ID
Name - Name of the item
value - Real value of the item
Starting bid - standard starting bid.
Visual Description - What it looks like to the players
Real description - DND description, what it's used for, what dice to roll, etc.
Minimum Bid - The value that the bid will increase by
Item Image - URL to image, if exists.
Rarity - Rarity of object; common, rare, wonderous
Type - Weapon, potion, bag, etc.


# THIS PROGRAM IS STILL UNDER CONSTRUCTION!
### Known Issues:
- no gui
- threading not working as intended.
- no buttons to skip auction
- bid increments need to be rounded to nearest 1, 5, 10 or multiple of 50
