import microbit
import music
import random

while True:
    frequency = random.randint(10, 100)
    music.pitch(frequency, duration=-1, wait=False)
    microbit.sleep(1500)
