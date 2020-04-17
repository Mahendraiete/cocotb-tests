library ieee;
use ieee.std_logic_1164.all;

entity add_and_invert is
    generic (
        WIDTH : positive);
    port (
        clk          : in std_ulogic;
        input_a      : in std_ulogic_vector(WIDTH - 1 downto 0);
        input_b      : in std_ulogic_vector(WIDTH - 1 downto 0);
        input_valid  : in std_ulogic;
        output       : out std_ulogic_vector(WIDTH - 1 downto 0);
        output_valid : out std_ulogic);
end entity;

architecture rtl of add_and_invert is
    signal sum       : std_ulogic_vector(WIDTH - 1 downto 0);
    signal sum_valid : std_ulogic;
begin

    i_adder : entity work.adder
        generic map(
            WIDTH => WIDTH)
        port map(
            clk          => clk,
            input_a      => input_a,
            input_b      => input_b,
            input_valid  => input_valid,
            output       => sum,
            output_valid => sum_valid);

    i_inverter : entity work.inverter
        generic map(
            WIDTH => WIDTH)
        port map(
            clk          => clk,
            input        => sum,
            input_valid  => sum_valid,
            output       => output,
            output_valid => output_valid);

end architecture;