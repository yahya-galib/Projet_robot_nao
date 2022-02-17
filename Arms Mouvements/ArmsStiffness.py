import motion


class ArmsStiffness:
    def __init__(self, session):
        self.motion = session.service("ALMotion")

    def activateArmsStiffnes(self):
        return 0
