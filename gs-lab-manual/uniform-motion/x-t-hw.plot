y(x)=100-50*x
set title "y-position vs. time" 
set xlabel "t (s)" 
set ylabel "y (m)" 
set nokey
set grid
#set yrange [-2:2]
set term postscript eps enhanced 
set output "x-t-graph.eps"
plot [0:5] y(x)
pause -1