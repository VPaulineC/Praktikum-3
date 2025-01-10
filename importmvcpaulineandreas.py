import pandas as pd
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def import_dataPauline(separator):
    """ This function is when you put together several datasets,
    but each dataset always starts with a time of 0.
    Input: dataframe that also has a column 't'
    Output: continuous time over all datasets
   """
    def time_norm(data):
        a = list(data.iloc[:]['t'])
        b = list(data.iloc[:]['t'])
        
        for u in range(len(a)-1):
            if a[u]>a[u+1]:
                if b[u]>b[u+1]:
                    offset = a[u]-a[u+1]+1
                    a[u+1] = offset + a[u+1]
                    u += 1
                else:
                    a[u+1] = offset + a[u+1]
                    u += 1
                      
        output = pd.DataFrame({'emg': data.emg, 't': a})
        output.reset_index(inplace = True, drop = True)
        return output
    
    """import data and put weights in one variable and mvc in one variable"""
    column_names = [
      'emg',
      't',  
    ]
    # Creating an empty Dataframe with column names only
    
    mvc_raw = pd.DataFrame(columns=column_names)
    
    # read all mvc, weight, and fatigue files 
    for i in range(3):
        # create string for path
        mvc_string = 'MVCPauline' + str(i+1) + '.txt'
        
    
        mvc_raw = pd.concat([mvc_raw, pd.read_csv(
            mvc_string,
             sep=separator, names=column_names, skiprows= 50, 
             skipfooter = 50,
             engine='python'
            )], ignore_index=True)

    # timing needs changing as, the appended data starts from 0 again

    mvcp = time_norm(mvc_raw)
    return  mvcp

def import_dataAndreas(separator):
    """ This function is when you put together several datasets,
    but each dataset always starts with a time of 0.
    Input: dataframe that also has a column 't'
    Output: continuous time over all datasets
   """
    def time_norm(data):
        a = list(data.iloc[:]['t'])
        b = list(data.iloc[:]['t'])
        
        for u in range(len(a)-1):
            if a[u]>a[u+1]:
                if b[u]>b[u+1]:
                    offset = a[u]-a[u+1]+1
                    a[u+1] = offset + a[u+1]
                    u += 1
                else:
                    a[u+1] = offset + a[u+1]
                    u += 1
                      
        output = pd.DataFrame({'emg': data.emg, 't': a})
        output.reset_index(inplace = True, drop = True)
        return output
    
    """import data and put weights in one variable and mvc in one variable"""
    column_names = [
      'emg',
      't',  
    ]
    # Creating an empty Dataframe with column names only
    
    mvc_raw = pd.DataFrame(columns=column_names)
    
    # read all mvc, weight, and fatigue files 
    for i in range(3):
        # create string for path
        mvc_string = 'MVCAndreas' + str(i+1) + '.txt'
        
    
        mvc_raw = pd.concat([mvc_raw, pd.read_csv(
            mvc_string,
             sep=separator, names=column_names, skiprows= 50, 
             skipfooter = 50,
             engine='python'
            )], ignore_index=True)

    # timing needs changing as, the appended data starts from 0 again

    mvca = time_norm(mvc_raw)
    return  mvca
