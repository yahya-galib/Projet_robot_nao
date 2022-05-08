import math
import time

from Trash_detection_NaoMark.NaoMark_detection import NaoMarkDetection
import qi
import argparse
import sys

from ArmsMouvements.ArmsStiffness import ArmsStiffness
from Deplacements.Movement import Movement

parser = argparse.ArgumentParser()
# 172.20.10.12
parser.add_argument("--ip", type=str, default="172.20.10.12",
                    help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
parser.add_argument("--port", type=int, default=9559,
                    help="Naoqi port number")

args = parser.parse_args()

try:
    connection_url = "tcp://" + args.ip + ":" + str(args.port)
    app = qi.Application(["LandmarkDetector", "--qi-url=" + connection_url])
except RuntimeError:
    print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
                                                                                         "Please check your script "
                                                                                          "arguments. Run with -h "
                                                                                          "option for help.")
    #sys.exit(1)

app.start()
session = app.session
posture_service = session.service("ALRobotPosture")
movement = Movement(app)
# creation d'un objet de la classe NaoMarkDetection qui decrit le comportement du robot pour chercher les dechets
searchTrash = NaoMarkDetection(app)
searchTrash.on_searchNaoMark(84)

# ArmsStiffness est la classe qui décrit les mouvements des articulations
arms = ArmsStiffness(app)
arms.Accroupissement()
arms.standUp()

searchTrashCan = NaoMarkDetection(app)
searchTrashCan.on_searchNaoMark(80)
if searchTrashCan.findTrash:
    arms.jeterDansLaPoubelle()

else:
    posture_service.goToPosture("Crouch", 0.8)



