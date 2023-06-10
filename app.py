import cv2
from cvzone.HandTrackingModule import HandDetector
import time
from Button import Button

camera = cv2.VideoCapture(0)
camera.set(3, 1280)
camera.set(4, 720)
hand_d = HandDetector(detectionCon=0.9, maxHands=1)

buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 800
        ypos = y * 100 + 150

        buttonList.append(
            Button((xpos, ypos), 100, 100, buttonListValues[y][x]))

clearBtn = Button((800, 550), 400, 100, "CLEAR")

equation = "0"
delay = 0

while True:
    success, frame = camera.read()
    hands, frame = hand_d.findHands(frame)

    for btn in buttonList:
        btn.draw(frame)
    
    clearBtn.draw(frame)

    cv2.rectangle(frame, (800, 50), (800 + 400, 50 + 100),
                  (255, 255, 255), cv2.FILLED)
    cv2.rectangle(frame, (800, 50), (
        800 + 400, 50 + 100), (0, 0, 0), 3)
    
    if hands:
        # Find distance between fingers
        lmList = hands[0]['lmList']
        length, _, frame = hand_d.findDistance(lmList[8], lmList[12], frame)
        x, y = lmList[8]

        if length <= 60:
            for number, btn in enumerate(buttonList):
                if btn.checkClick(frame, x, y) and delay == 0:
                    val = buttonListValues[int(number % 4)][int(number / 4)]

                    if val == "=":
                        equation = str(eval(equation))
                    else:
                        equation += val
                    delay = 1

            if clearBtn.checkClick(frame, x, y):
                equation = "0"

        if delay != 0:
            delay += 1

            if delay >= 10:
                delay = 0
        
    cv2.putText(frame, equation, (810, 120), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 0))

    cv2.imshow("Virtual Calculator", frame)
    key = cv2.waitKey(1)

    if key == 27:
        cv2.destroyAllWindows()
        break