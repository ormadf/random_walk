This is a program written on python 3 for:
- non-returning random walk simulation on square lattice (2D)
- non-returning random walk in 3D
- self-avoiding random walk

Self-avoiding random walk algorithm:
  if walking 'bug' returns on the site visited before, the attempt is ditched
  and new SAW starts again from the (0,0) position on the lattice
  several attempts usually required to perform SAW because of this

GUI is written with tkinter package

Usage:
start the program from the command line :
  python gui_randwalk.py

In the GUI:
Non-returning random walk:
 choose NR random walk from the drop-down menu 
 enter number of steps for NR random walk
 click on 'start walking' button
NR random walk 3D:
  choose NR random walk 3D
  the same as above

Self-Avoiding Random Walk:
  Choose self-awoiding walk from the menu
  choose number of steps
  choose number of attempts


