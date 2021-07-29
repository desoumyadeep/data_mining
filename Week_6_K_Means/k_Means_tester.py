#!/usr/bin/env python
from numpy.lib.function_base import place
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame


# Load Data
data = pd.read_csv('./dataset/Input/places.txt')
#data.head()
places = data[["x", "y"]]
places["total"] = round(abs(places["x"]) + abs(places["y"]))
places["rnk"] = places["total"].rank(method="dense")



# Start Algorithm
# Step 1: No. of Clusters
K = 3
Centroids = pd.DataFrame(columns=places.columns)



for i in range(K):
    for index, row in places.iterrows():
        if int(row["rnk"]) == (i+1):
            Centroids.loc[i] = row
            break


# Step 2: Select Random Centroids
# Centroids = (places.sample(n=K))

# print (Centroids)

# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4

diff = 1
j = 0

while(diff != 0):
    XD = places
    i = 1

    # Calculate the distance from the centroids for every rows and add list to DF
    for index1, row_c in Centroids.iterrows():
        ED = []
        
        for index2, row_d in XD.iterrows():
            d1 = (row_c["x"]-row_d["x"])**2
            d2 = (row_c["y"]-row_d["y"])**2
            d = np.sqrt(d1+d2)
            ED.append(d)
        places[i] = ED
       
        i = i+1

    C = []
    for index, row in places.iterrows():
        min_dist = row[1]
        pos = 1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos = i+1
        C.append(pos)
    places["Cluster"] = C
    Centroids_new = places.groupby(["Cluster"]).mean()[["y", "x"]]
    if j == 0:
        diff = 1
        j = j+1
    else:
        diff = (Centroids_new['y'] - Centroids['y']).sum() + \
            (Centroids_new['x'] - Centroids['x']).sum()
        # print(diff.sum())
    Centroids = places.groupby(["Cluster"]).mean()[["y", "x"]]

# print(Centroids)
# print(places)
for index, row in places.iterrows():
    print('{0} {1}'.format(index, int( row["Cluster"]) - 1))


# print(places)

'''
color = ['blue', 'green', 'cyan']
for k in range(K):
    data = places[places["Cluster"] == k+1]
    plt.scatter(data["x"], data["y"], c=color[k])
plt.scatter(Centroids["x"], Centroids["y"], c='red')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
'''

'''
                 y           x
Cluster                       
1        43.476248  -80.528372
2        33.460490 -112.071606
3        35.217097  -80.844227
'''
