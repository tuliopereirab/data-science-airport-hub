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
plt.suptitle("SBGL (azul) e SBGR (vermelho)",fontsize=16, y=1)
plt.xlabel('Meses')
plt.ylabel('Voos/anos')
plt.savefig('graphs/graf_flight_by_month_SBGR-SBGL_RED-BLUE.png')
# -----------------------------
# creating the same graph for comparison between SBSP and SBRJ
y_sbsp = sbsp.incoming
x_sbsp = sbsp.month
x_sbrj = sbrj.month
y_sbrj = sbrj.incoming


plt.plot(x_sbrj,y_sbrj,color='blue')
plt.plot(x_sbsp,y_sbsp,color='red')
plt.xlabel('Meses')
plt.ylabel('Voos/anos')
plt.suptitle("SBRJ (azul) e SBSP (vermelho)",fontsize=16, y=1)
plt.savefig('graphs/graf_lines_SBRJ-SBSP_months.png')
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

all_airports = all_files[all_files.incoming > 3000]
sns.lmplot('year','incoming',all_airports,height=5.2,aspect=2)

# ------------------------------------------
# GRAPHICS FOR THE HOLE YEAR
# the objective here is to show the increasement of the flight numbers in the year
# the datasets are from 2000 until 2018
# it will be considered only incoming flights for the calculations

## GRÁFICO IMPORTANTE
flights = pd.DataFrame(columns=['year','total_flights'])
for i in range(2000,2019):
    address = 'datasets/flight_numbers/year/' + str(i) + '.csv'
    data = pd.read_csv(address, sep=',')
    flight_sum = data['incoming'].sum()
    flights = flights.append(pd.Series([str(i), str(flight_sum)], index=flights.columns), ignore_index=True)

plt.plot( 'year', 'total_flights', data=flights, marker='o', color='mediumvioletred')
plt.savefig('graphs/graf_total_flights_year.png')
## ##################################################################################################################

# flights by brazilian region

flights = pd.DataFrame(columns=['year','sbeg','sbbr','sbgr','sbpa','sbsv','sbcy'])
for i in range(2000,2019):
    address = 'datasets/flight_numbers/year/' + str(i) + '.csv'
    data = pd.read_csv(address, sep=',')
    airport_sbeg = data[data.airport == 'SBEG'] # manaus
    flight_sum_sbeg = airport_sbeg['incoming'].sum()
    print(str(i) + ": MANAUS : " + str(flight_sum_sbeg))
    #
    airport_sbbr = data[data.airport == 'SBBR'] # brasilia 
    flight_sum_sbbr = airport_sbbr['incoming'].sum()
    print(str(i) + ": BRASILIA : " + str(flight_sum_sbbr))
    #
    airport_sbgr = data[data.airport == 'SBGR'] # guarulhos
    flight_sum_sbgr = airport_sbgr['incoming'].sum()
    print(str(i) + ": GUARULHOS : " + str(flight_sum_sbgr))    
    #
    airport_sbpa = data[data.airport == 'SBPA'] # porto alegre
    flight_sum_sbpa = airport_sbpa['incoming'].sum()
    print(str(i) + ": PORTO ALEGRE : " + str(flight_sum_sbpa))
    #
    airport_sbsv = data[data.airport == 'SBSV'] # salvador
    flight_sum_sbsv = airport_sbsv['incoming'].sum()
    print(str(i) + ": SALVADOR : " + str(flight_sum_sbsv))
    #
    airport_sbcy = data[data.airport == 'SBCY'] # cuiabá 
    flight_sum_sbcy = airport_sbcy['incoming'].sum()
    print(str(i) + ": CUIABA : " + str(flight_sum_sbcy))
    print("------------------------")
    flights = flights.append(pd.Series([str(i), flight_sum_sbeg, flight_sum_sbbr, flight_sum_sbgr, flight_sum_sbpa, flight_sum_sbsv,flight_sum_sbcy], index=flights.columns), ignore_index=True)
   
# total flights by airport from 2000 until 2018
flights_airport = pd.DataFrame(columns=['airport','total_flights'])
total_flights_sbeg = flights['sbeg'].sum()
print("SBEG: " + str(total_flights_sbeg))
flights_airport = flights_airport.append(pd.Series(["SBEG", total_flights_sbeg], index=flights_airport.columns), ignore_index=True)
#
total_flights_sbbr = flights['sbbr'].sum()
print("SBBR: " + str(total_flights_sbbr))
flights_airport = flights_airport.append(pd.Series(["SBBR", total_flights_sbbr], index=flights_airport.columns), ignore_index=True)
#
total_flights_sbgr = flights['sbgr'].sum()
print("SBGR: " + str(total_flights_sbgr))
flights_airport = flights_airport.append(pd.Series(["SBGR", total_flights_sbgr], index=flights_airport.columns), ignore_index=True)
#
total_flights_sbpa = flights['sbpa'].sum()
print("SBPA: " + str(total_flights_sbpa))
flights_airport = flights_airport.append(pd.Series(["SBPA", total_flights_sbpa], index=flights_airport.columns), ignore_index=True)
#
total_flights_sbsv = flights['sbsv'].sum()
print("SBSV: " + str(total_flights_sbsv))
flights_airport = flights_airport.append(pd.Series(["SBSV", total_flights_sbsv], index=flights_airport.columns), ignore_index=True)
#
total_flights_sbcy = flights['sbcy'].sum()
print("SBCY: " + str(total_flights_sbsv))
flights_airport = flights_airport.append(pd.Series(["SBCY", total_flights_sbcy], index=flights_airport.columns), ignore_index=True)



x_sbeg = "SBEG"
y_sbeg = flights.sbeg
x_sbbr = "SBBR"
y_sbbr = flights.sbbr
x_sbgr = "SBGR"
y_sbgr = flights.sbgr
x_sbpa = "SBPA"
y_sbpa = flights.sbpa
x_sbsv = "SBSV"
y_sbsv = flights.sbsv
x_sbcy = "SBCY"
y_sbcy = flights.sbcy

plt.scatter(x_sbeg,y_sbeg,color='blue')
plt.scatter(x_sbbr,y_sbbr,color='orange')
plt.scatter(x_sbgr,y_sbgr,color='green')
plt.scatter(x_sbpa,y_sbpa,color='red')
plt.scatter(x_sbsv,y_sbsv,color='pink')
plt.scatter(x_sbcy,y_sbcy,color='yellow')
plt.xlabel('Aeroportos')
plt.ylabel('Total de voos')

plt.plot('airport', 'total_flights', data=flights_airport, marker='o', color='mediumvioletred')
plt.savefig('graphs/graf_by_region.png')


# ###################################################################################################################

sns.lmplot('year','total_flights', flights)



flight_numbers = flights.total_flights
flight_numbers.hist(normed = 1 , histtype = 'step', cumulative = True ,
      linewidth = 3.5 , bins = 20, color = sns.desaturate("indianred" , .75))