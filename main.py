def solveFirstPart(leftArray, rightArray):
        finalSum = 0
        sortAscending(leftArray)
        sortAscending(rightArray)

        print(leftArray)
        print(rightArray)

        for x in range(len(leftArray)):
            finalSum += abs(leftArray[x] - rightArray[x])

        return finalSum

def sortAscending(array):
    for x in range(len(array)):
        for z in range(len(array) - 1):
            if array[z] <= array[z+1]:
                y = array[z]
                array[z] = array[z+1]
                array[z+1] = y

def solveSecondPart(leftArray, rightArray):
    arrLength = len(leftArray)
    finalSum = 0

    for x in range(arrLength):
        occurrences = 0
        for y in range (arrLength):
            if leftArray[x] == rightArray[y]:
                occurrences += 1
        finalSum += leftArray[x] * occurrences

    return finalSum

if __name__ == '__main__':

    with open("files/input.txt") as inputFile:
        lines = inputFile.readlines()
        leftArray = []
        rightArray = []
        for line in lines:
            split = line.split(' ')
            leftArray.append(int(split[0]))
            rightArray.append(int(split[3][:-1]))

        print(solveFirstPart(leftArray, rightArray))
        print(solveSecondPart(leftArray, rightArray))
