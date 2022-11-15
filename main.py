from replit import audio
import os, time


print("🎵 MyPOD Music Player")
print()
print("Press 1 to Play")
print("Press 2 to Exit")
print()
print("Press anything else to see the menu again.")


def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()

while True:
  # clear the screen 
  os.system("clear")

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input

def quit():
  exit = ""
  while exit.lower() != "no" or exit.lower() != "n":  
    exit = input("Do you want to generate another health stat? ") 
    if exit.lower() == "yes" or exit.lower() == "y" or exit =="":
      name = promptUser()
      dice_6_8() 
    else:
     print()
     print("Shutting down ⚔️ Character Stats Generator...")
     break
      

def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run to generate health stats.""")
    print()
    continue


if __name__=="__main__":
  
  endGame()