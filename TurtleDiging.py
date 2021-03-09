import csv
import math
from tokenize import String


def findingThelocationsOfTurtles(numberOfTurtles, height, width):

    positionForTurtles = []

    if (numberOfTurtles < height):
        for counter in range(numberOfTurtles-1, -1, -1):
            rowStartingPoint = height - height/numberOfTurtles * (counter + 1)
            colStartingPoint = 0
            print(rowStartingPoint)

            if (isinstance(rowStartingPoint, float)):
                percentage_Of_How_Far_In_The_Width_Of_Grid = rowStartingPoint - math.floor(rowStartingPoint)
                print(percentage_Of_How_Far_In_The_Width_Of_Grid)

                rowStartingPoint = math.floor(rowStartingPoint)
                colStartingPoint = math.floor(percentage_Of_How_Far_In_The_Width_Of_Grid*width)

            positionForTurtles.append([rowStartingPoint, colStartingPoint])

    print(positionForTurtles)
    return positionForTurtles

def startDiging(grid, positionForTurtles, numberOfBlocksToScanForEachTurtle, numTurtles, width, amountOfFuel):

    print(width)
    for counter in range(int(numberOfBlocksToScanForEachTurtle)):
        for turtle in range(numTurtles):
            turtleRowPostion = positionForTurtles[turtle][0]
            turtleColPostion = positionForTurtles[turtle][1]

            block = grid[turtleRowPostion][turtleColPostion]
            if block == 'D':
                grid[turtleRowPostion][turtleColPostion] = "C"
                amountOfFuel[turtle] = amountOfFuel[turtle] - 10

            if turtleColPostion > width - 2:
                turtleRowPostion = turtleRowPostion + 1
                turtleColPostion = 0
            else:
                turtleColPostion = turtleColPostion + 1

            positionForTurtles[turtle][0] = turtleRowPostion
            positionForTurtles[turtle][1] = turtleColPostion

    return grid


def diggingUpDirt(csvFile, numberOfTurtles):

    csvReader = csv.reader(csvFile)

    amountOfFuel = [1000] * numberOfTurtles

    gridOfDirt = []

    for row in csvReader:
        print(row)
        rowOfValues = []
        for col in row:
            rowOfValues.append('D')
        gridOfDirt.append(rowOfValues)


    height = len(gridOfDirt)
    width = len(gridOfDirt[0])

    # placement of the turtles
    locationsOfTheTurtles = findingThelocationsOfTurtles(numberOfTurtles, height, width)

    numberOfBlocksToScanForEachTurtle = height*width/numberOfTurtles

    gridOfDirt = startDiging(gridOfDirt, locationsOfTheTurtles, numberOfBlocksToScanForEachTurtle, numberOfTurtles, width, amountOfFuel)
    return gridOfDirt

inputFile = open("dirt.csv")

print(diggingUpDirt(inputFile, 5))