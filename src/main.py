from sre_constants import SUCCESS
import cv2
import mediapipe as mp
import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.drawing_utils as drawing


hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5
)


cam = cv2.VideoCapture(0)

while True:
    
    success, frame = cam.read()
    if not success:
        print("Camera not detected!")

    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    handsDetected = hands.process(frameRGB)

    if handsDetected.multi_hand_landmarks:
        for lanmark in handsDetected.multi_hand_landmarks:
            print(lanmark)
            drawing.draw_landmarks(
                image=frame,
                landmark_list=lanmark,
                connections=mpHands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Landmark", frame)

    if cv2.waitKey(1) == ('q'):
        break

cam.release()
cv2.destroyAllWindows()
