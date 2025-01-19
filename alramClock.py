from playsound import playsound  # For playing the alarm sound
import time  # For pausing the program during countdown

# Define a function for the alarm
def alarm(seconds):
    """
    Countdown timer that waits for the specified number of seconds 
    and plays an alarm sound when time is up.
    
    Args:
        seconds (int): Total time to wait in seconds.
    """
    time_elapsed = 0  # Tracks elapsed time

    while time_elapsed < seconds:
        time.sleep(1)  # Wait for 1 second
        time_elapsed += 1  # Increment elapsed time

        # Calculate the remaining time in minutes and seconds
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Print the remaining time dynamically on the same line
        print(f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="")

    # Play the alarm sound when time is up
    playsound("alarm.mp3")  # Ensure alarm.mp3 is in the same directory as this script

# Ask the user for input time in minutes and seconds
minutes = int(input("How many minutes to wait: "))  # Get minutes from user
seconds = int(input("How many seconds to wait: "))  # Get seconds from user

# Convert total time to seconds and call the alarm function
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
