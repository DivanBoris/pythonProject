import pandas as pd
import os
import datetime as DT
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

os.chdir("C:\\Users\\79291\\PycharmProjects\\pythonProject\\Heave-and-Roll-artifacts-correction")
Files = os.listdir()

for File in Files:
    print(f'Start {File}{str(DT.datetime.now().strftime("%H:%M:%S"))}')
    df = pd.read_csv(File,header= None, sep=' ')
    df.columns = [Nb]