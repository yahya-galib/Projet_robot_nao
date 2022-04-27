import naoqi
import motion


class HeadStiffness:
    def __init__(self, app):
        self.app = app
        session = app.session
        self.motion = session.service("ALMotion")

    def activateHeadStiffness(self):
        # Make sure the head is stiff to be able to move it.
        # To do so, make the stiffness go to the maximum in one second.
        # Joint name
        jointName = "HeadYaw"
        # Target stiffness.
        stiffness = 1.0
        # Time (in seconds) to reach the target.
        time = 1.0
        # Call the stiffness interpolation method.
        self.motion.stiffnessInterpolation(jointName, stiffness, time)

    def removeHeadStiffness(self):
        jointName = "HeadYaw"
        stiffness = 0.0
        time = 1.0
        self.motion.stiffnessInterpolation(jointName, stiffness, time)

    def lookAtRightSide(self):
        # Interpolate the head yaw to 1.0 radian in 1.0 second
        names = "HeadYaw"
        angleLists = -1.5
        timeLists = 1.0
        isAbsolute = True
        self.motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    def lookAtLefSide(self):
        names = "HeadYaw"
        angleLists = 1.5
        timeLists = 3.0
        isAbsolute = True
        self.motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    def HeadAngle(self, alpha, beta):
        self.motion.setStiffnesses("Head", 1.0)
        self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [alpha, beta], 0.3)
        self.motion.setStiffnesses("Head", 0.0)

    def lookDown(self):
        names = "HeadYaw"
        angleLists = 1.5
        timeLists = 3.0
        isAbsolute = True
        self.motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    def lookStraight(self):
        names = "HeadYaw"
        angleLists = 0.0
        timeLists = 3.0
        isAbsolute = True
        self.motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)

# in our case Angleslist is already in radian not need to convert to rad
# Example showing multiple trajectories
# names      = ["HeadYaw", "HeadPitch"]
# angleLists = [30.0*almath.TO_RAD, 30.0*almath.TO_RAD]
# isAbsolute = True
# motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

# HeadYaw	(Head joint twist (Z))	in degree(-119.5 to 119.5)	in radian(-2.0857 to 2.0857)
