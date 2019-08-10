from pyb import Timer
from pyb import Pin
from pyb import ADC
from array import array


class Mic(object):

    def __init__(self, pin_name):
        self.pin = Pin(pin_name, Pin.ANALOG)
        self.adc = ADC(self.pin)

    def get_data(self, time=1, frequency=15):
        """

        Converts the analog values of the mic to digital values. In a totally silent environment, the
        measured value is V_CC/2.

        Args:
            time (int): Time (in seconds) to sample
            frequency (int): Frequency (in Hz) to sample
        """
        timer = Timer(8, freq=frequency)

        data = array('H', (0 for _ in range(time*frequency)))

        # logger.info('Start listening')
        self.adc.read_timed(data, timer)
        return data
