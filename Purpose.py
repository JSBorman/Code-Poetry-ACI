#!/usr/bin/env python
import time
from random import random, randint
import os

base1, base2 = -1, 0
i_live, still_searching = True, True

life = ["Purpose", "Adventure", "Nature", "Challenge", "Opportunity", "Love", "Give", "Change"]
possibilities = len(life) - 1

to_ancestors = life.index("Purpose")
inspired, determined = [ord(steps[to_ancestors]) for steps in ["Inspired","Determined"]]

def this_life(destiny, this_year):
	my_purpose = destiny in life

	while(i_live):
		keep_searching(this_year)
		for meaning in life:
			meaningful = meaning
			
			if my_purpose is meaningful:
				still_searching = False
				os.exit(to_ancestors)

def keep_searching(this_year):
	next_year = this_year + 1

	if inspired is determined:
		my_purpose = life[ (inspired*determined/destiny) % possibilities]

	if i_am_alive() and still_searching:
		print("Another chance")
		time.sleep(365.25 * days())
	
	elif still_searching:
		print("Another life...")
		begin_life()

def i_am_alive():
	illness = random()
	condition = len(life) * days() * genetics()
	
	if(illness > condition ):
		return not i_live
	return i_live

def begin_life():
	this_year = 0
	i_live = True
	chance = randint(0, possibilities)
	destiny = life[chance]
	this_life(destiny, this_year)

def days():
	return float("." + str(base2) + str(base1**base2))
def genetics():
	return float(str(base1**base2) + str(base2)) 

begin_life()