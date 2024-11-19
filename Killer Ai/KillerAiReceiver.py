import event, time, cyberpi, mbot2

cyberpi.wifi.connect("CIS_WiFi", "CIS!2018#WiFi")
while not cyberpi.wifi.is_connect():
    # DO SOMETHING
    pass

cyberpi.console.println("Connected!")

@cyberpi.event.mesh_broadcast("message")
def mesh_broadcast():
    cyberpi.console.println('received')
    pass

@event.is_press('a')
def control():
    while True:
        '''
        0 = neutral
        1 = up
        2 = down
        3 = left
        4 = right
        '''
        message = cyberpi.mesh_broadcast.get("message")
        cyberpi.console.println(str(message))
        if message == 1:
            mbot2.forward(50)

        elif message == 2:
            mbot2.backward(50)

        elif message == 3:
            mbot2.turn(50)

        elif message == 4:
            mbot2.turn_right(50)

        elif message == 0:
            mbot2.forward(0)
