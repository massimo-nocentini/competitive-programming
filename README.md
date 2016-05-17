
<script type="text/javascript" async 
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Competitive Programming

In this repo I put my programming training, mostly based on the [CP book][cpbook], against 
[UVa judge][UVa:judge].

## Python libs

My plan is to use Python as the primary language to solve problems; for this reason,
the [`python-libs`][python:libs] directory contains useful definitions to ease solving, 
such as [input utils][libs:input], [sorting and ordering][libs:sorting].


## WIP problems

   -    [UVa 10141][UVa10141]: **Request for Proposal**

## RTE problems

   -    [UVa 11093][UVa11093]: **Just Finish it up** ([code][UVa11093:code])

## Solved problems

The following content grows as a stack, namely most recently solved on top:

   -    [UVa 101][UVa101]: **The Block Problem** ([code][UV101:code])<br>
        *trick*: a sort of *double dispatching* to implement an *automaton* of 
        commands; moreover, nice play with Python `list`s
   -    [UVa 11942][UVa11942]: **Lumberjack Sequencing** ([code][UVa11942:code])<br>
        *trick*: use Python condition concatenation `a < b < c < d < e < f < g < h < i < j` 
        for asc/des order checks
   -    [UVa 11559][UVa11559]: **Event Planning** ([code][UVa11559:code])
   -    [UVa 11332][UVa11332]: **Summing Digits** ([code][UVa11332:code])<br>
        *trick*: use Python facilities to write an integer `n` in base 10; 
        the sum of its digits is `sum(map(int, str(n)))`
   -    [UVa 10114][UVa10114]: **Loansome Car Buyer** ([code][UVa10114:code])<br>
        *method*: one pass after filling vector 'piggyback', as time series for deprecation percentages
   -    [UVa 11547][UVa11547]: **Automatic Answer** ([code][UVa11547:code])<br>
        *trick*: if `a` is an integer, apply `a // 10 % 10` to get digit in decine position
   -    [UVa 11727][UVa11727]: **Cost Cutting** ([code][UVa11727:code])
   -    [UVa 11498][UVa11498]: **Division of Nlogonia** ([code][UVa11498:code])
   -    [UVa 11172][UVa11172]: **Relational Operator** ([code][UVa11172:code])

          
[cpbook]:http://cpbook.net/#CP3details

[UVa:judge]:https://uva.onlinejudge.org/index.php?option=com_frontpage&Itemid=1

[python:libs]:https://github.com/massimo-nocentini/competitive-programming/tree/master/python-libs
[libs:input]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/inpututils.py
[libs:sorting]:https://github.com/massimo-nocentini/competitive-programming/blob/master/python-libs/sorting.py

[UVa10141]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=609&page=show_problem&problem=1082

[UVa101]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=37
[UVa101:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/101.py

[UVa11093]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2034
[UVa11093:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11093.py

[UVa11942]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3093
[UVa11942:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11942.py

[UVa11559]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=2595
[UVa11559:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11559.py

[UVa11332]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=2307
[UVa11332:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11332.py

[UVa10114]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=1055
[UVa10114:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/10114.py

[UVa11547]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=607&page=show_problem&problem=2542
[UVa11547:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11547.py

[UVa11727]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2827
[UVa11727:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11727.py

[UVa11498]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2493
[UVa11498:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11498.py

[UVa11172]:https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2113
[UVa11172:code]:https://github.com/massimo-nocentini/competitive-programming/blob/master/UVa/11172.py
