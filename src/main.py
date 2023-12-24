import cv2
import pyautogui
import mouse
from Hands import HandTracker

def main():
    handsTracker = HandTracker()
    cam = cv2.VideoCapture(0)
    while True:
        success, frame = cam.read()
        if not success:
            print("Camera not detected!")
        height, width, channels = frame.shape
        frame = cv2.flip(frame, 1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        landmarks = handsTracker.getHandsLandmarks(frameRGB)
        if landmarks:
            handsTracker.getHandsDrawImage(landmarks=landmarks, image=frame)
            for handLmrk in landmarks:
                LANDMARK1 = None
                LANDMARK2 = None
                LANDMARK3 = None
                LANDMARK4 = None
                LANDMARK5 = None
                for num, landmark in enumerate(handLmrk.landmark):
                    if num == 4:
                        LANDMARK1 = landmark
                    if num == 8:
                        LANDMARK2 = landmark
                    if num == 12:
                        LANDMARK3 = landmark
                    if num == 16:
                        LANDMARK4 = landmark
                    if num == 20:
                        LANDMARK5 = landmark
                if handsTracker.handMouseMove.isActivate(LANDMARK1, LANDMARK2, LANDMARK3, LANDMARK4, LANDMARK5, width, height):
                    cv2.circle(frame, (int((LANDMARK2.x*width+LANDMARK3.x*width)/2), 
                                       int((LANDMARK2.y*height+LANDMARK3.y*height)/2)), 15, (255 ,102, 255), cv2.FILLED)
                    pyautogui.moveTo()
                if handsTracker.handMouseClick.isActivate(LANDMARK1, LANDMARK2, width, height):
                    cv2.circle(frame, (int((LANDMARK1.x*width+LANDMARK2.x*width)/2), 
                                       int((LANDMARK1.y*height+LANDMARK2.y*height)/2)), 10, (255 ,102, 255), cv2.FILLED)
                    mouse.click('left')

        cv2.imshow("Hand Landmark", frame)

        if cv2.waitKey(1) == ('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()