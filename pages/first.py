import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')

df1 = pd.read_csv('D:/resource/MISY225/my-streamlit/Final-data-app/archive/Terra.csv')
df2 = pd.read_csv('D:/resource/MISY225/my-streamlit/Final-data-app/archive/terrausd.csv')
df3 = pd.read_csv('D:/resource/MISY225/my-streamlit/Final-data-app/archive/terra-luna.csv')

#1:全部的luna币价格波动
from matplotlib.lines import lineStyles
from matplotlib.pyplot import title


st.subheader('The daily closing price of a luna coin from the date of issue to the crash')
fig,ax = plt.subplots()
df1.Close.plot(label = 'close price',linestyle='solid',color='blue')
ax.set_ylabel('Daily closing price($)')
ax.legend()
ax.set_title('daily closing price($) of crypto luna',fontsize=15,color='r')
st.pyplot(fig)


#2：5月份两张图
st.subheader('The daily price of luna and USD during the crash')

fig,ax = plt.subplots(2,1,figsize=[30,10])

df2.price.plot.bar(ax = ax[0],label='usd', linestyle = 'dashed',  color = 'blue')

df3.price.plot.bar(ax = ax[1],label='luna', linestyle = 'dashed',  color = 'blue')

ax[0].set_ylabel('Daily price($)')
ax[1].set_ylabel('Daily price($)')


ax[0].legend()
ax[1].legend()

ax[0].set_title(' ave daily price($) of USD',fontsize=15,color='r')
ax[1].set_title(' ave daily price($) of luna',fontsize=15,color='r')
st.pyplot(fig)

#3：存量图（在第三步里）




