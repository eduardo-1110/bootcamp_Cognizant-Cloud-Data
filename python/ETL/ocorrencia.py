from msilib import schema
from os import sep
import pandas as pd
import pandera as pa
from pyparsing import col

df = pd.read_csv('ocorrencia.csv', sep = ';',parse_dates=['ocorrencia_dia'],dayfirst=True)
#print(df)
#print(df.dtypes

