from time import time
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

# regresion
import seaborn as sns

# -------------------------------------------------------------------------

for i in range(2000,2019):
    address = "datasets/flight_numbers/year/" + str(i) + ".csv"
    data = pd.read_csv(address, sep=',')
    if(i == 2000):
        print(1)
        all_files = data
    else:
        print(i)
        all_files = all_files.append(data)

# separate in data frames with a specific airport
sbgr = all_files[all_files.airport == 'SBGR']
sbgl = all_files[all_files.airport == 'SBGL']
sbsp = all_files[all_files.airport == 'SBSP']
sbrj = all_files[all_files.airport == 'SBRJ']
# ----------------------------
# creating a graph for comparison between SBGR e SBGL
y_sbgr = sbgr.incoming
x_sbgr = sbgr.month
x_sbgl = sbgl.month
y_sbgl = sbgl.incoming


plt.scatter(x_sbgl,y_sbgl,color='blue')
plt.scatter(x_sbgr,y_sbgr,color='red')
plt.xlabel('Months')
plt.ylabel('Flights')

# -----------------------------
# creating the same graph for comparison between SBSP and SBRJ
y_sbsp = sbsp.incoming
x_sbsp = sbsp.month
x_sbrj = sbrj.month
y_sbrj = sbrj.incoming


plt.plot(x_sbrj,y_sbrj,color='blue')
plt.plot(x_sbsp,y_sbsp,color='red')
plt.xlabel('Months')
plt.ylabel('Flights')

# ----------------------------------

# creating graphs by year for two different airports


sbgr = pd.DataFrame(columns=['year','incoming','outgoing'])
for i in range(2000,2019):
    address = "datasets/flight_numbers/year/" + str(i) + ".csv"
    data = pd.read_csv(address, sep=',')
    
    temp_sbgr = data[data.airport == 'SBGR']        # save only SBGR numbers
    temp_sum_sbgr_incoming = temp_sbgr['incoming'].sum()
    temp_sum_sbgr_outgoing = temp_sbgr['outgoing'].sum()
    sbgr = sbgr.append(pd.Series([str(i), str(temp_sum_sbgr_incoming), str(temp_sum_sbgr_outgoing)], index=sbgr.columns), ignore_index=True)
print(sbgr)

sbgl = pd.DataFrame(columns=['year','incoming','outgoing'])
for i in range(2000,2019):
    address = "datasets/flight_numbers/year/" + str(i) + ".csv"
    data = pd.read_csv(address, sep=',')
    
    temp_sbgl = data[data.airport == 'SBGL']        # save only SBGR numbers
    temp_sum_sbgl_incoming = temp_sbgl['incoming'].sum()
    temp_sum_sbgl_outgoing = temp_sbgl['outgoing'].sum()
    sbgl = sbgl.append(pd.Series([str(i), str(temp_sum_sbgl_incoming), str(temp_sum_sbgl_outgoing)], index=sbgl.columns), ignore_index=True)
print(sbgl)


x_sbgr = sbgr.year
y_sbgr = sbgr.incoming
x_sbgl = sbgl.year
y_sbgl = sbgl.incoming

plt.plot(x_sbgl,y_sbgl,color='pink')
plt.plot(x_sbgr,y_sbgr,color='orange')
plt.xlabel('Year')
plt.ylabel('Incoming flights')

# ------------------------------------------

# clustering
sbgr_clust = all_files[all_files.airport == 'SBGR']
sns.lmplot("year", "incoming", sbgr_clust,height = 5.2, aspect = 2)

sbgl_cluts = all_files[all_files.airport == 'SBGL'];
sns.lmplot('year','incoming', sbgl_cluts, height=5.2, aspect = 2)