-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2023 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2023.2 (win64) Build 4029153 Fri Oct 13 20:14:34 MDT 2023
-- Date        : Sun Mar 10 17:39:29 2024
-- Host        : Jonas-PC running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode synth_stub {c:/Users/Jonas/Nextcloud/Jugend Forscht/Simulation von
--               Quantencomputern/Code/Versions/QuantumProcessor4.0/QuantumProcessor4.0.gen/sources_1/ip/clockGenerator/clockGenerator_stub.vhdl}
-- Design      : clockGenerator
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity clockGenerator is
  Port ( 
    clk_100 : out STD_LOGIC;
    clk_200 : out STD_LOGIC;
    clk_250 : out STD_LOGIC;
    reset : in STD_LOGIC;
    locked : out STD_LOGIC;
    clk_in : in STD_LOGIC
  );

end clockGenerator;

architecture stub of clockGenerator is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "clk_100,clk_200,clk_250,reset,locked,clk_in";
begin
end;
