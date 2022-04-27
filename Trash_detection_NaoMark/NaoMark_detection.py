import almath
import time
import math
import argparse
from Trash_detection_NaoMark.LandMarkDetection import LandMarkDetection
from Deplacements.Movement import Movement
from HeadMovement.HeadStiffness import HeadStiffness

class NaoMarkDetection:

    def __init__(self, app):

        self.app = app
        session = app.session
        self.landmarkTheoreticalSize = 0.06
        self.memValue = "LandmarkDetected"
        self.currentCamera = "CameraTop"
        self.motion_service = session.service("ALMotion")
        self.tts = session.service("ALTextToSpeech")
        self.memory_service = session.service("ALMemory")
        self.landMark_service = session.service("ALLandMarkDetection")
        self.landMark_service.subscribe("Test_LandMark", 500, 0.0)
        self.head = HeadStiffness(self.app)
        self.compt = 0
        self.movement = Movement(app)
        self.findBottle = False
        self.findTrash = False
        self.motion_service.wakeUp()
        self.x = 0
        self.y = 0
        self.z = 0
        ## self.landMark_service.subscribe("landmarkTest")
        """
        self.motion = session.service("ALMotion")
        self.memory = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        self.posture_service = session.service("ALRobotPosture")
        self.motion.wakeUp()
        self.x = 0
        self.y = 0
        self.z = 0
        self.head = HeadStiffness(self.app)
        """
    def on_searchNaoMark(self, landMark):
        self.head.HeadAngle(0, 0.10)
        time.sleep(3)
        markData = self.memory_service.getData(self.memValue)
        # Wait for a mark to be detected.
        while len(markData) == 0 and self.compt < 4:
            self.MovementRotation()
            time.sleep(3)
            markData = self.memory_service.getData(self.memValue)
            self.compt += 1
            print (self.compt)

        # Check whether we got a valid output.
        if markData and isinstance(markData, list) and len(markData) >= 2:
            # We detected naomarks !

            # First Field = TimeStamp.
            timeStamp = markData[0]

            # Second Field = array of Mark_Info's.
            markInfoArray = markData[1]
            # Browse the markInfoArray to get info on each detected mark.
            for markInfo in markInfoArray:
                # First Field = Shape info,we don't need it
                markShapeInfo = markInfo[0]
                # Second Field = Extra info (ie, mark ID).
                markExtraInfo = markInfo[1]
                # check out wich type of naomark the nao found
                # we will use the landmark with the id 130 as the bottle
                if markExtraInfo[0] == 64 and landMark == 64:
                    self.findBottle = True
                    self.tts.say("landmark 64 detected")
                    print("landmark with ID 64 detected")
                    # Retrieve landmark center position in radians.
                    wzCamera = markData[1][0][0][1]
                    wyCamera = markData[1][0][0][2]
                    # Retrieve landmark angular size in radians.
                    angularSize = markData[1][0][0][3]

                    # Compute distance to landmark.
                    distanceFromCameraToLandmark = self.landmarkTheoreticalSize / (2 * math.tan(angularSize / 2))

                    # Get current camera position in NAO space.
                    transform = self.motion_service.getTransform(self.currentCamera, 2, True)
                    transformList = almath.vectorFloat(transform)
                    robotToCamera = almath.Transform(transformList)

                    # Compute the rotation to point towards the landmark.
                    cameraToLandmarkRotationTransform = almath.Transform_from3DRotation(0, wyCamera, wzCamera)

                    # Compute the translation to reach the landmark.
                    cameraToLandmarkTranslationTransform = almath.Transform(distanceFromCameraToLandmark, 0, 0)

                    # Combine all transformations to get the landmark position in NAO space.
                    robotToLandmark = robotToCamera * cameraToLandmarkRotationTransform * cameraToLandmarkTranslationTransform
                    self.x = robotToLandmark.r1_c4
                    self.y = robotToLandmark.r2_c4
                    self.z = robotToLandmark.r3_c4
                    theta = math.atan(self.y / self.x)
                    print(theta)
                    self.motion_service.setMoveArmsEnabled(True, True)
                    self.motion_service.moveTo(1.4*self.x-0.10, self.y-0.10, -theta-0.10)
                    self.landMark_service.unsubscribe("Test_LandMark")
                else:
                    print("code pour la poubelle")

        else:
            self.tts.say("No landmark detected")
            print("No landMark detected")


        """
        landmark_detector = LandMarkDetection(self.app)
        self.head.HeadAngle(0, 0.25)
        landmark_detector.on_run()

        for i in range(4):
            if not landmark_detector.find:
                self.tts.say("trash can not find, I turn around")
                self.MovementRotation()
                landmark_detector.on_run()
            else:
                print ("Je vais envoyer les coordonnees de la cible  x= " + str(landmark_detector.x))
                self.Trouver = True
                self.x = landmark_detector.x
                self.y = landmark_detector.y
                self.z = landmark_detector.z
                break
        """
    def MovementRotation(self):
        self.motion_service.setMoveArmsEnabled(False, False)
        print ("Disabled left arm rigth arms")
        self.motion_service.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
        time.sleep(1.0)
        self.motion_service.wbEnable(True)
        initRobotPosition = almath.Pose2D(self.motion_service.getRobotPosition(False))
        X = 0
        Y = 0
        Theta = math.pi / 2.0
        self.motion_service.moveTo(X, Y, Theta, _async=True)
        self.motion_service.waitUntilMoveIsFinished()
        endRobotPosition = almath.Pose2D(self.motion_service.getRobotPosition(False))
        robotMove = almath.pose2DInverse(initRobotPosition) * endRobotPosition
        robotMove.theta = almath.modulo2PI(robotMove.theta)
        print ("Robot Move:", robotMove)
        self.motion_service.wbEnable(False)
        self.motion_service.stopMove()
        self.motion_service.setMoveArmsEnabled(True, True)
