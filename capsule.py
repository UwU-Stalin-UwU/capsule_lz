#UwU-Stalin-UwU
#Capsule file of lab

from datetime import datetime
import os
import pandas as pd


def logging(func):                                               #Decorator
    def wrapper(*args, **kwargs):
        usr_func = func
        org = func(*args, **kwargs)
        usr_func_name = str(usr_func.__name__)
        usr_name = os.getlogin()
        time_act = str(datetime.now().time())
        day_act =  str(datetime.now().date())
        logs = 'logs.csv'
        if os.path.isfile(logs):                                                                                          #If csv file exists
            file_df = pd.read_csv(logs)
            data = {'': [len(file_df)], 'User': [usr_name], 'Func': [usr_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv('logs.csv',header=False, index=False, mode='a')
        else:                                                                                                             #If csv file doesn't exist
            data = {'User': [usr_name], 'Func': [usr_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv('logs.csv')
        return org
    return wrapper

@logging
def hello():                                                                                                              #Test func
    print('hello')

def main():
    #for i in range(200):
        #pr()
    hello()

if __name__ == "__main__":
    main()