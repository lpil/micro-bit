# Why is this so noisy? :(

import microbit
import audio
import math

SAMPLE_RATE = 7812.5 * 1000
TWO_PI = math.pi * 2.0
MAX_AMPLITUDE = 124


def make_frame_iterator(frequency):
    frame = audio.AudioFrame()
    frame_length = len(frame)
    position_in_period = 0.0
    position_in_period_delta = frequency / SAMPLE_RATE

    while True:
        for i in range(frame_length):
            # frame[i] = int(math.sin(position_in_period * TWO_PI) * MAX_AMPLITUDE + 124)
            frame[i] = int(math.sin(math.pi * i / 16) * MAX_AMPLITUDE + 128.5)

        yield frame

        position_in_period = position_in_period + position_in_period_delta

        if position_in_period >= 1.0:
            position_in_period = position_in_period - 1.0


iterator = make_frame_iterator(440)

audio.play(iterator)
