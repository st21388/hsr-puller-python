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

# open and load the list in the json into variable named data
with open("history.json") as f:
    data = json.load(f)

while True:
    pull_number = int(input("Enter 1x or 10x roll: "))
    if pull_number == 1:
        rate_4 = get_rate_4_star(data["warp_4"])