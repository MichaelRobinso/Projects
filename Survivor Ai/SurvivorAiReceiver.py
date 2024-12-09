import event, time, cyberpi, mbot2, mbuild

cyberpi.wifi.connect("Verizon_XCR9LH", "chary-dna6-nap")
while not cyberpi.wifi.is_connect():
    # DO SOMETHING
    pass

cyberpi.console.println("Connected!")

cyberpi.audio.set_volume(100)
CurrentLives = [2]
CurrentGens = [1]


@event.receive("scanforgens")
def repair():
    if mbuild.quad_rgb_sensor.get_green(3, index=1) > 125 and mbuild.quad_rgb_sensor.get_green(3, index=1) < 135:
        CurrentGens[0] = CurrentGens[0] - 1
        cyberpi.display.show_label("You have found a generator!  It has been repaired.", 10, 20, 40)
    else:
        cyberpi.display.show_label("You are not at a generator yet", 10, 20, 40)
    time.sleep(3)
    cyberpi.display.clear()
    pass


@event.receive("youwin")
def winning():
    cyberpi.display.show_label('You Have Escaped HORRAYY!!!!', 10, 20, 40)
    cyberpi.audio.play_tone(500, .1)
    cyberpi.audio.play_tone(600, .1)
    cyberpi.audio.play_tone(720, 1)
    time.sleep(2)
    cyberpi.display.clear()
    pass


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
        scanforhit = cyberpi.mesh_broadcast.get("hit")
        if message == 1:
            mbot2.forward(50)

        elif message == 2:
            mbot2.backward(50)

        elif message == 3:
            mbot2.turn(-45)

        elif message == 4:
            mbot2.turn(45)

        elif message == 5:
            cyberpi.broadcast("scanforgens")

        elif message == 0:
            mbot2.forward(0)

        if CurrentLives[0] == 0:
            cyberpi.display.show_label('You Are Dead...', 10, 20, 40)
            cyberpi.audio.play_tone(400, .1)
            cyberpi.audio.play_tone(300, .1)
            cyberpi.audio.play_tone(250, .2)
            time.sleep(10)

        if mbuild.quad_rgb_sensor.get_blue(3, index=1) >= 90 and mbuild.quad_rgb_sensor.get_blue(3, index=1) <= 110 and CurrentGens[0] < 1:
            cyberpi.broadcast("youwin")

        if scanforhit == 1:
            CurrentLives[0] = CurrentLives[0] - 1
            cyberpi.display.show_label('You Have Been Hit Runnn!!!!', 10, 20, 40)
            cyberpi.audio.play_tone(300, .1)
            cyberpi.audio.play_tone(200, .1)
            time.sleep(2)
            cyberpi.display.clear()

        elif scanforhit == 0:
            scanforhit = 0
