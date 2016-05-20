y(x)=10-2.5*x
set title "y-velocity vs. time" 
set xlabel "t (s)" 
set ylabel "v_y (m/s)" 
set nokey
set grid
set yrange [-12:12]
set term postscript eps enhanced 
set output "v-t-graph.eps"
plot [0:8] y(x)
pause -1