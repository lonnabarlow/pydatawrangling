import pandas as pd
import numpy as np


df = pd.read_csv('historical_RAPTOR_by_player.csv') 
type(df)

len(df)
print(len(df))


def get_info(df):
    print(df.describe())
    print(df["raptor_total"].mean())
    

get_info(df)
 
df.columns 
print(df.columns) 

df.columns.values.tolist()
print(df.columns.values.tolist())

columns_list = list(df)
print(columns_list)

df.dtypes
print(df.dtypes)

list(df.select_dtypes(['int64']).columns) 
print(list(df.select_dtypes(['int64']).columns))

df.apply(lambda x: x.duplicated().any(), axis='rows')
print(df.apply(lambda x: x.duplicated().any(), axis='rows'))

def abc_name(df):
    df.sort_values("player_name")
    print(df.sort_values("player_name"))

abc_name(df)   

def end_name(df):
    df.sort_values(by="player_name",ascending=False)
    print(df.sort_values(by="player_name",ascending=False))

end_name(df)    


df.groupby("player_name").aggregate(["min", "max"])
print(df.groupby("player_name").aggregate(["min", "max"]))

