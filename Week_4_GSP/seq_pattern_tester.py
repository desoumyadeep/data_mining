#!/usr/bin/env python
# $example on$
from pyspark.ml.fpm import PrefixSpan
# $example off$
from pyspark.sql import Row, SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("PrefixSpanExample")\
        .getOrCreate()
    sc = spark.sparkContext

    # $example on$
    df = sc.parallelize([Row(sequence=[["b","d"], ["a"], ["e"], ["f", "c"], ["d"]]),
                         Row(sequence=[["a"], ["c"], ["d", "e"], ["c"], ["f"], ["g"]]),
                         Row(sequence=[["c"], ["f"], ["b", "d"], ["a"], ["e"], ["c"], ["g"]])]).toDF()

    prefixSpan = PrefixSpan(minSupport=1, maxPatternLength=5,
                            maxLocalProjDBSize=32000000)

    # Find frequent sequential patterns.
    prefixSpan.findFrequentSequentialPatterns(df).show()
    # $example off$

    spark.stop()

'''
(b d) a e (f c) d
a c (d e) c f g
c f (b d) a e c g
'''
