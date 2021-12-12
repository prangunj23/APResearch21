from bfs import computationtimebfs, statesexploredbfs, manhattandistance, pathlengthbfs, numberofwalls
from dfs import sizeofmaze, initialneighbors, computationtimedfs, statesexploreddfs, pathlengthdfs
from csv import writer
# dfs = 1
# bfs = 0
if pathlengthbfs > pathlengthdfs:
    value = 1
    
elif pathlengthbfs == pathlengthdfs:
    if statesexploredbfs > statesexploreddfs:
        value = 1
        
    elif statesexploredbfs == statesexploreddfs:
        if computationtimebfs > computationtimedfs:
            value = 1
            
        else:
            value = 0
            
    else:
        value = 0
        
else:
    value = 0
    

Input = [sizeofmaze, initialneighbors, manhattandistance, numberofwalls, value]

with open('data.csv', 'a') as item:

    writeritem = writer(item)

    writeritem.writerow(Input)

    item.close()

