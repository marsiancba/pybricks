from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Direction, Port
from pybricks.tools import wait
from pybricks.iodevices import XboxController

hub = PrimeHub()

print("Connecting to Xbox controller...")
xbox = XboxController()
print("Xbox controller connected!")

motorE = Motor(Port.E, Direction.CLOCKWISE)
motorC = Motor(Port.C, Direction.CLOCKWISE)

hub.speaker.beep()

MOTOR_SPEED = 100
MOTOR_C_SPEED = 500
last_buttons = set()
motorC_direction = 1

while True:
    pressed = xbox.buttons.pressed()
    new_presses = set(pressed) - last_buttons

    if Button.UP in pressed:
        motorE.dc(MOTOR_SPEED)
    elif Button.DOWN in pressed:
        motorE.dc(-MOTOR_SPEED)
    else:
        motorE.dc(0)

    if Button.Y in new_presses:
        motorC_direction = -motorC_direction

    if Button.Y in pressed:
        motorC.run(MOTOR_C_SPEED * motorC_direction)
    else:
        motorC.stop()

    last_buttons = set(pressed)

    wait(50)
