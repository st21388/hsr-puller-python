"""
Written by: Surya.A
Component 1: Version 1:
Create a purely text-based program for the initial rate calculator.
Calculates rates for 4 stars and 5 stars. 4 stars have a constant rate of 5.1%
until guaranteed every 10 pulls (on the 10th pull). 5 stars have a constant rate
of 0.6% until warp 74 where it increases by 6% until 90 pulls where it overcaps
at 102.6%. When at 10 pulls and a both a 4 star and five star is won, the 5 star
takes priority and the 4 star will be erased. After winning a 5 star warp count
is reset to 0.

Component 1: Version 2:
For the frame that shows history of every pull, we need to store the 4* and 5*
pity for every individual pull. The way we will accomplish this is by changing
the history list to a 2d list that stores the 4* and 5* pity alongside its
rarity. E.g, [[3, 65, 8], [3, 66, 9], [4, 67, 10]] etc.

This version uses jsons to store every individual pull. This is so that when
implementing the GUI the reward frame can show the previous 10 pulls and so that
the history button can show the previous 300 pulls.
"""
import json
import random

def get_rate_4_star(warp):
    if warp == 10: # 10 pulls is guaranteed 4 star
        return 1.1
    else:
        return 0.051

def get_rate_5_star(warp):
    # base rate same until we reach 74th pull
    if warp < 74:
        return 0.006
    
    # after 73th pull, the rate increase 6% per pull until 90 pull
    elif warp <= 90 and warp >= 74:
        return (warp - 73) * 0.06 + 0.006

def roll(rate_four, rate_five): # the current rate (account for pity) and the type of rarity (4* or 5*)
    win = False # set the win condition to false
    if (rate_four*100) > random.uniform(0.0,100.0) and (rate_five*100) > random.uniform(0.0,100.0):
        return "5&4"
    elif (rate_five*100) > random.uniform(0.0,100.0):
        return "5"
    elif (rate_four*100) > random.uniform(0.0,100.0):
        return "4"

def pull(): # function for pulling
    data["warp_4"] += 1 # increment 4 & 5 star pity count by 1
    data["warp_5"] += 1
    rate_4 = get_rate_4_star(data["warp_4"]) # calculate the rates
    rate_5 = get_rate_5_star(data["warp_5"])
    
    outcome = roll(rate_4,rate_5) # roll the dice
    if outcome == "5&4": # if both 5 and 4 star win, discard 4 star
        '''append data as (rarity, 5* pity, 4* pity)'''
        data["history"].append([5,data["warp_5"],data["warp_4"]])
        data["warp_5"] = 0
        data["warp_4"] = 0
        print("5 STAR WIN!")
    elif outcome == "5": # if 5 star win, reset 5* pity not 4 star
        data["history"].append([5,data["warp_5"],data["warp_4"]])
        data["warp_5"] = 0
        print("5 STAR WIN!")
    elif outcome == "4": # if 4 star win, reset 4* pity not 5 star
        data["history"].append([4,data["warp_5"],data["warp_4"]])
        data["warp_4"] = 0
        print("4 STAR WIN!")
    else: # else, then 3 star was won
        data["history"].append([3,data["warp_5"],data["warp_4"]])
        print("3 STAR")
    
    if len(data["history"]) == 300:
        data["history"].pop(0) # history can not store over 300 pulls    

# open and load the list in the json into variable named data
with open("history.json") as f:
    data = json.load(f)

while True:
    pull_number = input("Enter 1x or 10x roll: ") # get number of pulls

    if pull_number == "1": # for single pulls
        pull()

    if pull_number == "10": # for 10x pulls
        for i in range(0,10,1):
            pull()

    if pull_number == "clear": # debug for clearing the history.json dictionary
        data = {"history": [], "warp_4": 0, "warp_5": 0}


    with open("history.json", 'w') as f:
        json.dump(data, f, indent=1)