import pandas as pd 
import numpy as np 

l = np.linspace(5.0, 2.0)
float_list = l.astype(float)
round_list = float_list.round(1)
unique_list = np.unique(round_list)
py_list = str(unique_list.tolist())
print('"%s"' % py_list )
quote_list = []
for iter in unique_list:
    quote_list.append("%s" % iter)
print(quote_list)