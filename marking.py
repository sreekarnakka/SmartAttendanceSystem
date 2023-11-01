import cv2
import os
import xlsxwriter
import numpy as np
import face_recognition
from datetime import datetime
import pandas as pd
path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
# print(myList)
print("List of students:")
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

with open('Attendance.csv', 'r+') as f:
    myDataList = f.readlines()
    nameList = []
    for line in myDataList:
        entry = line.split(',')
        nameList.append(entry[0])
    #print(nameList[1:len(nameList)])
print("list of students present:")
print(list(set(classNames) & set(nameList)))
print("list of students absent:")
print(list(set(classNames) - set(nameList)))

list1=[(set(classNames) & set(nameList))]
list2=[(set(classNames) - set(nameList))]


def insert_data(listdata):
    wb = xlsxwriter.Workbook("PRESENTEES.xlsx")
    ws = wb.add_worksheet()
    ws.write('A1', 'NAME')
    row = 1
    col = 0
    for line in listdata:
        for item in line:
            ws.write(row, col, item)
            col += 1
            row += 1
            col = 0

    wb.close()


insert_data(list1)
os.system("PRESENTEES.xlsx")

def insert_data1(listdata):
    wb = xlsxwriter.Workbook("ABSENTEES.xlsx")
    ws = wb.add_worksheet()
    ws.write('A1', 'NAME')
    row = 1
    col = 0
    for line in listdata:
        for item in line:
            ws.write(row, col, item)
            col += 1
            row += 1
            col = 0

    wb.close()


insert_data1(list2)
os.system("ABSENTEES.xlsx")



import pywhatkit

#pywhatkit.sendwhatmsg("+918179227736", "Your ward is Absent", 10, 2)
pywhatkit.sendwhatmsg_instantly("+918179227736","Your ward is Absent")
#pywhatkit.sendwhatmsg_instantly("+919441281528","Your ward is Absent")
#pywhatkit.sendwhatmsg_instantly("+916281142549","Your ward is Absent")