from model_adder import model_adder
from model_inverter import model_inverter


class model_add_and_invert:

    def __init__(self, width):
        self.width = width
        self.adder = model_adder(width)
        self.inverter = model_inverter(width)

    def process(self, input_a, input_b):
        sum = self.adder.process(input_a, input_b)
        output = self.inverter.process(sum)

        return output
