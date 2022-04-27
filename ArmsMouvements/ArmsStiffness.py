import time



class ArmsStiffness:

    def __init__(self, app):
        self.app = app
        session = app.session
        self.motion_service = session.service("ALMotion")
        self.posture_service = session.service("ALRobotPosture")

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
        keys.append([1.000000])

        try:
            self.motion_service.angleInterpolation(names, keys, times, True)
        except BaseException as err:
            pass

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

        noms.append("RShoulderRoll")
        temps.append([1.00000])
        cle.append([-0.2216568])
        noms.append("RShoulderPitch")
        temps.append([1.00000])
        cle.append([0.9948376])
        noms.append("RElbowRoll")
        temps.append([1.00000])
        cle.append([1.0070549])
        noms.append("RElbowYaw")
        temps.append([1.00000])
        cle.append([1.5393804])
        noms.append("RWristYaw")
        temps.append([1.00000])
        cle.append([0.1396263])

        noms.append("LShoulderRoll")
        temps.append([1.00000])
        cle.append([0.2216568])
        noms.append("LShoulderPitch")
        temps.append([1.00000])
        cle.append([0.9948376])
        noms.append("LElbowRoll")
        temps.append([1.00000])
        cle.append([-1.0070549])
        noms.append("LElbowYaw")
        temps.append([1.00000])
        cle.append([-1.5393804])
        noms.append("LWristYaw")
        temps.append([1.00000])
        cle.append([-0.1396263])
        try:
            self.motion_service.angleInterpolation(noms, cle, temps, True)
        except BaseException:
            pass


        self.motion_service.openHand("RHand")
        self.motion_service.openHand("LHand")

        a.append("RShoulderRoll")
        b.append([1.00000])
        c.append([0.2199114])
        a.append("LShoulderRoll")
        b.append([1.00000])
        c.append([-0.2199114])
        try:
            self.motion_service.angleInterpolation(a, c, b, True)
        except BaseException:
            pass
        self.motion_service.closeHand("RHand")
        self.motion_service.closeHand("LHand")

    def standUp(self):
        names = list()
        times = list()
        keys = list()

        names.append("LHipYawPitch")
        times.append([1.00000])
        keys.append([-0.170010])
        names.append("LHipRoll")
        times.append([1.00000])
        keys.append([0.119108])
        names.append("LHipPitch")
        times.append([1.00000])
        keys.append([0.127419])
        names.append("LKneePitch")
        times.append([1.00000])
        keys.append([-0.092328])
        names.append("LAnklePitch")
        times.append([1.00000])
        keys.append([0.087419])
        names.append("LAnkleRoll")
        times.append([1.00000])
        keys.append([-0.110793])

        names.append("RHipYawPitch")
        times.append([1.00000])
        keys.append([-0.170010])
        names.append("RHipRoll")
        times.append([1.00000])
        keys.append([-0.119102])
        names.append("RHipPitch")
        times.append([1.00000])
        keys.append([0.127419])
        names.append("RKneePitch")
        times.append([1.00000])
        keys.append([-0.092328])
        names.append("RAnklePitch")
        times.append([1.00000])
        keys.append([0.087419])
        names.append("RAnkleRoll")
        times.append([1.00000])
        keys.append([0.110793])

        try:
            self.motion_service.angleInterpolation(names, keys, times, True)
        except BaseException:
            pass
