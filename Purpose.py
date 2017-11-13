#!/usr/bin/env python
import time
import random

this_year = 0
i_live = True
inspired = True
still_searching = True
chance = 0		# Needs to not be a constant
health = .8

my_purpose = 'tbd'
life = ["find love", "honor", "earn a doctorate", "go to college"] # Include more life goals
to_ancestors = 0
days = .01


def this_life(destiny):
	my_purpose = destiny in life

	while(i_live):
		keep_searching()
		for meaning in life:
			meaningful = meaning
			
			if my_purpose is meaningful:
				still_searching = False
				return to_ancestors

			else:
				continue

def keep_searching():
	next_year = this_year + 1

	if still_alive() is False:
		i_live = False
	else:
		i_live = True

	#if(inspired):
	# 	determination = len(life)
	#	opportunity = 20
	#	my_purpose = life[inspired*destiny + opportunity % determination]

	if i_live and still_searching:
		print("Another year... another chance")
		time.sleep(365.25 * days)
	
	elif still_searching:
		print("Another life... another chance")
		begin_life()

def begin_life():
	this_year = 0
	i_live = True
	destiny = life[chance]		# Need to change chance
	this_life(destiny)

def still_alive():
	if(random.random() < health ):
		return i_live
	else:
		return not i_live

begin_life()