# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
numberOfStudents = [1400,600,300,410,250]
courseNames = ['CS','Games','COMP','EH','ITB']
fig=plt.figure(figsize=(10,7))
plt.pie(numberOfStudents,labels=courseNames)
plt.show()

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
courseNames = ['CS','Games','COMP','EH','ITB']
numberOfStudents  = [1400,600,300,410,250]
#creating explode data
explode=(0.0,0.1,0.0,0.0,0.0)
#Creating color parameters
colors=("orange","cyan","brown","indigo","beige")

#Wedge properties"
wp={'linewidth':1,'edgecolor':"green"}

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.2f}%".format(pct, absolute)

# Creating plot
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(numberOfStudents,
                                  autopct=lambda pct: func(pct, numberOfStudents),
                                  explode=explode,
                                  labels=courseNames,
                                  shadow=True,
                                  colors=colors,
                                  startangle=90,
                                  wedgeprops=wp,
                                  textprops=dict(color="magenta"))   

#Adding legend
ax.legend(wedges,courseNames,
          title="courseNames",
          loc="center left",
          bbox_to_anchor=(1,0,0.5,1))
plt.setp(autotexts,size=8,weight="bold")
ax.set_title("Customizing pie chart")

#show plot
plt.show()

# %%
