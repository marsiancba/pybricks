from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController

hub = PrimeHub()

print("Connecting to Xbox controller...")
xbox = XboxController()
print("Xbox controller connected!")

motorZ = Motor(Port.D, Direction.CLOCKWISE)
motorL = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motorP = Motor(Port.B, Direction.CLOCKWISE)
colorSensor = ColorSensor(Port.C)


hub.speaker.beep()

def sound_shot():  # Y button
    for f, d in [(4000, 8), (2500, 20), (1000, 40)]:
        hub.speaker.beep(f, d)

def sound_laser():  # A button
    for f in range(800, 3000, 400):
        hub.speaker.beep(f, 10)
    for f in range(3000, 800, -600):
        hub.speaker.beep(f, 10)

def sound_robot():  # B button
    for f, d in [(600, 80), (900, 80), (1200, 80)]:
        hub.speaker.beep(f, d)

def sound_magic():  # X button
    for f, d in [(1000, 50), (1300, 50), (1600, 50), (2000, 100)]:
        hub.speaker.beep(f, d)

last_buttons = set()

while True:
    j=xbox.joystick_right()
    k=xbox.joystick_left();

    angle = j[0]*0.3
    speed = k[1]

    #motorZ.track_target(j[0])
    #motorZ.run(400)

    motorZ.run_target(400, angle, then=Stop.BRAKE, wait=Stop.NONE)
    motorL.dc(speed)
    motorP.dc(speed)

    pressed = xbox.buttons.pressed()  # current pressed buttons

    new_presses = set(pressed) - last_buttons

    if Button.Y in new_presses:
        sound_shot()
    if Button.A in new_presses:
        sound_laser()
    if Button.B in new_presses:
        sound_robot()
    if Button.X in new_presses:
        sound_magic()

    # D-pad display control
    if Button.UP in new_presses:
        hub.display.icon([[  0,   0, 100,   0,   0],
                          [  0, 100, 100, 100,   0],
                          [100,   0, 100,   0, 100],
                          [  0,   0, 100,   0,   0],
                          [  0,   0, 100,   0,   0]])  # Arrow up
        print("D-pad UP: Arrow up")
    if Button.DOWN in new_presses:
        hub.display.icon([[  0,   0, 100,   0,   0],
                          [  0,   0, 100,   0,   0],
                          [100,   0, 100,   0, 100],
                          [  0, 100, 100, 100,   0],
                          [  0,   0, 100,   0,   0]])  # Arrow down
        print("D-pad DOWN: Arrow down")
    if Button.LEFT in new_presses:
        hub.display.icon([[  0,   0, 100,   0,   0],
                          [  0, 100,   0,   0,   0],
                          [100, 100, 100, 100, 100],
                          [  0, 100,   0,   0,   0],
                          [  0,   0, 100,   0,   0]])  # Arrow left
        print("D-pad LEFT: Arrow left")
    if Button.RIGHT in new_presses:
        hub.display.icon([[  0,   0, 100,   0,   0],
                          [  0,   0,   0, 100,   0],
                          [100, 100, 100, 100, 100],
                          [  0,   0,   0, 100,   0],
                          [  0,   0, 100,   0,   0]])  # Arrow right
        print("D-pad RIGHT: Arrow right")

    last_buttons = set(pressed)

    wait(50)

