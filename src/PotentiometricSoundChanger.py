import pyfirmata
import time
import os

device = "/dev/ttyUSB0"

board = pyfirmata.Arduino(device)
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        sound_volume = int(analog_value * 100)
        os.system("amixer set Master {0:s}%".format(str(sound_volume)))
    time.sleep(0.01)

