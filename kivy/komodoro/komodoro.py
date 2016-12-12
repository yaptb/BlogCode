#
#Kivy Pomodoro-like Application
#http://yetanotherpointlesstechblog.blogspot.com
#

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class Timer:
    
    """  a service that manages the time keeping logic for the
    application """


    TOTALTIME=15*60         #total time for a coutn down
    timerRunning=False      #flag. True if the clock is running
    elapsedTimeSecs=0       #the number of seconds that have elapsed
    

    def startTimer(self):
        self.timerRunning =True

    def stopTimer(self):
        self.timerRunning = False

    def resetTimer(self):
        self.elapsedTimeSecs=0

    def tick(self):

        """updates the start of the timer.
        this method expects to be called once per second"""
        
        if(self.timerRunning):
            self.elapsedTimeSecs = self.elapsedTimeSecs+1

    def getTimeRemaining(self):

        """returns the amount of time remaining on the count down
        as a tuple (minutes, seconds)"""
        
        timeRemainingSecs = self.TOTALTIME-self.elapsedTimeSecs
        if(timeRemainingSecs<0):
            timeRemainingSecs=0

        minutes = int(timeRemainingSecs/60)
        seconds = int(timeRemainingSecs-minutes*60)
        
        return (minutes, seconds)

    def checkComplete(self):
        """returns true if the countown has finished"""
        (mins,secs)= self.getTimeRemaining()
        if( mins==0 and secs==0):
            return True
        else:
            return False
            

class KomodoroMain(Widget):

        """  the root widget controller for our application"""


        timer = Timer()     # instantiates the timer service


        #object properties are used by Kivy to bind
        #widgets defined in *.kv files so that they
        #can be accessed from python.
        
        displayLabel = ObjectProperty(None) #the count down display
        startButton = ObjectProperty(None)  #the start button
        stopButton = ObjectProperty(None)   #the stop button


        def update(self, stuff):
            """this method is a callback method that is called by the
            kivy scheduler one a second"""

            #update the timer service
            self.timer.tick()

            #if we have finished the countdown, notify the user
            #else display the time remaining
        
            if( self.timer.checkComplete()):
                self.displayLabel.text="Finished!"
            else:
                (mins,secs)=self.timer.getTimeRemaining()
                smins='{0:02d}'.format(mins)
                ssecs='{0:02d}'.format(secs)
                self.displayLabel.text=smins+':'+ssecs


        def btnStart_OnPress(self, value):
            self.timer.startTimer()
            self.startButton.disabled=True
            self.stopButton.disabled=False
        
        def btnStop_OnPress(self, value):
            self.timer.stopTimer()
            self.startButton.disabled=False
            self.stopButton.disabled=True

        def btnReset_OnPress(self, value):
            self.timer.resetTimer()



class KomodoroApp(App):

        """creates a subclass of the Kivy App class to define our
        program as a Kivy application """

    
        def build(self):
            """called from Kivy. Build and return the root widget for
            our application and schedule updates every second"""
            main=KomodoroMain()
            Clock.schedule_interval(main.update, 1.0)
            return main

if __name__== '__main__':
    KomodoroApp().run()

    
