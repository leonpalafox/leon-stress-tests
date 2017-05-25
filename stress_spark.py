import pandas as pd
import numpy as np
from operator import add
from pyspark.sql.functions import col, lit
from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext
import pyspark.sql.functions as F

def sorti(x):
	a = np.sort(x)
	return np.mean(a[:4])
test_df = pd.DataFrame(np.random.rand(10000,10000))
sqlCtx = SQLContext(sc)
df = sqlCtx.createDataFrame(test_df) #Create the dataframe in spark
import timeit
start_time = timeit.default_timer()
rowMean  = (reduce(add, (col(x) for x in df.columns[:4])) / 5).alias("mean")
df.select(rowMean)
elapsed = timeit.default_timer() - start_time
print(elapsed)