from pyb import Timer
from pyb import ADC
from array import array
# import logging


# logger = logging.getLogger(__name__)


def get_data(pin, time=1, frequency=15):
    """

    Converts the analog values of the mic to digital values. In a totally silent environment, the
    measured value is V_CC/2.

    Args:
        time (int): Time (in seconds) to sample
        frequency (int): Frequency (in Hz) to sample
    """
    adc = ADC(pin)
    timer = Timer(8, freq=frequency)

    data = array('H', (0 for _ in range(time*frequency)))

    # logger.info('Start listening')
    adc.read_timed(data, timer)
    return data
