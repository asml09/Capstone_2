import json
import csv
import pandas as pd
import numpy as np 
import matplotlib
from sklearn.model_selection import train_test_split

# READ + MERGE CSV 
decks = pd.read_csv('decks.csv')
dat = pd.read_csv('data.csv')
dat['tag'] = dat['tag'].transform(lambda x: x[1:])
data = decks.merge(dat, how = 'inner', on = 'tag')
data['win_ratio'] = data['wins'] / data['battleCount']
data['threecrown_ratio'] = data['threeCrownWins'] / data['battleCount']
data.drop(['Unnamed: 0_x', 'Unnamed: 0_y', 'wins', 'losses', 'threeCrownWins', 'tag'], axis = 1, inplace=True)


# DATA VISUALIZATION


# TRAIN TEST SPLIT
def traintest_split(data, test_ratio):
    X = data.drop('win_ratio', axis = 1)
    y = data['win_ratio']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
    return X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = traintest_split(data, 0.2)
print(X_train.columns)
print(y_train.head())






# MACHINE LEARN
# What's the best deck? What's the best card? 


