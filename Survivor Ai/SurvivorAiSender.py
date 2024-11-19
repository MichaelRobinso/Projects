import event, time, cyberpi, mbot2
# initialize

cyberpi.wifi.connect("CIS_WiFi", "CIS!2018#WiFi")
while not cyberpi.wifi.is_connect():
    # DO SOMETHING
    pass

cyberpi.console.println("Connected!")

@event.is_press('a')
def btn_press():
    while True:
        '''
        0 = neutral
        1 = up
        2 = down
        3 = left
        4 = right
        '''
        if cyberpi.controller.is_press('up'):
            cyberpi.mesh_broadcast.set("message", 1)
            cyberpi.console.println(1)
        elif cyberpi.controller.is_press('down'):
            cyberpi.mesh_broadcast.set("message", 2)
            cyberpi.console.println(2)
        elif cyberpi.controller.is_press('left'):
            cyberpi.mesh_broadcast.set("message", 3)
            cyberpi.console.println(3)
        elif cyberpi.controller.is_press('right'):
            cyberpi.mesh_broadcast.set("message", 4)
            cyberpi.console.println(4)
        else:
            # Joystick is neutral, send stop message
            cyberpi.mesh_broadcast.set("message", 0)
            cyberpi.console.println(0)
