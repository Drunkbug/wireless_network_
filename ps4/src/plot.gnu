# Gnuplot script
set term png
set output "../data_0_5.png"
set logscale y 10
set xlabel "Eb/N0 (dB)"
set ylabel "Probability of bit error (BER)"
set style line 1 lc rgb '#0060ad' lt 1 lw 1.5
set style line 2 lc rgb '#FA9D00' lt 1 lw 1.5
set style line 3 lc rgb '#7D72F9' lt 1 lw 1.5
set style line 4 lc rgb '#dd181f' lt 1 lw 1.5
set style line 5 lc rgb '#29c524' lt 1 lw 1.5
plot "./data_0_5.dat" using 1:2 with lines ls 1 title "BER", "" using 1:3 with lines ls 2 title "Sklar"

set term png
set output "../data_0_01_comparision.png"
set logscale y 10
set xlabel "Eb/N0 (dB)"
set ylabel "Probability of bit error (BER)"
plot "./data_0_5.dat" using 1:2 with lines ls 1 title "0.5", "" using 1:3 with lines ls 2 title "Sklar", \
     "./data_0_01_th0.dat" using 1:2 with lines ls 3 title "0.01th0", \
     "./data_0_01_thn0_2.dat" using 1:2 with lines ls 4 title "0.01th-0.2", \
     "./data_0_01_th0_2.dat" using 1:2 with lines ls 5 title "0.01th0.2"
