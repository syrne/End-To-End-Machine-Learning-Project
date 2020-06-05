import os
import pandas as pd
import matplotlib.pyplot as plt

data_path = os.path.join(os.path.dirname(__file__), 'data/housing.csv')
data_df = pd.read_csv(data_path)

print(data_df.head())
print(data_df.describe())
print(data_path)
