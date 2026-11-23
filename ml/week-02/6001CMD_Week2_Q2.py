# %%
import pandas as pd
import numpy as np
cols=['Area','Num_Beds','Price']
df=pd.read_csv('House_Price_Data.csv',names= cols)
df.info  
x=df.iloc[1:, :-1].values
y=df.iloc[1:, -1].values
print(x)
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('Training score is :{:.3f}'.format(train_score))
print('Test score is :{:.3f}'.format(test_score))

# %%
import pandas as pd
import numpy as np
cols=['Area','Num_Beds','Price']
df=pd.read_csv('House_Price_Data.csv',names= cols)
df.info  
x=df.iloc[1:, :-1].values
y=df.iloc[1:, -1].values
print(x)
print(y)

# %%

# %%
