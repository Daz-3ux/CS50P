import sys
from pyfiglet import Figlet
figlet = Figlet()
import random

def main():
  cnt = len(sys.argv)
  if (cnt in [1, 3]) == False:
      print("Invalid usage")
      exit(1)
  if cnt == 1:
      random_text()
  elif cnt == 3:
      format_text(sys.argv[1], sys.argv[2])

def random_text():
    txt = input("Input: ").strip()
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(txt))

def format_text(flag, font):
    if (flag == "-f" or flag == "--font") and font in figlet.getFonts():
        txt = input("Input: ").strip()
        figlet.setFont(font=font)
        print(figlet.renderText(txt))
    else:
        print("Invalid usage")
        exit(1)
    
main()