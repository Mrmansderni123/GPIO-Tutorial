import RPi.GPIO as pi # Import Gpio Package
import time # Import Time delay Package



pi.setmode(pi.BCM)##Set up gpio numbering

pi.setwarnings(False) ## Turn off warnings

pi.setup(21,pi.OUT)## Setup Gpio #21 for output


##pi.setup(16,pi.OUT)## Setup Gpio #16 for output
##pi.setup(23,pi.OUT)## Setup Gpio #23 for output
##pi.setup(18,pi.OUT)## Setup Gpio #18 for output



##Gpio 21
pi.output(21,True)## Turn Gpio #19 on
print('Gpio 21 on')
time.sleep(1)## Pause one second
pi.output(21,False)## Turn Gpio # 19 off






####Gpio 16
##pi.output(16,True)## Turn Gpio #16 on
##print('Gpio 16 on')
##time.sleep(1)## Pause one second
##pi.output(16,False)## Turn Gpio # 16off
##
####Gpio 23
##pi.output(23,True)## Turn Gpio #23 on
##print('Gpio 23 on')
##time.sleep(1)## Pause one second
##pi.output(23,False)## Turn Gpio # 23 off
##
####Gpio 18
##pi.output(18,True)## Turn Gpio #18 on
##print('Gpio 18 on')
##time.sleep(1)## Pause one second
##pi.output(18,False)## Turn Gpio # 18 off
##
##print('Leds off')

