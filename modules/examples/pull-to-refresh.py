#From https://omz-forums.appspot.com/pythonista/post/5906241792507904
#Text drawing may not be very good yet, but I am working on it :)
# Pull down to refresh.
# By Shambhala, for Pythonista

from scene import *
import sound

class MyScene (Scene):
    def setup(self):
        self.sw, self.sh = self.size.w, self.size.h
        self.ssh = self.sh # Top of page.
        self.tch = self.sh
        self.rise = False
        
        self.DIST = 0 # Distance, in pixels, that the user has pulled down the page.
        self.ref = 30 # Distance to refresh.
        self.maxD = 50 # Maximum distance.
        self.RiseSpeed = 10 # Speed the page rises.
    
    def draw(self):
        # Background color, behind the page:
        background(0, 0, 0)
        
        # When you let go, raise the page:
        if self.rise:
            self.ssh+=self.RiseSpeed
        if self.ssh>self.sh:
            self.rise = False
            self.ssh = self.sh
        
        # Adjust variables:
        self.DIST = self.sh - self.ssh
        
        # Draw above/behind the page:
        tint(1, 1, 1)
        if self.DIST >= self.ref:
            text('Release to refresh.','Helvetica',26,self.sw/2.0,self.sh-2,2)
        else:
            text('Pull down to refresh...','Helvetica',26,self.sw/2.0,self.sh-2,2)
            
        # Draw the page content here:
        fill(0.2, 0.2, 0.2)
        rect(0, 0, self.sw ,self.ssh) #Background
        text('Distance: ' + str(self.DIST), 'Arial', 20, 50, 50, 9)
    
    def touch_began(self, touch):
        self.rise = False
        self.tch = touch.location.y
    
    def touch_moved(self, touch):
        mk = self.tch - touch.location.y
        self.tch = touch.location.y
        self.ssh -= mk
        if self.ssh < self.sh - self.maxD:
            self.ssh = self.sh - self.maxD

    def touch_ended(self, touch):
        if self.ssh>self.sh: self.ssh=self.sh
        if self.DIST >= self.ref:
            self.refreshPage()
        else:
            self.rise = True
            print 'ni'
    
    def refreshPage(self):
        # When the user pulls, run this code.
        sound.play_effect('Click_1',3,3)
        # When it's done, raise the page:
        self.rise = True

run(MyScene())



# Track how far your finger moves.
#   Move the page the same amount that your finger moves.
#   Don't let the page go too low.
# When the user pulls it down enough, tell them they can release to refresh the page. 
# Once the player releases:
#   If the page is pulled down far enough, run the refreshPage() function.
#   Otherwise, just bring the page back to normal height.
