#!/bin/sh

set -eu

yt build
cp build/bbc-microbit-classic-gcc/src/cpp-hello-combined.hex /media/removable/MICROBIT/
