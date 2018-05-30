set term png
set title "testing least square fitting"
set xlabel "x"
set ylabel "y"
set output 'result.png'
set key autotitle columnhead
set key top left
p[0:][0:] 'data' w p pt 5 lc -1, 1.02435100*x -0.120001793 w l lw 2 t "y=1.02435x-0.1200"
