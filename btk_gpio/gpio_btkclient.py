
import os #used to all external commands
import sys # used to exit the script
import dbus
import dbus.service
import dbus.mainloop.glib
import RPi.GPIO as GPIO
import time
import thread


class BtkGpioClient():

        """GPIO client of the Bluetooth Keyboard Emulator
        Polls the status of a GPIO pin and triggers the emulator to send a single key
        http://yetanotherpointlesstechblog.blogspot.com
        """

        #constants
        PIN=37                          # physical number of GPIO pin to monitor  
        KEYCODE=26                      # w scan code - key code to send. 
        MIN_KEY_TIME=0.001              # minimum delay between key down and key up events to enable key press to be detected
        REPEAT_KEY=True                 # True = repeat key while the pin is enabled. FALSE = send a single key per keypress
        REPEAT_KEY_DELAY=0.001          # delay between repeated key presses when REPEAT_KEY = True


        def __init__(self):

            #the structure for a bt keyboard input report (size is 10 bytes)
                
            self.state=[
                    0xA1, #this is an input report
                    0x01, #Usage report = Keyboard
                    #Bit array for Modifier keys
                    [0, #Right GUI - Windows Key
                     0, #Right ALT
                     0, #Right Shift
                     0, #Right Control
                     0, #Left GUI
                     0, #Left ALT
                     0, #Left Shift
                     0],    #Left Control
                    0x00,   #Vendor reserved
                    0x00,   #rest is space for 6 keys
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00]


            #initialize the GPIO library    
            print "setting up GPIO"

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(BtkGpioClient.PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

                
            #connect with the Bluetooth keyboard server    
            print "setting up DBus Client"  

            self.bus = dbus.SystemBus()
            self.btkservice = self.bus.get_object('org.yaptb.btkbservice','/org/yaptb/btkbservice')
            self.iface = dbus.Interface(self.btkservice,'org.yaptb.btkbservice')    


            #hard code the key to send for this demo
            self.state[4]=BtkGpioClient.KEYCODE

        

        def send_key_state(self):
        
            """sends a single frame of the current key state to the emulator server"""    

            bin_str=""
            element=self.state[2]
            for bit in element:
                    bin_str += str(bit)
            self.iface.send_keys(int(bin_str,2),self.state[4:10]  )


        def send_key_down(self):
        
            """sends a key down event to the server"""    

            self.state[4]=BtkGpioClient.KEYCODE
            self.send_key_state()


        def send_key_up(self):
        
            """sends a key up event to the server"""    

            self.state[4]=0
            self.send_key_state()



        def pin_event(self,channel):


            """RPi.GPIO callback method. called when a GPIO  event occurs on the specified pin

            """    
  

            if(self.key_down==False):
                    print "Key Down"    
                    self.key_down=True
            else:
                    print "Key Up"
                    self.key_down=False
           
            

        def event_loop(self):

            """main loop. sets up the GPIO callback then polls the hit state to detect a key press.
            """
        
            self.key_down=False
            key_up_sent=False    
            key_down_sent=False
            
            GPIO.add_event_detect(BtkGpioClient.PIN, GPIO.BOTH, callback=self.pin_event,bouncetime=250) 

                
            while True:


                if(self.key_down ):

                        #the pin is set on

                        if(BtkGpioClient.REPEAT_KEY and key_down_sent):
                                #finish the current key and repeat        
                                self.send_key_up()
                                key_down_sent=False
                                time.sleep(BtkGpioClient.REPEAT_KEY_DELAY)

                        if(not key_down_sent):
                                #start a key press
                                self.send_key_down()
                                key_down_sent=True


                else:

                        #the pin is set off

                        if(key_down_sent):
                                #finish the key press
                                self.send_key_up()
                                key_down_sent=False


                time.sleep(BtkGpioClient.MIN_KEY_TIME)  #seems like the minimum delay required for a keypress to be registered


if __name__ == "__main__":

    print "Setting up GPIO Bluetooth kb emulator client"

    dc = BtkGpioClient()

    print "starting event loop"
    dc.event_loop()

    
