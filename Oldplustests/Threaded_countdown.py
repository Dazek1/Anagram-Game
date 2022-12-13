import threading
import time     

# Countdown with threading (I think!?)

# Define the countdown function

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print("You're out of time!\n")

# Note below for reminder!
    # add some function which stops the game, for example by changing a variable to false (which the main thread always checks) or some other method like by checking count_thread.is_alive()
    
# Input the time

t = input("Enter the time in seconds: ")


def initiate_game():
    count_thread = threading.Thread(None, countdown(int(t)))
    
initiate_game()
   