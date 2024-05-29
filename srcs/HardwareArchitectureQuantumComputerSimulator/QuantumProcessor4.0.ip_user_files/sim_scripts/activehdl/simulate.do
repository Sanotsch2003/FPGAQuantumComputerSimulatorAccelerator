transcript off
onbreak {quit -force}
onerror {quit -force}
transcript on

asim +access +r +m+quantumProcessor_tb  -L xpm -L xil_defaultlib -L unisims_ver -L unimacro_ver -L secureip -O5 xil_defaultlib.quantumProcessor_tb xil_defaultlib.glbl

do {quantumProcessor_tb.udo}

run 1000ns

endsim

quit -force
