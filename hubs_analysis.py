import pandas as pd
import numpy as np
from pandas import DataFrame

def column_name(option,year,month):
    # the datasets chosen has a few problems with column names
    # this can be explained because some of the datasets used the ICAO default
    # but most of them used the Brazilian default
    # the difference is basically this: 'ICAO Aeródromo...' instead 'Aeroporto...'
    # but it doesn't follow any logical sequence and this function just return the right name
    # it sounds like weird, but this is the only way to garantee that every file will be analysed
    # the 'option' argument define if the return name will related with origin or destination
    
    if(option == 0):     # origin
        if(year < 2013):
            return 'Aeroporto Origem'
        else:
            if((year == 2013) and (month == 11)):
                return 'ICAO Aeródromo Origem'
            elif((year == 2014) and (month > 5) and (month < 8)):
                return 'ICAO Aeródromo Origem'
            elif((year == 2015) and (month > 7)):
                return 'ICAO Aeródromo Origem'
            elif((year == 2016) and (month < 4)):
                return 'ICAO Aeródromo Origem'
            elif((year == 2016) and ((month == 7) or (month > 10))):
                return 'ICAO Aeródromo Origem'
            elif(year > 2016):
                return 'ICAO Aeródromo Origem'
            else:
                return 'Aeroporto Origem'
    elif(option == 1):     # destination
        if(year < 2013):
            return 'Aeroporto Destino'
        else:
            if((year == 2013) and (month == 11)):
                return 'ICAO Aeródromo Destino'
            elif((year == 2014) and (month > 5) and (month < 8)):
                return 'ICAO Aeródromo Destino'
            elif((year == 2015) and (month > 7)):
                return 'ICAO Aeródromo Destino'
            elif((year == 2016) and (month < 4)):
                return 'ICAO Aeródromo Destino'
            elif((year == 2016) and ((month == 7) or (month > 10))):
                return 'ICAO Aeródromo Destino'
            elif(year > 2016):
                return 'ICAO Aeródromo Destino'
            else:
                return 'Aeroporto Destino'
    else:
        return -1       # wrong option
    

def create_airport_list(year):
    # this function will return the name of all airports contained into all datasets for a year
    # these names will be used for counting how many times each airport is shown 
    # and this number will define how many upcoming or outgoing flights each airport had
    
    # creating the two most important arrays for this step
    # they'll be used for create the address to each files be accessed
    # ----------------------------------
    # this step creates each one of the addresses necessary to access the csv files
    airports = {}   # the array where the list of airport will be saved
    datasets_folder = 'datasets'
    for j in range(1,13):       # use range(1,13)
        if(j>=10):
            months_divider = '/'
        else:
            months_divider = '/0'
        address = str(datasets_folder) + '/' + str(year) + months_divider + str(j) + '.csv'
   
        # the next step will opens each one of the csv files datasets
        # after, it'll find all the different values which were not saved yet
        # so the different values will be saved into an array

        # the next lines ask the right name of the airport columns
        # which depends directly of which year and month is analysing
        column_airport_from = column_name(0,year,j)
        column_airport_to = column_name(1,year,j)
        
        # this substep will open a file and get the unique values for departed from airports
        file = pd.read_csv(address, sep=';', encoding='iso-8859-15',engine='python',error_bad_lines=False)
        temp_airports = file[column_airport_from].unique()
        
        # this substep will check if the airport is already in the list
        # only if not, it'll be added
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
        print('Arquivo ' + address + ' lido')
    return airports
    

    # the last step will be create and write a csv file 
    # the array created in the last step will be used to create the new csv file
    

def create_dataset_airports():
    # this function makes analysis in all files 
    # the files must to be divided by year and it's needed one file per month
    # this function will count how many times the airports are shown
    # and it will create a new csv file with all the information
    # the new csv file has the format below:
    #   year; month; airport; incoming_flights; outgoing_flights
    
    