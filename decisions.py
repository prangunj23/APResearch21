from bfs import computationtimebfs, statesexploredbfs, manhattandistance
from dfs import sizeofmaze, initialneighbors, computationtimedfs, statesexploreddfs
from csv import writer
# dfs = 1
# bfs = 0
if statesexploredbfs > statesexploreddfs:
    value = 0
elif statesexploredbfs == statesexploreddfs:
    if computationtimebfs > computationtimedfs:
        value = 0
    else:
        value = 1
else:
    value = 1

Input = [sizeofmaze, initialneighbors, manhattandistance, value]

with open('data.csv', 'a') as item:

    writeritem = writer(item)

    writeritem.writerow(Input)

    item.close()

