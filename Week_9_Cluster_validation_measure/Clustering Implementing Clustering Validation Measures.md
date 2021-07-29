## Clustering: Implementing Clustering Validation Measures

In this assignment, you will be implementing two clustering validation measures: Normalized Mutual Information (NMI) and Jaccard similarity. 

**Input Format**

The input of each test case includes *n* lines. Each line *i* includes two numbers separated by a space. The first number is the ground-truth cluster label of the *i*-th instance, and the second number is the predicted cluster label of the *i*-th instance. Sample 0 is an example input of five instances, where instance 1 belongs to cluster 2 and is predicted to belong to cluster 3, instance 2 belongs to cluster 0 and is predicted to belong to cluster 0...

**Constraints**

Machine learning libraries are not allowed in this assignment. For a complete list of allowed libraries, please refer to the column *standard challenges* on [this page](https://www.hackerrank.com/environment).

**Output Format**

You need to evaluate the clustering predictions with regard to the ground-truth by NMI and Jaccard measures. For each test case, your output is a single line, which includes two float numbers (rounded to **exactly 3 decimal places**) separated by a space . Sample 0 shows the example output of the example input, where the first number is NMI and the second number is Jaccard similarity.

You will be graded based on whether your file format is correct and on how many of the measures you submitted are correct.

**Sample Input 0**

```
2 3
0 0
0 1
1 1
2 2
```

**Sample Output 0**

```
0.656 0.000
```

**Sample Input 1**

```
2 1
0 2
2 0
1 1
2 2
1 1
1 1
1 1
2 2
2 2
0 0
0 0
1 1
1 1
1 1
2 2
1 1
1 0
1 1
2 2
1 1
0 0
0 0
2 2
1 1
2 2
1 1
0 0
2 2
1 1
2 2
0 0
1 1
0 0
2 2
2 2
0 0
0 0
1 1
1 1
2 2
0 0
0 0
2 2
0 0
1 1
0 2
1 1
0 0
1 1
2 2
1 1
1 1
1 1
1 1
1 1
2 2
0 0
1 1
2 2
2 2
0 0
0 0
0 0
1 1
0 0
0 0
1 1
2 2
0 0
2 2
1 1
1 1
2 2
2 2
0 0
2 2
2 2
1 1
0 0
0 0
1 2
0 0
0 0
1 1
2 2
1 1
2 2
1 1
2 2
0 0
1 1
1 1
0 0
1 1
2 2
1 1
1 1
2 2
1 1
2 2
2 2
2 2
1 1
2 2
2 2
1 1
0 0
0 0
1 1
0 0
2 2
0 0
1 1
0 0
0 0
2 2
0 0
2 2
2 2
2 2
2 2
0 0
0 0
2 2
0 0
0 0
0 0
2 2
0 0
2 2
0 0
1 1
0 1
1 1
2 2
2 2
0 0
0 0
2 2
1 1
0 0
0 0
0 0
2 2
0 0
0 0
1 1
0 0
0 0
2 2
0 0
0 0
2 2
2 2
2 2
2 2
1 1
1 1
1 1
0 0
1 1
2 2
2 2
0 0
2 1
0 0
0 0
2 2
0 0
1 1
2 2
0 0
0 0
1 1
1 1
0 0
0 0
1 0
1 1
2 2
2 2
0 0
0 0
2 1
0 0
1 1
2 2
2 2
1 1
1 1
2 2
0 0
1 1
0 0
1 1
0 0
1 1
0 0
2 2
1 1
2 2
2 2
1 1
0 0
1 1
0 0
1 1
2 2
0 0
1 1
2 2
1 1
2 2
2 2
1 1
0 0
2 2
1 1
2 2
2 2
2 2
0 0
2 2
1 1
2 2
1 1
1 1
0 0
1 1
1 1
1 1
0 0
1 1
1 1
0 0
1 1
2 2
1 1
0 0
0 0
2 2
0 0
1 1
2 2
0 0
0 0
1 1
0 0
0 0
1 1
1 1
1 1
2 2
0 0
0 0
2 2
2 2
2 2
0 0
0 0
2 2
1 1
2 2
2 2
1 1
2 2
0 0
1 1
2 2
1 1
0 0
2 2
1 1
1 1
2 2
1 1
2 2
1 1
0 0
1 1
0 0
1 1
1 1
1 1
0 0
0 0
2 2
1 1
0 0
2 2
0 0
2 2
2 2
2 2
0 0
0 0
2 2
2 2
2 2
```

**Sample Output 1**

```
0.849 0.877
```