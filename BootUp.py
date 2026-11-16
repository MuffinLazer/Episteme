import cv2
import sys

try:
    canvas = cv2.imread("canvas.png")
 
    WindowName = "CAMS"
    cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL) 
    cv2.moveWindow(WindowName, 0, 0)
    cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # we have done this a few times already 

    cv2.putText(canvas, "TESTING", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255))
    # the 20, 230 thing means it is placed at coords 20, 30, it is using hershy simplex font, 0, 0, 255 means rgb, so blue, 1.2 means refrences the smoothness of the font
 
    while True:
        cv2.imshow(WindowName, canvas)   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break #this reads for the letter q to kill the screens

except KeyboardInterrupt:
    print("SHUTTING DOWN BOOTUP PROCCESS")
    sys.exit()