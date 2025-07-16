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
"""
from random import *

#initialize constants
WARP_4 = 0
WARP_5 = 0

def get_rate_4_star(warp):
    pass
    if warp >= 10:
        tens_digit, ones_digit = divmod(warp, 10)
        if ones_digit == 0:
            return 1
        else:
            return 0.51
    else:
        return 0.51

def get_rate_5_star(warp):
    # base rate same until we reach 74th pull
    if warp < 74:
        return 0.06
    
    # after 73th pull, the rate increase 6% per pull until 90 pull
    elif warp <= 90 and warp >= 74:
        return (warp - 73) * 0.06 + 0.006
    
while True:    
    pull_number = int(input("Enter 1x or 10x pull: "))
    if pull_number == 1:
        WARP_4 += 1 # increment warp count of both rarities by 1
        WARP_5 += 1
        print(WARP_4) # print the warps so we know for testing
        print(WARP_5)
        rate_4 = get_rate_4_star(WARP) # run 4 star rate calculator
        print(rate_4) # print rate
        rate_5 = get_rate_5_star(WARP) # same for 5 star
        print(rate_5)
    elif pull_number == 10:
        WARP_4 += 10 # increment warp count of both rarities by 10
        WARP_5 += 10
        print(WARP)
        rate_4 = get_rate_4_star(WARP)
        print(rate_4)
        rate_5 = get_rate_5_star(WARP)
        print(rate_5)
    
    # do a random number from 1 - 100, check the number is lower than the rate (e.g random pulls 0.5 and the rate is 0.6 its a win)
    if (rate_5*100) > random(0.0,100.0):
        print("5 STAR WIN")
        WARP = 0 # reset warp to 0
    else:  # losing scenario