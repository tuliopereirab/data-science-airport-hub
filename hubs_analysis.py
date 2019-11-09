# this whole Python script is used only when it's necessary to create new csv files with the number of flights 
# this code makes analysis in each one of the csv files and generate new csv files containing the analysis
# the analysis check each one of the year folders and generate the new csv file based on the year analysed
# for each year, there is a csv file 
# for the next steps, it will be used only the csv generated from this process 
# none of the original datasets will be used for further analysis

import pandas as pd
import numpy as np
from pandas import DataFrame

def address_create(year,month):
    # this function creates an address to access an specific file based on year and month
    datasets_folder = 'datasets'
    if(month>=10):
        months_divider = '/'
    else:
        months_divider = '/0'
    address = str(datasets_folder) + '/' + str(year) + months_divider + str(month) + '.csv'
    return address

def get_encoding_code(year,month):
    # this function is used to get the right encoding for the specific file
    # some of the files has different enconding, so it is necessary
    if(year == 2014):
        if((month == 6) or (month == 7)):
            return 'utf-8'
        else:
            return 'iso-8859-15'
    elif((year == 2017) and (month == 9)):
        return 'utf-8'
    else:
        return 'iso-8859-15'

def get_engine_definition(encoding):
    # when a csv file with utf-8 encoding is being read, it is necessary change the engine
    # the engine used for utf-8 encoding file reading is C and for all the others is python
    if(encoding == 'utf-8'):
        return 'c'
    else:
        return 'python'
    
    
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
    # and this number will define how many incoming or outgoing flights each airport had
    
    # creating the two most important arrays for this step
    # they'll be used for create the address to each files be accessed
    # ----------------------------------
    # this step creates each one of the addresses necessary to access the csv files
    airports = {}   # the array where the list of airport will be saved
    for j in range(1,13):       # use range(1,13)
        address = address_create(year,j)    # gets the address for the year-month file
        # the next step will opens each one of the csv files datasets
        # after, it'll find all the different values which were not saved yet
        # so the different values will be saved into an array

        # the next lines ask the right name of the airport columns
        # which depends directly of which year and month is analysing
        column_airport_from = column_name(0,year,j)
        column_airport_to = column_name(1,year,j)
        
        encoding_code = get_encoding_code(year,j)
        engine_def = get_engine_definition(encoding_code)
        
        # this substep will open a file and get the unique values for departed from airports
        file = pd.read_csv(address, sep=';', encoding=encoding_code,engine=engine_def,error_bad_lines=False)
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

# print(create_airport_list(2018))        # test the function above

def create_dataset_airports(year):
    # this function makes analysis in files each year
    # the files must to be divided by year and it's needed one file per month
    # this function will count how many times the airports are shown
    # the list of airports in each year will come from the function above
    # and a new csv file will be created with all the information
    # the new csv file has the format below:
    #   year; month; airport; incoming_flights; outgoing_flights
    airport_list = create_airport_list(year)
    df = pd.DataFrame(columns=['year','month','airport','incoming','outgoing'])
    for j in range(1,13):
        address = address_create(year,j)    # gets the address for the specific month based on the year
        
        encoding_code = get_encoding_code(year,j)
        engine_def = get_engine_definition(encoding_code)
        
        file = pd.read_csv(address, sep=';', encoding=encoding_code,engine=engine_def,error_bad_lines=False)
        
        column_airport_from = column_name(0,year,j)
        column_airport_to = column_name(1,year,j)
        
        for i in airport_list:  
            temp_incoming_flights = file[file[column_airport_to] == airport_list[i]].shape[0]
            temp_outgoing_flights = file[file[column_airport_from] == airport_list[i]].shape[0]
            print(str(address) + '\t' + str(airport_list[i]) + ': ' + str(temp_incoming_flights) + '\t'  + str(temp_outgoing_flights)) #shows file, airport and the number of outgoing flights
            	
            df = df.append(pd.Series([str(year), str(j), str(airport_list[i]), str(temp_incoming_flights), str(temp_outgoing_flights)], index=df.columns), ignore_index=True)
            
    address_output_file = 'datasets/' + 'flight_numbers/' + str(year) + '.csv'
    output_file = df.to_csv (address_output_file, index = None, header=True)
    
    
# --------------------------------------------
    # this peace of code makes analysis in all csv file from all year folders
    # the output of this are new csv files with number of flights from/to each airport found
for x in range(2000,2019):
    create_dataset_airports(x)
# --------------------------------------------
    
# print(pd.read_csv('datasets/2017/12.csv', sep=';', encoding='iso-8859-15',engine='python',error_bad_lines=False)) 
    