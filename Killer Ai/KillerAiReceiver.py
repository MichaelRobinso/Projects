import event, time, cyberpi, mbot2, mbuild
# initialize

cyberpi.wifi.connect("Verizon_XCR9LH", "chary-dna6-nap")
while not cyberpi.wifi.is_connect():
    # DO SOMETHING
    pass

cyberpi.console.println("Connected!")

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

        killer = cyberpi.mesh_broadcast.get("killer")
        cyberpi.console.println(str(killer))

        if killer == 1:
            mbot2.forward(60)
        elif killer == 2:
            mbot2.backward(60)

        elif killer == 3:
            mbot2.turn(-45)

        elif killer == 4:
            mbot2.turn(-45)

        elif killer == 5:
            cyberpi.display.show_label('Swing!!! You have to rest now.', 10, 20, 40)
            if mbuild.ultrasonic2.get() <= 10 and (mbuild.quad_rgb_sensor.get_blue(3, index=1) >= 245 or mbuild.quad_rgb_sensor.get_blue(2, index=1) >= 245):
                cyberpi.mesh_broadcast.set('hit', 1)
            else:
                cyberpi.mesh_broadcast.set('hit', 0)
            time.sleep(2)
            cyberpi.display.clear()

        elif killer == 0:
            mbot2.forward(0)
