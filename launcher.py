import qi
from naoqi import ALProxy

from Deplacements.Movement import Movement
from HeadMovements.HeadStiffness import HeadStiffness
import argparse
import sys
import time


# sys.path.insert(0, 'C:\Users\Gando\Desktop\ProjetLong\Deplacements\Movement.py')
# print(sys.path)

# if __name__ == "__main__":
parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, default="127.0.0.1",
                    help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
parser.add_argument("--port", type=int, default=9559,
                    help="Naoqi port number")

args = parser.parse_args()
session = qi.Session()
try:
    session.connect("tcp://" + args.ip + ":" + str(args.port))
except RuntimeError:
    print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
                                                                                          "Please check your script "
                                                                                          "arguments. Run with -h "
                                                                                          "option for help.")
    sys.exit(1)

HeadStiff = HeadStiffness(session)
move = Movement(session)
x = 1.0
y = 0.0
theta = 0.0
move.moveRobot(x, y, theta)
# After 5 seconds, we'll make him stop
time.sleep(3)
# make the robot turn to theta=math.pi/2
# move.MakeNaoTurn()
#time.sleep(3)
# move.moveRobot(x, y, theta)
# Nao stops walking when it encounters an obstacle
#time.sleep(3)
activateHeadStiffness = HeadStiff.activateHeadStiffness()
headMove = HeadStiff.lookAtRightSide()
time.sleep(2)
headmove2 = HeadStiff.lookAtLefSide()
time.sleep(2)
headmove3 = HeadStiff.lookStraight()



