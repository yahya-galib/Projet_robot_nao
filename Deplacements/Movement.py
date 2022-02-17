import math
import time


class Movement:
    def __init__(self, session):
        self.positionErrorThresholdPos = 0.01
        self.positionErrorThresholdAng = 0.03
        self.motion_service = session.service("ALMotion")
        self.posture_service = session.service("ALRobotPosture")
        self.tts = session.service("ALTextToSpeech")
        self.memoryProxy = session.service("ALMemory")
        self.sonarProxy = session.service("ALSonar")
        # Wake up robot
        self.motion_service.wakeUp()
        # Send robot to Stand Init
        self.posture_service.goToPosture("StandInit", 0.5)

    def moveRobot(self, x, y, theta):
        # disable Arms movements
        leftArmEnable = False
        rightArmEnable = False
        footContactProtectionEnable = False
        isEnabled = True
        distance = 0.40
        self.motion_service.setMoveArmsEnabled(leftArmEnable, rightArmEnable)
        # activate the foot contact protection
        self.motion_service.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", footContactProtectionEnable]])
        # setting security distance to avoid collision
        self.motion_service.setOrthogonalSecurityDistance(distance)
        self.motion_service.setTangentialSecurityDistance(distance)
        # activate the external collision protection
        name = "Move"
        enable = True
        self.motion_service.setExternalCollisionProtectionEnabled(name, enable)
        result = self.motion_service.getExternalCollisionProtectionEnabled("Move")
        print (result)
        # Position before movement
        initPosition = self.motion_service.getRobotPosition(False)
        print(initPosition)
        targetDistance = [x, y, theta]
        expectedEndPositionX = initPosition[0] * targetDistance[0]
        expectedEndPositionY = initPosition[1] * targetDistance[1]
        expectedEndPositionTheta = initPosition[2] * targetDistance[2]
        expectedEndPosition = [expectedEndPositionX, expectedEndPositionY, expectedEndPositionTheta]
        self.motion_service.moveTo(x, y, theta, _async=True)
        self.motion_service.waitUntilMoveIsFinished()
        # position after movement
        realEndPosition = self.motion_service.getRobotPosition(False)
        print (realEndPosition)
        positionError = realEndPosition.diff(expectedEndPosition)
        # positionError.theta = almath.modulo2PI(positionError.theta)
        if (abs(positionError.x) < self.positionErrorThresholdPos
                and abs(positionError.y) < self.positionErrorThresholdPos
                and abs(positionError.theta) < self.positionErrorThresholdAng):
            print "Arrived at Destination"
        else:
            print "Destination not reached"

    def obstacleAvoidance(self):
        # make the nao turn
        self.MakeNaoTurn()
        # sleep  2s and then move a little forward
        time.sleep(2)
        x = 0.2
        y = 0.0
        theta = 0.0
        self.motion_service.moveTo(x, y, theta)

    def MakeNaoTurn(self):
        x = 0.0
        y = 0.0
        theta = math.pi / 2
        # theta should be changed to make our robot turn left or right
        self.motion_service.moveTo(0.5, 0, theta)

    def isStanding(self):
        if (self.postureService.getPostureFamily() == "Standing") and (self.motionService.robotIsWakeUp()):
            return True
        else:
            return False
