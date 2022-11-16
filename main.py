from replit import audio
import os, time


print("🎵 MyPOD Music Player")
print()
print("Press 1 to Play")
print("Press 2 to Exit")
print()
print("Press anything else to see the menu again.")
time.sleep(3)


def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
 

def pause():
  source = audio.play_file('audio.wav')
  source.paused = True # pause the playback
 
        
def start():
  while True:
    # clear the screen 
    os.system("clear")
  
    # Show the menu
    input()
    print("🎵 MyPOD Music Player")
    print()
    print("Press 1 to Play")
    print("Press 2 to Exit")
    print()
   
    # take user's input
    try:
      num = int(input(" "))
      print()
    except ValueError:
      print()
      print("I am expecting positive numbers.")
      print()
      continue
    # check whether you should call the play() subroutine depending on user's input
    if num == 1:
      play()
    elif num == 2:
      pause()
      break
    

def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run to play music again.""")
    print()
    continue


if __name__=="__main__":
  start()
  pause()
  endGame()