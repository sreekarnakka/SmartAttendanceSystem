# import cv2
# import os
# import numpy as np
# import face_recognition
# from datetime import datetime
#
# path = 'ImagesAttendance'
# images = []
# classNames = []
# myList = os.listdir(path)
# # print(myList)
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)
#
#
# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList
#
#
# def markAttendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             #now = datetime.now()
#             #today = datetime.today()
#             #dtString = now.strftime('%H:%M:%S')
#             now = datetime.now()
#             x=now.strftime("%d-%m-%Y  %I:%M:%S%p")
#             #f.writelines(f'{name},{today}\n')
#             f.writelines(f'{name},{x}\n')
#
#
# encodeListKnown = findEncodings(images)
# print('Encoding Complete')
#
#
# while True:
#     img = face_recognition.load_image_file('ImagesBasic/grouppic.jpeg')
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#
#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
#
#     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#         # print(faceDis)
#         matchIndex = np.argmin(faceDis)
#
#         '''if matches[matchIndex]:
#             name = classNames[matchIndex].upper()
#             # print(name)
#             y1, x2, y2, x1 = faceLoc
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#             markAttendance(name)'''
#
#         if faceDis[matchIndex] < 0.50:
#             name = classNames[matchIndex]#.upper()
#             markAttendance(name)
#         else:
#             name = 'Unknown'
#         # print(name)
#         y1, x2, y2, x1 = faceLoc
#         y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#         cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#         cv2.imshow('Webcam', img)
#         cv2.waitKey(1)

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