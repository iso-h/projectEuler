#It works give it a second

def getSmallestMultiplyByRange(lowEnd, highEnd):
    loser = False
    x = 0
    i = 1
    currentNumber = 0

    #Multiply largest number by smallest number, testing all in range, find next multiple of
    #smallest number to test.
    while True:
        currentNumber = i * highEnd
        #print(currentNumber)
        for x in range(lowEnd, highEnd):
            if currentNumber % x != 0:
                loser = True
                break

        if loser == False:
            print(currentNumber)
            return

        loser = False
        i += 1

getSmallestMultiplyByRange(1, 20)
