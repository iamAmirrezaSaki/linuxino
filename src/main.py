import pyfirmata
import time
import os

board = pyfirmata.Arduino('/dev/ttyUSB0')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led_pin = board.get_pin('d:9:p')

while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        sound_volume = int(analog_value * 100)
        os.system("amixer set Master {0:s}%".format(str(sound_volume)))
        # os.system("xrandr --output eDP-1 --brightness {0:s}%".format(str(analog_value)))
    time.sleep(0.01)

