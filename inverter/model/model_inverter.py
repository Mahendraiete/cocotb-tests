class model_inverter:

    def __init__(self, width):
        self.width = width

    def process(self, input):
        return (2**self.width-1) - input
