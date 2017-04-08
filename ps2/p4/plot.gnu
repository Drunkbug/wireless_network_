# Gnuplot script for plotting heurestics
set term png
set grid
set output "heuristic0.png"
set xlabel "Running Times"
set ylabel "# of APs"
set style line 1 lc rgb '#0060ad' lt 1 lw 1
plot 'heuristic0.txt' using 1:2 with linespoint ls 1 title "Number of APs"

set output "heuristic1.png"
set xlabel "Running Times"
set ylabel "# of APs"
plot 'heuristic1.txt' using 1:2 with linespoint ls 1 title "Number of APs"

set output "heuristic2.png"
set xlabel "Running Times"
set ylabel "# of APs"
plot 'heuristic2.txt' using 1:2 with linespoint ls 1 title "Number of APs"
