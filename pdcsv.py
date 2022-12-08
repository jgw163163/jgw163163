#合并币安历史数据到一个表
import pandas as pd
import numpy as np
import glob,os
#path = r'C:\venv\data\futures\um\monthly\klines\ETHUSDT\1mo\2020-01-01_2021-12-01'
file = glob.glob(r'C:\venv\data\futures\um\csv\*.csv', recursive=True)
dl = []
for f in file:
    ds=pd.read_csv(f,header=None)
    ds['filename']=os.path.splitext(os.path.split(f)[-1])[0]
    ds.to_csv(r"C:\Users\wugaojie\PycharmProjects\ftx\venv\data\futures\um\Students.csv",mode='a',header=False)
