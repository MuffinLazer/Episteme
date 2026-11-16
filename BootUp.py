import cv2
import sys
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import time
import cursor

def Startscreen():  
    text = "INITIALIZING"
try:
        cursor.hide()
        currenttime = time.monotonic()
        currenttime = int(currenttime) # monotonic time gives me the time of the clock in seconds in a float, which is super helpful as it lets us do basic math to find future time
        futuretime = currenttime + 5
            
        canvas = cv2.imread("Resources/canvas.png")	# reads the image file 
            
        font = ImageFont.truetype("Resources/Ethnocentric-Regular.otf", 70) # finds out font and selects the size of it
            
        WindowName = "CAMS"
        cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL) 
        cv2.moveWindow(WindowName, 0, 0)
        cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # we have done this a few times already 

        canvasRGB = cv2.cvtColor(canvas,cv2.COLOR_BGR2RGB) # once again cv2 is kinda bad so we have to convert it from bgr to rgb

        pilfirst = Image.fromarray(canvasRGB) # takes the rgb canvas and makes it into PIL which lets us draw text with more options

        draw = ImageDraw.Draw(pilfirst) # makes a drawing function that says we draw on pilfirst

        draw.text((225, 278), text, font=font, fill=(0,0,255,225)) # draws our text

        processed = cv2.cvtColor(np.array(pilfirst), cv2.COLOR_RGB2BGR) # converts it back to bgr

            # cv2.putText(canvas, "INITIALIZING", (396, 320), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
            # the 396, 320 thing means it is placed at coords 396, 320, it is using hershy simplex font, 0, 0, 255 means rgb, so blue, 1.2 size of the font, the number 2 at the very end is the boldness of the text
        while True:
            cv2.imshow(WindowName, processed) # you know what this does
            currenttime = int(time.monotonic()) # maff
            if cv2.waitKey(1) & currenttime >= futuretime: # turns out you really need cv2.waitkey(1), like a lot
                break 
except KeyboardInterrupt:
        print("SHUTTING DOWN BOOTUP PROCCESS")
        sys.exit() # W LARPING
