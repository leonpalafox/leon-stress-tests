import pandas as pd
import numpy as np
def sorti(x):
	a = np.sort(x)
	return np.mean(a[:4])
test_df = pd.DataFrame(np.random.rand(10000,10000))
import timeit
start_time = timeit.default_timer()
data_neighbours = pd.DataFrame(index=test_df.columns,columns=range(1,5))
nr = test_df.apply(lambda x:sorti(x))
elapsed = timeit.default_timer() - start_time
print(elapsed)