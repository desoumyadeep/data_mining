#!/usr/bin/env python
from scipy import spatial

dataSetI = [0.8,0.6]
dataSetII = [16,12]
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)

print(result)