vlib modelsim_lib/work
vlib modelsim_lib/msim

vlib modelsim_lib/msim/xpm
vlib modelsim_lib/msim/xil_defaultlib

vmap xpm modelsim_lib/msim/xpm
vmap xil_defaultlib modelsim_lib/msim/xil_defaultlib

vlog -work xpm  -incr -mfcu  -sv "+incdir+../../../QuantumProcessor4.0.gen/sources_1/ip/clockGenerator" \
"C:/Xilinx/Vivado/2023.2/data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv" \

vcom -work xpm  -93  \
"C:/Xilinx/Vivado/2023.2/data/ip/xpm/xpm_VCOMP.vhd" \

vlog -work xil_defaultlib  -incr -mfcu  "+incdir+../../../QuantumProcessor4.0.gen/sources_1/ip/clockGenerator" \
"../../../QuantumProcessor4.0.gen/sources_1/ip/clockGenerator/clockGenerator_clk_wiz.v" \
"../../../QuantumProcessor4.0.gen/sources_1/ip/clockGenerator/clockGenerator.v" \

vcom -work xil_defaultlib  -93  \
"../../../QuantumProcessor4.0.srcs/sources_1/new/ALU.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/RAM.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/RAMController.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/addressTempCache.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/bootloader.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/controlUnit.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/coreCache.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/indexCalculator.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/processingCore.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/programMemory.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/quantumProcessor.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/timer.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/uartTransmitter.vhd" \
"../../../QuantumProcessor4.0.srcs/sources_1/new/updateAandBCache.vhd" \
"../../../QuantumProcessor4.0.srcs/sim_1/new/testbench.vhd" \

vlog -work xil_defaultlib \
"glbl.v"

