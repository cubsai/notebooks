# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
max_temp = [30,31,32,28,27,29,26]
min_temp = [23,22,20,24,18,19,10]
avg_temp = [25,28,28,26,23,25,24]
wind = [50,100,40,65,80,75,50]
plt.scatter(days,wind)
plt.figure(figsize=(7,5))
plt.scatter(days,wind,color='red',alpha=0.6,s=[e^3 for e in wind])
plt.title('wind speed',fontsize=18,color='red')
plt.xlabel('Days of the week',fontsize=12,color='green')
plt.ylabel('wind speed',fontsize=12,color='green')
plt.ylim(30,120)
plt.grid()

plt.scatter(days,avg_temp)
plt.figure(figsize=(6,5))
plt.plot(days,avg_temp,color='g',linestyle='--',marker='*',linewidth=3,markersize=15)
plt.fill_between(days,avg_temp,color='y',alpha=0.3)
plt.ylim(20,30)
plt.title('Average temperature',fontsize=18,color='red')
plt.xlabel('Days of the week',fontsize=12,color='green')
plt.ylabel('Temperature',fontsize=12,color='green')

plt.plot(days,max_temp,label='max')
plt.plot(days,min_temp,label='min')
plt.plot(days,avg_temp,label='avg')

plt.title('Average Temperature',fontsize=18,color='red')
plt.xlabel('Days of the week',fontsize=12,color='green')
plt.ylabel('Temperature',fontsize=12,color='green')
plt.plot(days,max_temp,label='max')
plt.plot(days,min_temp,label='min')
plt.plot(days,avg_temp,label='avg')
plt.legend(loc='lower left',shadow=True,fontsize='large')
plt.axhline(24,color='red',linewidth=3)



# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
max_temp = [30,31,32,28,27,29,26]
min_temp = [23,22,20,24,18,19,10]
avg_temp = [25,28,28,26,23,25,24]
wind = [50,100,40,65,80,75,50]
plt.scatter(days,wind)
plt.figure(figsize=(7,5))
plt.scatter(days,wind,color='red',alpha=0.6,s=[e^3 for e in wind])
plt.title('wind speed',fontsize=18,color='red')
plt.xlabel('Days of the week',fontsize=12,color='green')
plt.ylabel('wind speed',fontsize=12,color='green')
plt.ylim(30,120)
plt.grid()

# %%
