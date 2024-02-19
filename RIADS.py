#
# This is Rados' Item Auction Dnd Software (RIADS) V0.01
#
# This program is licensed under the Beerware License;
# Make all the changed you want, but please share your improvements.
#
# Feel Free to use this program in anyway you want, but do not remove
# the credits
# Original Program by NotRados on Github
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import csv
import random
import threading
import time

##### Variables #####
                    #
chance = 15         # Percent chance of item being valued wrong.
valueChange = 0.40  # Percent change of percieved value.

currentBid = 0      # The current bid of the item.
bidIncrements = 0   # How much each round the bid will increase.
passFlag =  False   # When True, it will skip the time simulations, if players
                    # decide not to bid for the item.
npcPassChance = 0   # Will increase for each bid, until NPCs pass.
npcPassFlag = False # Will remain false until NPCs pass.
auction_active = True


##### Functions #####

# Open CSV and select a random item.
def OpenCSV():
    with open('ItemList.csv', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        items = list(csv_reader)
    random_item = random.choice(items)
    
    print("Item up for Bidding: ", random_item['Name'])
    print("Visual Description: ", random_item['Visual Description'])
    print("\n(ACTUAL ITEM DESCRIPTION)\n", random_item['Real description'])
    
    currentBid = int(random_item['Starting bid'])
    bidIncrements = int(random_item['Minimum Bid'])
    # = int(random_item[''])
    
    return currentBid, bidIncrements


# Decide whether item is over/under priced.
# Set Starting bid and bid increments.
def Valuation(currentBid, bidIncrements):
    if random.randint(0, 100) <= chance:
        if random.randint(0, 100) % 2 == 1:
            print("ITEM HAS BEEN UNDERVALUED")
            currentBid -= currentBid*valueChange
            bidIncrements -= bidIncrements*valueChange
            
        else:
            print("ITEM HAS BEEN OVERVALUED")
            currentBid += (currentBid*valueChange)
            bidIncrements += bidIncrements*valueChange
    else:
        print("item has not been misvalued")

    return currentBid, bidIncrements


# NPC Bid
def NPCBid(currentBid, bidIncrements):
    global npcPassFlag
    global npcPassChance
    global auction_active
    while auction_active and not npcPassFlag:
        time.sleep(random.randint(0, 1))
        if auction_active:  # Check again in case auction ended during sleep
            currentBid += bidIncrements
            print("NPC bids! Current bid is:", currentBid)
            if random.randint(0, 100) <= npcPassChance:
                npcPassFlag = True
                print("No more bids from NPC")
            else:
                npcPassChance += 3
                print("NPC might bid again...")
    pass


# Player Bid
def PlayerBid():
    global currentBid
    global bidIncrements
    global npcPassChance
    global auction_active
    while auction_active:
        player_input = input("bid?...")
        if player_input == True: # if the user enters anything
            currentBid += bidIncrements
            print("Player bids! Current bid is:", currentBid)
            if random.randint(1, 100) <= npcPassChance:
                print("NPCs won't bid anymore.")    
                npcPassChance = 100  # Set high to prevent further NPC bids
            else:
                npcPassChance += 8


# Main function
def main():
    currentBid, bidIncrements = OpenCSV()
    currentBid, bidIncrements = Valuation(currentBid, bidIncrements)
    NPCBid(currentBid, bidIncrements)

    # create threads
    npcThread = threading.Thread(target = NPCBid, args = (currentBid, bidIncrements))
    playerThread = threading.Thread(target = PlayerBid)

    # Start threads
    playerThread.start()
    npcThread.start()

    # End threads
    npcThread.join()
    playerThread.join()
    


main()
