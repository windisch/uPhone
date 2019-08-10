from uphone.board import Board


class Mic(object):

    def __init__(self, pin_name):
        self.adc = Board.get_adc_of_pin(pin_name)

    def get_data(self, time=1, frequency=15):
        """

        Converts the analog values of the mic to digital values. In a totally silent environment, the
        measured value is V_CC/2.

        Args:
            time (int): Time (in seconds) to sample
            frequency (int): Frequency (in Hz) to sample
        """
        timer = Board.get_timer(frequency)
        data = Board.get_array(time*frequency)

        # logger.info('Start listening')
        self.adc.read_timed(data, timer)
        return data
