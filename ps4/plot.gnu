# Gnuplot script
set term png
set output "./data_0_5.png"
set logscale y 10
set xlabel "Eb/N0 (dB)"
set ylabel "Probability of bit error (BER)"
set style line 1 lc rgb '#0060ad' lt 1 lw 1.5
set style line 2 lc rgb '#FA9D00' lt 1 lw 1.5
plot "./data_0_5.dat" using 1:2 with lines ls 1 title "BER", "" using 1:3 with lines ls 2 title "Sklar"

set term png
set output "./data_0_01.png"
set logscale y 10
set xlabel "Eb/N0 (dB)"
set ylabel "Probability of bit error (BER)"
plot "./data_0_01.dat" using 1:2 with lines ls 1 title "BER", "" using 1:3 with lines ls 2 title "Sklar"
