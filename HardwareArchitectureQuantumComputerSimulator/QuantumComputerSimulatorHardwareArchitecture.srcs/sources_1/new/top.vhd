
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity top is
 generic(
    nCores: integer:=2; 
    precision: integer:=64; 
    maxQubits: integer:=14; 
    baudRate : integer:=460800
);
  port(
    system_clk: in std_logic; --clock
    reset_btn: in std_logic; --reset the current program
    tx: out std_logic; --data out
    rx: in std_logic; --data in
    seg: out std_logic_vector(6 downto 0); --seven segment leds
    an: out std_logic_vector(3 downto 0); --seven segment digits
    led : out std_logic_vector(15 downto 0)--overflow leds
    );
end top;

architecture Behavioral of top is

    --declare components
    
    component ClockGenerator
        port
         (-- Clock in ports
          -- Clock out ports
          clk_out_100          : out    std_logic;
          clk_out_200          : out    std_logic;
          -- Status and control signals
          reset             : in     std_logic;
          locked            : out    std_logic;
          clk_in           : in     std_logic
         );
     end component;
        
     component Timer is
        Port ( 
            clk : in std_logic;
            count_en : in std_logic;
            reset : in std_logic;
            seg: out std_logic_vector(6 downto 0);
            an: out std_logic_vector(3 downto 0);
            overflow: out std_logic_vector(15 downto 0)
            );
     end component;
          
    --signals (unique Input signals to components are organized into groups, general multiused signals like clocks are also organized into groups)
    
    --clocks
    signal w_clk_100 : std_logic;
    signal w_clk_200 : std_logic;
    signal w_clk_rdy : std_logic;
    
    --reset
    signal w_main_reset : std_logic;
    
    --Timer
    signal w_timer_count_en : std_logic;
    
    

begin
   ClockGenerator_inst : ClockGenerator
       port map ( 
              -- Clock out ports  
               clk_out_100 => w_clk_100,
               clk_out_200 => w_clk_200,
              -- Status and control signals                
               reset => w_main_reset,
               locked => w_clk_rdy,
               -- Clock in ports
               clk_in => system_clk
             );
    
    Timer_inst : Timer
        port map(
            clk => w_clk_100,
            count_en => w_timer_count_en,
            reset => w_main_reset,
            seg => seg,
            an => an,
            overflow => led
            );
            

    
end Behavioral;
