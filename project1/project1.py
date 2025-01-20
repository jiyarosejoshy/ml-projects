import pandas as p
import matplotlib.pyplot as mat
import seaborn as sea

data = p.read_excel("HousePricePrediction.xlsx")

print(data.head(5))

obj = (data.dtypes == 'object')
obj_cols = list(obj[obj].index)
obj_var = len(obj_cols)
print("no of object variables: ",obj_var)

int_ = (data.dtypes == 'int64')
int_cols = list(int_[int_].index)
int_var = len(int_cols)
print("no of integer variables: ",int_var)

fl = (data.dtypes == 'float')
fl_cols = list(fl[fl].index)
fl_var = len(fl_cols)
print("no of float variables: ",fl_var)