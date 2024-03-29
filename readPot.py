# This module reads the value from the Potentiometer on pin A0

# Import neccessary modules to read from Analog Pin
from machine import Pin, ADC

# This is for testing only, remove this before merging with master
from time import sleep

# Constantly read the potentiometer and print out the values
def getSetting():
	pot = ADC(0).read()
	if pot <= 341:
		return 0
	elif pot > 341 and pot <= 682:
		return 1
	elif pot > 682:
		return 2
