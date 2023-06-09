import pytesseract
import cv2
import os
import numpy as np
from pathlib import Path

from roboflow import Roboflow
rf = Roboflow(api_key="qSAE0cOsWyZS8vnra1eh")
project = rf.workspace().project("licenseplatedetection-z1uvx")
model = project.version(1).model


def imageProcessing(img, res):

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    
    img = cv2.convertScaleAbs(img, 100, 2)

    box = img[((int)(res['y']-res['height']*0.5)):((int)(res['y']+res['height']*0.5)),
              ((int)(res['x']-res['width']*0.5)):((int)(res['x']+res['width']*0.5))]
    box = cv2.resize(box, (700, (int)(box.shape[0]*700/box.shape[1])))
    
    
    bordered = cv2.copyMakeBorder(
        box.copy(), 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    gray = cv2.cvtColor(bordered, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(
        contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    image2 = gray.copy()
    plate_num = ''
    text = ''
    lettersFound = 0
    # for cnt in sorted_contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     height, width = image2.shape
    #     if height > 5*h:
    #         continue
    #     # if w > h * 3:
    #     #     continue
    #     if w > 0.4*width:
    #         continue
    #     area = h * w
    #     if area < 0.01 * height * width or area > 0.5 * height * width:
    #         continue
    #     lettersFound += 1
    #     rect = cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #     letter = thresh[y-5:y+h+5, x-5:x+w+5]
    #     letter = cv2.bitwise_not(letter)

    #     text = pytesseract.image_to_string(
    #         letter, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3').splitlines()

    #     if(len(text) >= 1):
    #         pass
    #         # print('text-', text)
    #     elif(h > 2*w):
    #         text = ['1']
    #         # print('text-', text)
    #     plate_num += ''.join(text)
        
    for cnt in sorted_contours:
        x,y,w,h = cv2.boundingRect(cnt)
        height, width = image2.shape
        if height > 5*h: continue
        # if w > h* 3: continue
        if w > 0.4*width: continue
        area = h * w
        if area < 0.01* height * width or area > 0.5 * height * width: continue
        rect = cv2.rectangle(image2, (x,y), (x+w, y+h), (0,255,0),2)
        letter = thresh[y-5:y+h+5, x-5:x+w+5]
        letter = cv2.bitwise_not(letter)
        
        letter = cv2.GaussianBlur(letter, (3, 3), 0)
        letter = cv2.threshold(letter, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



        text = pytesseract.image_to_string(letter, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
        # if(len(text)>=1):
        #   print('text-',text[-1])
        # elif(h>2*w):
        #   text='1'
        print('text-',text)
        plate_num += text
            
        print('plate_num=', plate_num)
    # if lettersFound > 0:
    #     # cv2.imshow('rect', rect)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    return plate_num



def detectLicensePlateNumber(vehicle_img):
    vehicle_img = cv2.imdecode(np.frombuffer(
                vehicle_img, np.uint8), cv2.IMREAD_COLOR)
    
    print(vehicle_img)
    
    pred = (model.predict(vehicle_img, confidence=40,
                overlap=30).json())['predictions'][0]
    print(pred)
    if not pred:
        plateNumber = "Couldn't read, sorry"

    plateNumber = imageProcessing(vehicle_img, pred)
    if not plateNumber:
        plateNumber = "Couldn't read, sorry"
    return plateNumber