class Postures:
    def __init__(self, session):
        self.motion = session.service("ALMotion")
        self.posture_service = session.service("ALRobotPosture")

    def stand(self):
        self.posture_service.goToPosture("StandInit", 1.0)

    def crouch(self):
        self.posture_service.goToPosture("Crouch", 1.0)

    def standZero(self):
        self.posture_service.goToPosture("StandZero", 1.0)

    def isStanding(self):
        if (self.posture_service.getPostureFamily() == "Standing") and (self.motion.robotIsWakeUp()):
            return True
        else:
            return False
