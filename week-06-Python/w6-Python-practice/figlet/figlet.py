import sys, random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()  # list of fonts


def printOutput(inputStr, fontX):
    figlet.setFont(font=fontX)
    print("Output: ")
    outputFiglet = figlet.renderText(inputStr)
    print(outputFiglet)
    return 0


if len(sys.argv) == 1:
    inputStr = input("Input: ")
    randomFont = random.choice(fonts)
    printOutput(inputStr, randomFont)
elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and (sys.argv[2] in fonts)
):
    inputStr = input("Input: ")
    fontName = sys.argv[2]
    printOutput(inputStr, fontName)
else:
    print("Invalid usage")
    sys.exit(1)
