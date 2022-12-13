import time

# Countdown without threading

# Define the countdown function

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Time is up')
  
# Input the time 
t = input("Enter the time in seconds: ")
  
# Call the function

countdown(int(t))