from bfs import computationtimebfs, statesexploredbfs, manhattandistance, pathlengthbfs
from dfs import sizeofmaze, initialneighbors, computationtimedfs, statesexploreddfs, pathlengthdfs
from csv import writer
# dfs = 1
# bfs = 0
if pathlengthbfs > pathlengthdfs:
    value = 1
    length = pathlengthdfs
elif pathlengthbfs == pathlengthdfs:
    if statesexploredbfs > statesexploreddfs:
        value = 1
        length = pathlengthdfs
    elif statesexploredbfs == statesexploreddfs:
        if computationtimebfs > computationtimedfs:
            value = 1
            length = pathlengthdfs
        else:
            value = 0
            length = pathlengthbfs
    else:
        value = 0
        length = pathlengthbfs
else:
    value = 0
    length = pathlengthbfs

Input = [sizeofmaze, initialneighbors, manhattandistance, length, value]

with open('data.csv', 'a') as item:

    writeritem = writer(item)

    writeritem.writerow(Input)

    item.close()

