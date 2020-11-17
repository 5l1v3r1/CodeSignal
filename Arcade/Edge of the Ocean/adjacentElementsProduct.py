def adjacentElementsProduct(inputArray):
    biggest = inputArray[0] * inputArray[1]
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i + 1] > biggest:
            biggest = inputArray[i] * inputArray[i + 1]

    return biggest