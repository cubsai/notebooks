# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
df=pd.read_csv('Brain_Weight_dataset.csv')
df.shape
df.info()
df.isnull().sum()
df.duplicated().sum()
df.nunique()
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.3,random_state=0)

# %%
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

# %%
accuracy=model.score(x_test,y_test)
print("Model accuracy: {:.2f}".format(accuracy))

# %%
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

# %%
print("Training accuracy:")
print('RMSE is :{:.2f}'.format(rmse))
print('R2 score is :{:.2f}'.format(r2))

# %%
