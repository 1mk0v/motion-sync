def getLengthOfPoints(landmark1, landmark2, widthFrame, heightFrame):
    return (
        (int(landmark1.x*widthFrame) - int(landmark2.x*widthFrame))**2 
      + (int(landmark1.y*heightFrame) - int(landmark2.y*heightFrame))**2
    )**0.5