import cyberpi
import time
import mbot2
import mbuild
import event

@event.is_press('a')
def countdown_timer():
    timer = 60  # Start the timer at 60 seconds
    for t in range(timer, -1, -1):  # Loop from 60 to 0
        cyberpi.display.show_label(str(t), 32, 45, 50)  # Display the remaining time
        time.sleep(1)  # Wait for 1 second before the next iteration
    cyberpi.display.show_label("TIME'S UP!", 24, 5, 50)  # Show message when done
    cyberpi.audio.play_drum('crash-cymbal', 0.25)
