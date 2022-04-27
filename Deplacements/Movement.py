import math
import time
import almath


class Movement:
    def __init__(self, app):
        session = app.session
        self.motion_service = session.service("ALMotion")
        self.posture_service = session.service("ALRobotPosture")
        self.sonarProxy = session.service("ALSonar")
        self.memoryProxy = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        # Wake up robot
        self.motion_service.wakeUp()
        # Send robot to Stand Init
        self.posture_service.goToPosture("StandInit", 0.5)

    def obstacleAvoidance(self, X):
        # disable Arms movements
        leftArmEnable = False
        rightArmEnable = False
        self.motion_service.setMoveArmsEnabled(leftArmEnable, rightArmEnable)
        self.motion_service.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])

        self.motion_service.wbEnable(True)

        self.sonarProxy.subscribe("SonarActived")

        distanceObstacle = self.memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")

        if distanceObstacle > 1:
            self.motion_service.moveTo(X, 0, 0, _async=True)
        else:
            while distanceObstacle < 1.5:
                self.tts.say("Obstacle ")
                self.motion_service.moveTo(0.0, 0.0, math.pi / 2, _async=True)
                # wait is useful because with _async moveTo is not blocking function
                self.motion_service.waitUntilMoveIsFinished()
                self.sonarProxy.subscribe("SonarActived")
                distanceObstacle = self.memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")


    def moveTo(self,x,y,theta):
        self.motion_service.moveTo(x,y,theta)