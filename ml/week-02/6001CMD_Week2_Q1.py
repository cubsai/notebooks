# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
cols=['population','profit']
df=pd.read_csv('Rest_Pop_Profit.csv',names=cols)
df.head()
print(df.head())
print("Dataset shape:")
df.shape
print("Dataset info:")
df.info()
print("Checking for any null values:")
df.isnull().any()
print("Checking for unique values in each column:")
df.nunique()
x=df.iloc[:,0:1].values
y=df.iloc[:,1].values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.25,random_state=0)

# %%
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
y_train_pred=model.predict(x_train)
y_test_pred=model.predict(x_test)
from sklearn.metrics import mean_squared_error, r2_score
rmse=np.sqrt(mean_squared_error(y_train,y_train_pred))
r2=r2_score(y_train,y_train_pred)

# %%
print("Training accuracy:")
print('RMSE is :{:.2f}'.format(rmse))
print('R2 score is :{:.2f}'.format(r2))

# %%
rmse=np.sqrt(mean_squared_error(y_test,y_test_pred))
r2=r2_score(y_test,y_test_pred)
print("Testing accuracy:")
print('RMSE is :{:.2f}'.format(rmse))
print('R2 score is :{:.2f}'.format(r2))

accuracy=model.score(x_test,y_test)
print("Model accuracy: {:.2f}".format(accuracy))

# %%
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
max_temp = [30,31,32,28,27,29,26]
min_temp = [23,22,20,24,18,19,10]
avg_temp = [25,28,28,26,23,25,24]
wind = [50,100,40,65,80,75,50]
plt.scatter(days,wind)
plt.scatter(days,avg_temp)

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
cols=['population','profit']
df=pd.read_csv('Rest_Pop_Profit.csv',names=cols)
df.head()

# %%
print("Dataset shape:")
df.shape

# %%
print("Dataset info:")
df.info()

# %%
print("Checking for any null values:")
df.isnull().any()

# %%
print("Checking for unique values in each column:")
df.nunique()
x=df.iloc[:,0:1].values

# %%
y=df.iloc[:,1].values

# %%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.25,random_state=0)

# %%
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
y_train_pred=model.predict(x_train)
y_test_pred=model.predict(x_test)

# %%
from sklearn.metrics import mean_squared_error, r2_score
rmse=np.sqrt(mean_squared_error(y_train,y_train_pred))
r2=r2_score(y_train,y_train_pred)

# %%
print("Training accuracy:")
print('RMSE is :{:.2f}'.format(rmse))
print('R2 score is :{:.2f}'.format(r2))

# %%
rmse=np.sqrt(mean_squared_error(y_test,y_test_pred))
r2=r2_score(y_test,y_test_pred)
print("Testing accuracy:")
print('RMSE is :{:.2f}'.format(rmse))
print('R2 score is :{:.2f}'.format(r2))

accuracy=model.score(x_test,y_test)
print("Model accuracy: {:.2f}".format(accuracy))

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
cols=['population','profit']
df=pd.read_csv('Rest_Pop_Profit.csv',names=cols)
df.head()
print(df.head())
print("Dataset shape:")
df.shape

# %%
print("Dataset info:")
df.info()


# %%
print("Checking for any null values:")
df.isnull().any()
print("Checking for unique values in each column:")
df.nunique()


# %%
x=df.iloc[:,0:1].values
y=df.iloc[:,1].values

# %%
print(x,y)

# %%
