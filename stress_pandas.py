import pandas as pd
import numpy as np

test_df = pd.DataFrame(np.random.rand(10000,10000))
import timeit
start_time = timeit.default_timer()
data_neighbours = pd.DataFrame(index=test_df.columns,columns=range(1,5))
for i in range(0,len(test_df.columns)):
    data_neighbours.ix[i,:10] = test_df.ix[0:,i].sort_values(ascending=False)[:4].index
elapsed = timeit.default_timer() - start_time
print(elapsed)