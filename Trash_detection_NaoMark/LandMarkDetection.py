#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Demonstrates a way to localize the robot with ALLandMarkDetection"""

import qi
import sys
import argparse
import almath
import time
import math


class LandMarkDetection:
    def __init__(self, app):
        session = app.session
        self.memory = session.service("ALMemory")
        self.subscriber = self.memory.subscriber("LandmarkDetected")
        self.subscriber.signal.connect(self.on_landmark_detected)
        self.tts = session.service("ALTextToSpeech")
        self.landmark_detection = session.service("ALLandMarkDetection")
        self.landmark_detection.subscribe("LandmarkDetector", 500, 0.0)
        self.got_landmark = False
        self.landmarkTheoreticalSize = 0.06  # in meters
        self.currentCamera = "CameraTop"
        self.find = False
        self.x = 0
        self.y = 0
        self.z = 0

    def on_landmark_detected(self, markData):

        if markData == []:  # empty value when the landmark disappears
            self.got_landmark = False
        elif not self.got_landmark:  # only speak the first time a landmark appears
            self.got_landmark = True
            self.find = True
            print ("I saw a landmark! ")
            self.tts.say("I saw a landmark! ")

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
            print ("Dans le classe LocalizationLandmark Position of landmark et x= " + str(self.x)+", y="+str(self.y)+", z="+str(self.x))


    def on_run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print ("Starting LandmarkDetector")
        try:
            cpt = 2
            while cpt != 0:
                time.sleep(1)
                cpt = cpt - 1
                if self.find:
                    break
        except KeyboardInterrupt:
            print ("Interrupted by user, stopping LandmarkDetector")
            self.landmark_detection.unsubscribe("LandmarkDetector")