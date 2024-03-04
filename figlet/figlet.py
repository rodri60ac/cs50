import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    string = input("Input: ")
    f = random.choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(string))

elif len(sys.argv) == 3 and sys.argv[1] in ['-f','--font'] and sys.argv[2] in fonts:
    string = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(string))

else:
    sys.exit("Invalid Usage")
