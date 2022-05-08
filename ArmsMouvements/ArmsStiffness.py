import time

class ArmsStiffness:

    def __init__(self, app):
        self.app = app
        session = app.session
        self.motion_service = session.service("ALMotion")
        self.posture_service = session.service("ALRobotPosture")
        self.tts = session.service("ALTextToSpeech")

    def fixerMainDroite(self):

        names = list()
        times = list()
        keys = list()

        names.append("RShoulderRoll")
        times.append([1.00000])
        keys.append([-0.006981])
        names.append("RShoulderPitch")
        times.append([1.00000])
        keys.append([0.167552])
        names.append("RElbowRoll")
        times.append([1.00000])
        keys.append([0.034907])
        names.append("RElbowYaw")
        times.append([1.00000])
        keys.append([1.125737])
        names.append("RWristYaw")
        times.append([1.00000])
        keys.append([0.000000])
        names.append("RHand")
        times.append([1.00000])
        keys.append([0.100000])

        try:
            self.motion_service.angleInterpolation(names, keys, times, True)
        except BaseException as err:
            pass

    def jeterDansLaPoubelle(self):

        names = list()
        times = list()
        keys = list()

        names.append("RShoulderRoll")
        times.append([1.00000])
        keys.append([-0.006981])
        names.append("RShoulderPitch")
        times.append([1.00000])
        keys.append([0.167552])
        names.append("RElbowRoll")
        times.append([1.00000])
        keys.append([0.034907])
        names.append("RElbowYaw")
        times.append([1.00000])
        keys.append([1.125737])
        names.append("RWristYaw")
        times.append([1.00000])
        keys.append([-1.312488])
        names.append("RHand")
        times.append([1.00000])
        keys.append([0.000000])

        try:
            self.motion_service.angleInterpolation(names, keys, times, True)
        except BaseException as err:
            pass
        self.motion_service.openHand("RHand")

    def ramasser(self):

        noms = list()
        temps = list()
        cle = list()
        noms.append("LShoulderRoll")
        temps.append([1.00000])
        cle.append([-0.300000])
        noms.append("RShoulderRoll")
        temps.append([1.00000])
        cle.append([+0.300000])
        try:
            self.motion_service.angleInterpolation(noms, cle, temps, True)
        except BaseException:
            pass

        noms = list()
        temps = list()
        cle = list()
        noms.append("LShoulderPitch")
        temps.append([1.00000])
        cle.append([0.100000])
        noms.append("RShoulderPitch")
        temps.append([1.00000])
        cle.append([0.100000])
        try:
            self.motion_service.angleInterpolation(noms, cle, temps, True)
        except BaseException:
            pass
        self.motion_service.setMoveArmsEnabled(False, False)
        time.sleep(1)
        self.posture_service.goToPosture("Stand", 0.8)
        time.sleep(1)


    def Accroupissement(self):
        self.posture_service.goToPosture("Crouch", 0.8)
        noms = list()
        temps = list()
        cle = list()

        a = list()
        b = list()
        c = list()

        a.append("RShoulderRoll")
        b.append([1.00000])
        c.append([-0.8063421])

        noms.append("RShoulderRoll")
        temps.append([1.00000])
        cle.append([0.3141592])
        noms.append("RShoulderPitch")
        temps.append([1.00000])
        cle.append([1.0908307])
        noms.append("RElbowRoll")
        temps.append([1.00000])
        cle.append([0.9948376])
        noms.append("RElbowYaw")
        temps.append([1.00000])
        cle.append([1.5009831])
        noms.append("RWristYaw")
        temps.append([1.00000])
        cle.append([-0.3804817])
        noms.append("RHand")
        temps.append([1.00000])
        cle.append([0.000000])
        self.motion_service.openHand("RHand")
        try:
            self.motion_service.angleInterpolation(noms, cle, temps, True)
        except BaseException:
            pass
        self.motion_service.setMoveArmsEnabled(True, False)

    def standUp(self):
        nom = list()
        temps = list()
        cle = list()
        self.motion_service.closeHand("RHand")
        nom.append("RHand")
        temps.append([1.00000])
        cle.append([0.0000000])
        nom.append("LHipYawPitch")
        temps.append([1.00000])
        cle.append([-0.170010])
        nom.append("LHipRoll")
        temps.append([1.00000])
        cle.append([0.119108])
        nom.append("LHipPitch")
        temps.append([1.00000])
        cle.append([0.127419])
        nom.append("LKneePitch")
        temps.append([1.00000])
        cle.append([-0.092328])
        nom.append("LAnklePitch")
        temps.append([1.00000])
        cle.append([0.087419])
        nom.append("LAnkleRoll")
        temps.append([1.00000])
        cle.append([-0.110793])

        nom.append("RHipYawPitch")
        temps.append([1.00000])
        cle.append([-0.170010])
        nom.append("RHipRoll")
        temps.append([1.00000])
        cle.append([-0.119102])
        nom.append("RHipPitch")
        temps.append([1.00000])
        cle.append([0.127419])
        nom.append("RKneePitch")
        temps.append([1.00000])
        cle.append([-0.092328])
        nom.append("RAnklePitch")
        temps.append([1.00000])
        cle.append([0.087419])
        nom.append("RAnkleRoll")
        temps.append([1.00000])
        cle.append([0.110793])
        try:
            self.motion_service.angleInterpolation(nom, cle, temps, True)
        except BaseException:
             pass
        self.tts.say("Looking for a trash can")
