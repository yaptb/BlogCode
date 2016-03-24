
import os #used to all external commands
import sys # used to exit the script
import dbus
import dbus.service
import dbus.mainloop.glib
import RPi.GPIO as GPIO
import time
import thread


class DeskCycle():

        PIN=40
    
        def __init__(self):

    
            print "setting up GPIO"

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(DeskCycle.PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            
            self.hitCount=0

            pin2=38
            GPIO.setup(pin2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(pin2, GPIO.FALLING, callback=self.pin_2_event,bouncetime=100) 

        def pin_2_event(self,channel):
        
            print("OI!")
       
        def pin_event(self,channel):
            self.hitCount+=1
       

        def event_loop(self):

            count =0

            keys_per_rev=5
            key_press_delay=0.05
            inter_key_delay=0.1
            last_time=0
            current_time=0

            GPIO.add_event_detect(DeskCycle.PIN, GPIO.FALLING, callback=self.pin_event,bouncetime=100) 

            while True:

                if(self.hitCount >0):
                    count+=1
                    print "Hit ",count
                    self.hitCount-=1

                time.sleep(0.01)

if __name__ == "__main__":

	print "Setting up desk cycle"

	dc = DeskCycle()

	print "starting event loop"
	dc.event_loop()

	
