y(x)=25-5*x
set title "x-position vs. time" 
set xlabel "t (s)" 
set ylabel "x (cm)" 
set nokey
set grid
#set yrange [-2:2]
set term postscript eps enhanced 
set output "x-t-graph.eps"
plot [0:10] y(x)
pause -1