"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
"""


def score(dice):
    s = 0
    if dice.count(1) >= 3:
        s += 1000
        s += int(dice.count(1) - 3) * 100
    elif dice.count(1) < 3:
        s += int(dice.count(1)) * 100
    if dice.count(2) == 3:
        s += 200
    if dice.count(3) == 3:
        s += 300
    if dice.count(4) == 3:
        s += 400
    if dice.count(5) >= 3:
        s += 500
        s += int(dice.count(5) - 3) * 100
    elif dice.count(5) < 3:
        s += int(dice.count(5)) * 50
    if dice.count(6) == 3:
        s += 600
    return s
