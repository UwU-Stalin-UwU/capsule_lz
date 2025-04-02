#UwU-Stalin-UwU
#Playstation players file of lab

import matplotlib.pyplot as plt
import pandas as pd

class Sonyboys():
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country
    
    def diagramm(self):
        labels = self.country
        plt.pie(sizes, labels = labels)
        plt.axis('equal')
        plt.show()

def main():
    df=pd.DataFrame()
    df=pd.read_csv('playstation_players.csv')
    df.columns = ['player_id', 'player_name', 'player_country']


if __name__=="__main__":
    main()