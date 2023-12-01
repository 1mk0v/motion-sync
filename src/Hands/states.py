
from .utils import getLengthOfPoints

class State:

    def __init__(self) -> None:
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


class HandMouseMove(State):

    def __init__(self) -> None:
        super().__init__()

    def isActivate(self, landmark1, landmark2, landmark3, landmark4, landmark5, width, height):
        if landmark1 and landmark2 and landmark3 and landmark4 and landmark5:
            lenOf12_8 = getLengthOfPoints(landmark2, landmark3, width, height)
            lenOf12_4 = getLengthOfPoints(landmark1, landmark3, width, height)
            lenOf12_16 = getLengthOfPoints(landmark4, landmark3, width, height)
            lenOf12_20 = getLengthOfPoints(landmark5, landmark3, width, height)
            diff1 = abs(lenOf12_4 - lenOf12_16)
            diff2 = abs(lenOf12_4 - lenOf12_20)
            diff3 = abs(lenOf12_16 - lenOf12_20)
            if diff1 <= 20 and diff2 <= 20 and diff3 <= 20 and lenOf12_8 <= 20:
                return True
        return False
    
class HandMouseClick(State):

    def __init__(self) -> None:
        super().__init__()

    def isActivate(self, landmark1, landmark2, width, height):
        if landmark1 and landmark2:
            length = getLengthOfPoints(landmark1, landmark2, width, height)
            if length <= 20:
                return True
        return False