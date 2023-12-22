import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.drawing_utils as drawing
from .states import HandMouseMove, HandMouseClick

class HandTracker():
    
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mpHands
        self.hands = self.mpHands.Hands(
            self.mode,
            self.maxHands,
            self.modelComplex,
            self.detectionCon,
            self.trackCon
        )
        self.handMouseMove = HandMouseMove()
        self.handMouseClick = HandMouseClick()
        self.mpDraw = drawing

    def getHandsDrawImage(self, landmarks, image):
        if landmarks:
            for handLms in landmarks:
                self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
    
    def getHandsLandmarks(self, imageRGB):
        results = self.hands.process(imageRGB)
        return results.multi_hand_landmarks