import freenect

class Connector:
    def __init__(self, ID):
        pass
    
    def getKinectData(self):
        return freenect.sync_get_depth(), freenect.sync_get_video()

