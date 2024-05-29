library IEEE;
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;

entity quantumProcessor_tb is
end;

architecture bench of quantumProcessor_tb is

  component quantumProcessor
  generic(
      nCores: integer:=1;
      precision: integer:=64;
      maxQubits: integer:=14;
      baudRate : integer:=460800;
      clockFrequency : integer:=200000000;
      instruction_address_width : integer:=10;
      instruction_width : integer := 8
  );
  port(
      clk: in std_logic;
      reset_btn: in std_logic;
      tx: out std_logic;
      rx: in std_logic;
      seg: out std_logic_vector(6 downto 0);
      an: out std_logic_vector(3 downto 0);
      led : out std_logic_vector(15 downto 0);
      clk_reset: in std_logic
      );
  end component;

  signal clk: std_logic;
  signal reset_btn: std_logic;
  signal tx: std_logic;
  signal rx: std_logic;
  signal seg: std_logic_vector(6 downto 0);
  signal an: std_logic_vector(3 downto 0);
  signal clk_reset: std_logic ;
  signal stop_the_clock : std_logic := '0';
  signal led : std_logic_vector(15 downto 0);
  
  constant clock_period: time := 10 ns;

begin

  -- Insert values for generic parameters !!
  uut: quantumProcessor 
                          generic map ( nCores                  => 2,
                                      precision                 => 64,
                                      maxQubits                 => 14,
                                      baudRate                  => 460800,
                                      clockFrequency            => 100000000,
                                      instruction_address_width => 10,
                                      instruction_width         =>  8)
                           port map ( clk                       => clk,
                                      reset_btn                 => reset_btn,
                                      tx                        => tx,
                                      rx                        => rx,
                                      seg                       => seg,
                                      an                        => an,
                                      clk_reset                 => clk_reset,
                                      led                       => led);

  stimulus: process
  begin
    reset_btn <= '0';
    -- Put initialisation code here


    -- Put test bench stimulus code here
    wait for 10ms;

  end process;

  clocking: process
  begin
    while not stop_the_clock = '1' loop
      clk <= '0', '1' after clock_period / 2;
      wait for clock_period;
    end loop;
    wait;
  end process;

end;

