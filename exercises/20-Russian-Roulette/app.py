import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position
result = spin_chamber() 

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
    result = spin_chamber
    if bullet_position == spin_chamber:
        return("You are dead!")
    else:
        return("Keep playing!")



print(fire_gun())