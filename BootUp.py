import cv2
import sys
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import time

text = "INITIALIZING"

try:
    currenttime = time.monotonic()
    currenttime = int(currenttime)
    futuretime = currenttime + 5
        
    canvas = cv2.imread("Resources/canvas.png")	
        
    font = ImageFont.truetype("Resources/Ethnocentric-Regular.otf", 70)
        
    WindowName = "CAMS"
    cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL) 
    cv2.moveWindow(WindowName, 0, 0)
    cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # we have done this a few times already 

    canvasRGB = cv2.cvtColor(canvas,cv2.COLOR_BGR2RGB)

    pilfirst = Image.fromarray(canvasRGB)

    draw = ImageDraw.Draw(pilfirst)

    draw.text((225, 278), text, font=font, fill=(0,0,255,225))

    processed = cv2.cvtColor(np.array(pilfirst), cv2.COLOR_RGB2BGR)

        # cv2.putText(canvas, "INITIALIZING", (396, 320), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
        # the 396, 320 thing means it is placed at coords 396, 320, it is using hershy simplex font, 0, 0, 255 means rgb, so blue, 1.2 size of the font, the number 2 at the very end is the boldness of the text
    
    while True:
        cv2.imshow(WindowName, processed)
        currenttime = int(time.monotonic())
        if currenttime == futuretime:
            break #this reads for the letter q to kill the screens

except KeyboardInterrupt:
    print("SHUTTING DOWN BOOTUP PROCCESS")
    sys.exit()
