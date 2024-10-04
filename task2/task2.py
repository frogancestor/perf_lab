import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("circleFilePath")
parser.add_argument("dotsFilePath")
args = parser.parse_args()

circleDataFile = open(args.circleFilePath, 'r')  # open circle file and read data
lines = circleDataFile.read().splitlines()
circleDataFile.close()

circleX = float(lines[0].split(' ')[0])
circleY = float(lines[0].split(' ')[1])
radius = float(lines[1])

dotDataFile = open(args.dotsFilePath, 'r')  # open dot file and read data
dots = dotDataFile.read().splitlines()
dotDataFile.close()

for dot in dots:
    dotX = float(dot.split(' ')[0]) - circleX
    dotY = float(dot.split(' ')[1]) - circleY

    hypotenuse = math.sqrt(dotX ** 2 + dotY ** 2)

    if hypotenuse < radius:
        print('1')
    elif hypotenuse == radius:
        print('0')
    elif hypotenuse > radius:
        print('2')
