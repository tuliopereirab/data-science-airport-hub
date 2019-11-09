import pandas as pd
import numpy as np

def create_airport_list():
    # this function creates a csv file containing all the airports/aerodromes shown in the files
    # this new csv file will be used for further analysis and as base to count the occurrencies
    # the airports csv file format will be:
    #   airports;
    
    
    # creating the two most important arrays for this step
    # they'll be used for create the address to each files be accessed
    years = {}
    address = {}
    count = 0
    for i in range(2000,2020):
        years[count] = i
        count += 1
    # ----------------------------------
    # this step creates each one of the addresses necessary to access the csv files
    datasets_folder = 'datasets'
    count = 0
    for i in years:
        for j in range(4,7):       # use range(0,13)
            if(j>=10):
                months_divider = '/'
            else:
                months_divider = '/0'
            address[count] = str(datasets_folder) + '/' + str(years[i]) + months_divider + str(j) + '.csv'
            count += 1
    
    # the next step will opens each one of the csv files datasets
    # after, it'll find all the different values which were not saved yet
    # so the different values will be saved into an array
    
    airports = {}   # the array where the list of airport will be saved
    
    for i in address:
        if(i < 187):        # this is the number refering to the 'address' array position
                            # which has the last 'Aeroporto Origem' instead 'ICAO Aeródromo...'
            column_airport_from = 'Aeroporto Origem'
            column_airport_to = 'Aeroporto Destino'
        else:
            column_airport_from = 'ICAO Aeródromo Origem'
            column_airport_to = 'ICAO Aeródromo Destino'
               
        # this substep will open a file and get the unique values for departed from airports
        file = pd.read_csv(address[i], sep=';', encoding='iso-8859-15',engine='python')
        temp_airports = file[column_airport_from].unique()
        for j in temp_airports:
            exists = 0
            for z in airports:
                if(j == airports[z]):
                    exists = 1
                    
            if(exists == 0):    
                next_position = len(airports)
                airports[next_position] = j                
                print('Adicionou!')
            else:
                print('Existe')
        # this substep will open a file and get the unique values for destination airports
        temp_airports = file[column_airport_to].unique()
        for j in temp_airports:
            exists = 0
            for z in airports:
                if(j == airports[z]):
                    exists = 1
            if(exists == 0):    
                next_position = len(airports)
                airports[next_position] = j
                print('Adicionou!')
            else:
                print('Existe')
        #temp_airports.clear()   # clear the array
        print('Arquivo ' + address[i] + ' lido')
    print(airports)

    # the last step will be create and write a csv file 
    # the array created in the last step will be used to create the new csv file
    


def create_dataset_airports():
    # this function makes analysis in all files 
    # the files must to be divided by year and it's needed one file per month
    # this function will count how many times the airports are shown
    # and it will create a new csv file with all the information
    # the new csv file has the format below:
    #   year; month; airport; incoming_flights; outgoing_flights
     
    