y(x)=5+4*x
set title "x-position vs. time" 
set xlabel "t (s)" 
set ylabel "x (m)" 
set nokey
set grid
set yrange [0:30]
set term postscript eps enhanced 
set output "x-t-graph.eps"
plot [0:5] y(x)
pause -1