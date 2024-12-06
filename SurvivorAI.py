import cyberpi    #All needed to allow code to work properly|
import mbot2      #                                         |
import mbuild     #                                         |
import event      #                                         |
import time       #                                         V

def survivorAI():
    # Survivor's base attributes
    base_power = 30  # Base speed
    lives = 2

    cyberpi.console.print(f"Survivor initialized with {lives} lives and base speed {base_power}.")
    
    while lives > 0:
        cyberpi.console.print("Survivor is moving...")
        time.sleep(1)  # Simulate movement
        # Simulate being hit (for example purposes, this always triggers)
        is_hit = True  # Replace with actual detection logic
        if is_hit:
            lives, base_power = survivor_IsHit(lives, base_power)
            if lives <= 0:
                cyberpi.console.print("Survivor has died.")
                break

        # Reset base speed after the hit logic ends
        base_power = 30
    cyberpi.console.print("Game Over!")

def survivor_IsHit(lives, base_power):
    # Logic for when the survivor is hit
    cyberpi.console.print("Survivor is hit!")
    lives -= 1
    base_power = 45  # Temporary speed boost
    cyberpi.console.print(f"Speed increased to {base_power} for 5 seconds.")
    
    # Simulate temporary speed boost
    time.sleep(1)
    cyberpi.console.print("Speed boost ended.")
    return lives, base_power


#@event.is_press('a')
#def swing():
#    if mbuild.ultrasonic2.get() <= 10:
#        if quad_rgb_sensor.is_color(color = "red") == True:
#            cyberpi.mesh_broadcast.set('survivor1hit', 0)
#        if quad_rgb_sensor.is_color(color = "blue") == True:
#            cyberpi.mesh_broadcast.set('survivor2hit', 0)
#    time.sleep(2)
#-----------------------------------------------
#import cyberpi
#import time

# Initialize lives for both survivors
#survivor1_lives = 2
#survivor2_lives = 2

# Define the handler for "survivor1hit"
#@cyberpi.mesh_broadcast.on("survivor1hit")
#def handle_survivor1hit(data):
#    global survivor1_lives
#    survivor1_lives -= 1
#    print(f"Survivor 1 hit! Remaining lives: {survivor1_lives}")
#    if survivor1_lives <= 0:
#        print("Survivor 1 is eliminated!")
        #break

# Define the handler for "survivor2hit"
#@cyberpi.mesh_broadcast.on("survivor2hit")
#def handle_survivor2hit(data):
#    global survivor2_lives
#    survivor2_lives -= 1
#    print(f"Survivor 2 hit! Remaining lives: {survivor2_lives}")
#    if survivor2_lives <= 0:
#        print("Survivor 2 is eliminated!")
        # Optionally, add logic to disable Survivor 2's movement or actions.
