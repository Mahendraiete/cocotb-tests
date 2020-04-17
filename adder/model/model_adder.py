class model_adder:

    def __init__(self, width):
        self.width = width

    def process(self, input_a, input_b):
        return (input_a + input_b) % 2 ** self.width
