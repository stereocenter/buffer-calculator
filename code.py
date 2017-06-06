while True:
    try:
        pH = float(input('Enter desired pH: '))
        sodiumGoal_M = float(input('Enter desired sodium ion concentration (molar): '))
        potassiumGoal_M = float(input('Enter desired potassum ion concentration (molar): '))
        bufferGoal_M = float(input('Enter desired buffer concentration (M): '))
        volumeGoal_L = float(input('Enter desired volume (L): '))
        break
    except ValueError:
        print("Not a valid number, please try again.")
