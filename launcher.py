import math
import time

from Trash_detection_NaoMark.NaoMark_detection import NaoMarkDetection
import qi
import argparse
import sys

from ArmsMouvements.ArmsStiffness import ArmsStiffness
from Deplacements.Movement import Movement

parser = argparse.ArgumentParser()
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

# print("hello")
movement = Movement(app)
# movement.obstacleAvoidance(2)
#searchBottle = NaoMarkDetection(app)
#searchBottle.on_searchNaoMark(64)
#time.sleep(3)
#searchBottle.on_searchNaoMark(68)
arms = ArmsStiffness(app)
arms.Accroupissement()
arms.standUp()
movement.moveTo(0.0,0.0,math.pi/2)




#movement = Movement(app)
#movement.moveTo(1, 0, 0)
#if searchBottle.findBottle == True:
    #arms.Accroupissement()
"""
while not findBottle:
    searchBottle.on_searchNaoMark()
    findBottle = searchBottle.find
    if not searchBottle.find:
        tts.say("Not find")
        time.sleep(2)
        movement.obstacleAvoidance()

print "cible trouver"
time.sleep(2)
theta = math.atan(searchBottle.y/searchBottle.x)
movement.moveTo(1.4*searchBottle.x, searchBottle.y, -theta)

arms.Accroupissement()
arms.ramasser()

searchPoubelle = NaoMarkDetection(app)
findPoubelle = False

while not findPoubelle:
    searchPoubelle.on_searchNaoMark()
    findPoubelle = searchPoubelle.find
    if not searchBottle.find:
        tts.say("Not find I am going ahead")
        time.sleep(2)
        movement.obstacleAvoidance()

theta = math.atan(searchPoubelle.y/searchPoubelle.x)
movement.moveTo(1.4*searchPoubelle.x, searchPoubelle.y, -theta)

arms.jetterDansLaPoubelle()
"""


#sys.exit(100)



