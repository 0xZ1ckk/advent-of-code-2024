def getTotalDistance():
    with open("files/input.txt") as inputFile:
        lines = inputFile.readlines()
        leftArray = []
        rightArray = []
        sum = 0
        for line in lines:
            split = line.split(' ')
            leftArray.append(int(split[0]))
            rightArray.append(int(split[3][:-1]))

        sortAscending(leftArray)
        sortAscending(rightArray)

        print(leftArray)
        print(rightArray)

        for x in range(len(leftArray)):
            sum += abs(leftArray[x] - rightArray[x])

        return sum

def sortAscending(array):
    for x in range(len(array)):
        for z in range(len(array) - 1):
            if array[z] <= array[z+1]:
                y = array[z]
                array[z] = array[z+1]
                array[z+1] = y

if __name__ == '__main__':

    print(getTotalDistance())

