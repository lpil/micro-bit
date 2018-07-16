from microbit import *

IMAGES = [
    Image.CLOCK12,
    Image.CLOCK1,
    Image.CLOCK2,
    Image.CLOCK3,
    Image.CLOCK4,
    Image.CLOCK5,
    Image.CLOCK6,
    Image.CLOCK7,
    Image.CLOCK8,
    Image.CLOCK9,
    Image.CLOCK10,
    Image.CLOCK11,
    Image.CLOCK12,
]

MAX_X = 1024

STEP_SIZE = int((MAX_X * 2) / (len(IMAGES) - 1))

while True:
    x = accelerometer.get_x()
    index = int((x + MAX_X) / STEP_SIZE)
    image = IMAGES[index]
    display.show(image)
