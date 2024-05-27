# We will need to import multiple threads to handle display the changes of the camera, camera data & alarm at the same time 
import threading

import winsound

# Importing Open CV - Used for computer vision
import cv2
import imutils

# Choose the number of cameras you have ; 1 camera indicate index 0 or 2 cameras indicate index 1
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Setting the width and height of the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# We are going to get a starting frame 
# So the idea of the motion detector system is to
        # Get a frame then compare it to the next frame,
        # Then calculate the difference
        # If the differences are high enough to be motion -: 
            # We are going to cause an alarm 
            

# _ -> A return value, 
# start_frame -> This will be returned by the camera
#cap.read () - Get from the camera a return value 
_, start_frame = cap.read()

start_frame = imutils.resize(start_frame, width=400)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

# Set alarm's default value
alarm = False 

# Says do we want to look for an alarm 
alarm_mode = False

# Says how long do we need to have movement to cause an alarm 
alarm_counter = 0


def beep_alarm():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break
        print("ALARM!!🔔")
        winsound.Beep(2500, 1000)
    alarm = False
    

while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=400)
    
    # If we are in alarm mode, then we are going to calculate the differences in frames in order to determine whther we have an alarm or not 
    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (21,21), 0)
        
        # Calculate the difference between this frame and the start frame defined above 
        difference = cv2.absdiff(frame_bw, start_frame)
        
        # Determine the lighness or darkeness -> We are going to go with either 255, & above which is light or below it till 0 is darkness
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        
        start_frame = frame_bw
        
        
        # Next, we take the threshhold difference and we calculate the sum of it and we define a value that we want to look for 
        # The smaller the number the more sensitive the detection will be ; So a number like 10, then with the slighest movement, the alarm will go off
        if threshold.sum() > 300:
            alarm_counter += 1 # Will increase every time it sees a threshold over 300
        else:
            if alarm_counter > 0:
                alarm_counter -= 1 # Will decrease every time it sees a threshold under 300
        
        # Show the threshold image 
        cv2.imshow("Camera", threshold)
     
    else:
        cv2.imshow("Camera", frame)   
        
        
        
    # Determines a longer movement 
    # The lower it is, the more immediate it will trigger the alarm 
    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()
    
    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    
    if key_pressed == ord ("q"):
        alarm_mode = False
        break
    
cap.release()
cv2.destroyAllWindows()
        