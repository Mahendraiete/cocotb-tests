from random import randint

import cocotb
from cocotb.clock import Clock
from cocotb.result import TestFailure
from cocotb.triggers import ClockCycles, ReadOnly, RisingEdge

from model_adder import model_adder


class test_adder:
    def __init__(self, dut):
        self.dut = dut

        self.dut.input_a <= 0
        self.dut.input_b <= 0
        self.dut.input_valid <= 0

        self.model = model_adder(int(self.dut.WIDTH))
        self.expected_outputs = []
        self.input_finished = False

    def set_input_finished(self):
        self.input_finished = True

    def test_finished(self):
        return self.input_finished and not self.expected_outputs

    @cocotb.coroutine
    def send_input(self, input_a, input_b):
        self.expected_outputs.append(self.model.process(input_a, input_b))
        self.dut.input_a <= input_a
        self.dut.input_b <= input_b
        self.dut.input_valid <= 1
        yield RisingEdge(self.dut.clk)
        self.dut.input_valid <= 0

    @cocotb.coroutine
    def check_output(self):
        while True:
            yield RisingEdge(self.dut.clk)
            yield ReadOnly()

            if self.dut.output_valid == 1:
                received_output = self.dut.output
                expected_output = self.expected_outputs.pop(0)
                if received_output != expected_output:
                    raise TestFailure()


@cocotb.test()
def adder_random_test(dut, num_tests=100):
    MAX_VALUE = 2 ** int(dut.WIDTH)

    tb = test_adder(dut)
    cocotb.fork(Clock(dut.clk, 5, 'ns').start())

    # Allow pipeline to fill with defined values
    yield ClockCycles(dut.clk, 5)

    cocotb.fork(tb.check_output())

    for i in range(num_tests):
        yield tb.send_input(randint(0, MAX_VALUE), randint(0, MAX_VALUE))

    tb.set_input_finished()

    while not tb.test_finished():
        yield RisingEdge(dut.clk)
