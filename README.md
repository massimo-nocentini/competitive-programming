
# Competitive Programming

In this repo I put my programming training, mostly based on the [CP book][cpbook], against 
[UVa judge][UVa:judge]; moreover, an [index][index] is provided.

In addition, more interesting material can be found in the following places:
   - https://algocoding.wordpress.com/2015/04/21/notes-and-courses-for-competitive-programming/
   - http://www.cs.cornell.edu/~wdtseng/icpc/
   - https://algo.is/
   - http://www.martystepp.com/acm/
   - http://www3.cs.stonybrook.edu/~skiena/392/javaprograms/
   - https://crypto.stanford.edu/pbc/notes/ (not really about programming, but with interesting math)
   - http://docs.sympy.org/latest/modules/polys/wester.html (again, interesting math)

[cpbook]:http://cpbook.net/#CP3details
[UVa:judge]:https://uva.onlinejudge.org/index.php?option=com_frontpage&Itemid=1
[index]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/index.ipynb?flush_cache=true


## Python libs

My plan is to use Python as the primary language to solve problems; for this reason,
the [`python-libs`][python:libs] directory contains useful definitions to ease solving,
classified as follows:

   - **utils, IO**: [input utils][libs:input], [behavior][libs:behavior], [timing][libs:timing]
   - **bitmasking**: [bit manipulation][libs:bit:manipulation], [gray codes][libs:gray:codes]
   - **sorting**: [sorting and ordering][libs:sorting]
   - **data structures**:
      - *linear*: [team queue][libs:teamqueue]

In order to use these modules in either IPython or Jupyter notebooks sessions, just set the `PYTHONPATH`
variable, here's and example:
   
   ```bash
    PYTHONPATH=~/Developer/working-copies/programming-contests/competitive-programming/python-libs/ jupyter-notebook
   ```

[python:libs]:https://github.com/massimo-nocentini/competitive-programming/tree/master/python-libs
[libs:input]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/inpututils.py
[libs:sorting]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/sorting.py
[libs:behavior]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/behavior.py
[libs:bit:manipulation]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/bits.py
[libs:timing]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/timing.py
[libs:gray:codes]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/graycodes.py
[libs:teamqueue]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/teamqueue.py

## Tutorials

At the same time, I help myself by taking notes about programming techniques, collecting
them in Jupyter notebooks:

   - [gotchas][gotchas]
   - [bit masking][bm]
   - [gray codes][gray]
   - [backtracking][backtrack]
   - [recursively-defined structures][recursively]
   - [Conway's Game of Life][gamelife]
   - [OEIS integration][oeis-interaction]
   - [OEIS mining][oeis-mining]

[gotchas]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/gotchas.ipynb?flush_cache=true
[bm]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/bitmasking.ipynb?flush_cache=true
[gray]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/graycodes.ipynb?flush_cache=true
[backtrack]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/backtrack.ipynb?flush_cache=true
[recursively]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/recursive-structures.ipynb?flush_cache=true
[gamelife]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/gamelife.ipynb?flush_cache=true
[oeis-interaction]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/oeis-interaction.ipynb?flush_cache=true
[oeis-mining]:http://nbviewer.jupyter.org/github/massimo-nocentini/competitive-programming/blob/master/tutorials/oeis-mining.ipynb?flush_cache=true
