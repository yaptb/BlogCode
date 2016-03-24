
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
        KEYCODE=26 # w scan code

        def __init__(self):

            #the structure for a bt keyboard input report (size is 10 bytes)

            self.state=[
                    0xA1, #this is an input report
                    0x01, #Usage report = Keyboard
                    #Bit array for Modifier keys
                    [0,	#Right GUI - Windows Key
                     0,	#Right ALT
                     0, #Right Shift
                     0, #Right Control
                     0,	#Left GUI
                     0, #Left ALT
                     0,	#Left Shift
                     0],	#Left Control
                    0x00,	#Vendor reserved
                    0x00,	#rest is space for 6 keys
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00]


            print "setting up GPIO"

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(DeskCycle.PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

            print "setting up DBus Client"	

            self.bus = dbus.SystemBus()
            self.btkservice = self.bus.get_object('org.yaptb.btkbservice','/org/yaptb/btkbservice')
            self.iface = dbus.Interface(self.btkservice,'org.yaptb.btkbservice')	


            #hard code the key to send
            self.state[4]=DeskCycle.KEYCODE

        
   	def send_key_state(self):

            bin_str=""
            element=self.state[2]
            for bit in element:
                    bin_str += str(bit)
            self.iface.send_keys(int(bin_str,2),self.state[4:10]  )


        def send_keys(self, num_keys, inter_key_delay, key_press_delay):
            
            for x in range(1,num_keys):
                self.state[4]=DeskCycle.KEYCODE
                self.send_key_state()
                time.sleep(key_press_delay)
                self.state[4]=0
                self.send_key_state()
                time.sleep(inter_key_delay)

    	def pin_event(self,channel):
            self.hitCount+=1
            self.last_hit_time = time.time()
            print "Hit",time.time(), self.hitCount
            


        def event_loop(self):

        
            self.keyDown=False
	    self.hitCount=0	
                

            keys_per_rev=5
            key_press_delay=0.2
            inter_key_delay=0.001

            self.last_hit_time=0
            self.current_hit_time=0
            self.rev_time=0.5
            
            GPIO.add_event_detect(DeskCycle.PIN, GPIO.FALLING, callback=self.pin_event,bouncetime=250) 

                
            while True:


                if(self.hitCount >0):

                        if(not self.keyDown):
                            print "On"    
                            self.state[4]=DeskCycle.KEYCODE
                            self.send_key_state()
                            self.keyDown=True

                        self.hitCount=0

                else:
                        if(self.keyDown):

                                if(time.time()-self.last_hit_time > 1):
                                        print "Off"    
                                        self.state[4]=0
                                        self.send_key_state()
                                        self.keyDown=False

                time.sleep(0.001)


if __name__ == "__main__":

	print "Setting up desk cycle"

	dc = DeskCycle()

	print "starting event loop"
	dc.event_loop()

	
