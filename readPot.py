# This module reads the value from the Potentiometer on pin A0

# Import neccessary modules to read from Analog Pin
from machine import Pin, ADC

# This is for testing only, remove this before merging with master
from time import sleep

# Constantly read the potentiometer and print out the values
def getSetting():
	return ADC(0).read()
