# Importing of Libraries
# Importing of opencv library
import cv2
# Importing of time library for adding delays
import time
# Import Client library from twilio
from twilio.rest import Client
# Adding testing video path
cam=cv2.VideoCapture(r"C:\Users\dell\PycharmProjects\recog\videoplayback.mp4")
# Initialising Backgound Subtractor
bg = cv2.createBackgroundSubtractorMOG2()
j = 0
# Main function
while(1):
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fg = bg.apply(gray)
    contours, _ = cv2.findContours(fg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        areas = []
    for contour in contours:
        ar = cv2.contourArea(contour) # Defining Contour Area
        areas.append(ar) # Appending the Area
        max_area = max(areas or [0])
        max_area_index = areas.index(max_area)
        cnt = contours[max_area_index]
        M = cv2.moments(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.drawContours(fg, [cnt], 0, (255,255,255), 3, maxLevel = 0)
    if h < w:
        j += 1
 # Conditions for fall detection contour Area
    if j > 20:
        cv2.putText(frame, 'FALL', (x+5, y-5), cv2.FONT_HERSHEY_TRIPLEX, 2, (79,244,255), 2)
        cv2.rectangle (frame,(x,y),(x+w,y+h),(0,0,255),2)
        # account_sid='AC9a23e0df928cdb7ad6cf8d926decfab2'
        account_sid = 'ACb966dd4800ecab1f544c00a89ba56e38'
        # auth_token='56e9a0a0140bb475111973487095af0a'
        auth_token = '9bdbfbc11b895dc9096a40f3e11fd8bf'
        client=Client(account_sid,auth_token)
        message=client.messages.create(to="+917396749442", from_="+12566702319", body="Your Kid has fallen Down"  )
        time.sleep(1000)
    if h > w:
        j = 0
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('video', frame)
    if cv2.waitKey(33) == 27:
        break
cam.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()