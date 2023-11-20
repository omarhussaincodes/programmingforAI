import random
# Colors Used: Black, White, Red, Blue, Green, Yellow

maxAttempts = 15
choicesPerAttempt = 6
colorsList = ["black", "white", "red", "green", "yellow",
              "blue", "purple", "orange", "pink", "violet"]

# Generate Random Code


def generateCode():
    result = []

    for i in range(choicesPerAttempt):
        randomIdx = random.randint(0, len(colorsList) - 1)
        result.append(colorsList[randomIdx])

    return result

# START GAME


def startGame():

    print("********* Let's Play MasterMind Game **************")
    print("Are you ready to break the code!")
    print(
        f"You will have a maximum of {maxAttempts} attempts to break the code.")

    print("**** Let's Play! *****")
    print("**************************************************************************************************")
    print(
        f"Please guess among the following listed colors:  {', '.join(map(str, colorsList))}")
    print("**************************************************************************************************")

    def validateInput(inputVal):
        if (isinstance(inputVal, str)):
            if (colorsList.count(inputVal) > 0):
                return True

        return False

    def checkIfUserWon():
        if (len(userGuesses) == len(code)):
            for i in range(len(code)):
                if (code[i] != userGuesses[i]):
                    return False

            return True

        return False

    def displayMatchesFeedback(matches, matchType):
        if (isinstance(matches, list)):
            print(
                f"You have {len(matches)} "
                f"{f'{matchType} (color only excludes exact color matches)' if matchType == 'right' else f'{matchType} (color and position)'} "
                f"matches which is/are: {', '.join(map(str, matches))}"
            )

    def provideFeedbackAfterEveryAttempt():
        # exact positions how many and which are those
        exactMatches = getExactMatches()
        if len(exactMatches) > 0:
            displayMatchesFeedback(exactMatches, "exact")
        # right match - wrong positons how many and which are those excluding the exact matches
        rightMatches = getRightMatches(exactMatches)
        if len(rightMatches) > 0:
            displayMatchesFeedback(rightMatches, "right")

    def getExactMatches():
        exactMatchesList = []

        if (len(userGuesses) == len(code)):

            for i in range(len(code)):
                value = userGuesses[i]
                if (code[i] == value):
                    exactMatchesList.append(value)

        return exactMatchesList

    def getRightMatches(exactMatchesList):
        rightMatchesDict = dict()
        rightMatchesList = []
        uniqueRightMatchesList = []

        if (len(userGuesses) == len(code)):

            for i in range(len(userGuesses)):
                value = userGuesses[i]
                if (code.count(value) > 0):
                    rightMatchesList.append(value)

        if (exactMatchesList):
            for value in rightMatchesList:
                if value not in exactMatchesList:
                    uniqueRightMatchesList.append(value)

        return uniqueRightMatchesList

    for i in range(maxAttempts):

        userGuesses = []
        print(f"********** Attempt #{i+1} **********")
        print("--------------------------------------------------------------------------------------------")
        print({', '.join(map(str, colorsList))})
        print("In each attempt, you are asked to enter a total of 6 above mentioned colors one by one.")
        print("Please Note : Colors can be repeated.")
        print("--------------------------------------------------------------------------------------------")

        for j in range(len(code)):
            while True:
                guessval = input(f"Enter Color @ position#{j+1}: ")
                userGuess = guessval.lower().replace(" ", "")
                if (validateInput(userGuess)):
                    # grab user value and perform comparison and feedback.
                    userGuesses.append(userGuess)
                    break
                else:
                    print(
                        f"xxxxxxxxxx - INVALID INPUT - Please enter {', '.join(map(str, colorsList))} colors only. - xxxxxxxxxx")

        print(
            f"Your current guessed colors: {', '.join(map(str, userGuesses))}")

        # feedback provide and check if WON
        if (checkIfUserWon()):
            print("!!!!!!!!!!! Congratulations!! You WON !!!!!!!!!!!")
            print(f"You CRACKED the CODE!")
            return
        else:
            # Give Feedback After every Attempt
            print(f"Here is your feedback for attempt #{i+1}: ")
            provideFeedbackAfterEveryAttempt()

    if (not checkIfUserWon()):
        print("HARD LUCK!! - You LOST!!")
        print(f"Here is the CODE: {', '.join(map(str, code))}")
        print(
            f"Here is YOU Guessed Colors: {', '.join(map(str, userGuesses))}")


code = generateCode()
print("CODE: ", code)
startGame()
