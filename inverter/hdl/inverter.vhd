library ieee;
use ieee.std_logic_1164.all;

entity inverter is
    generic (
        WIDTH : positive);
    port (
        clk          : in std_ulogic;
        input        : in std_ulogic_vector(WIDTH - 1 downto 0);
        input_valid  : in std_ulogic;
        output       : out std_ulogic_vector(WIDTH - 1 downto 0);
        output_valid : out std_ulogic);
end entity;

architecture rtl of inverter is
begin

    main_proc : process (clk)
    begin
        if rising_edge(clk) then
            output       <= not input;
            output_valid <= input_valid;
        end if;
    end process;

end architecture;