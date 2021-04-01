import json
import csv
import pandas as pd
import numpy as np 
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import kFold

# READ + MERGE CSV. Get dummy variables
decks = pd.read_csv('decks.csv')
dat = pd.read_csv('data.csv')
dat['tag'] = dat['tag'].transform(lambda x: x[1:])
data = decks.merge(dat, how = 'inner', on = 'tag')
data['win_ratio'] = data['wins'] / data['battleCount']
data['threecrown_ratio'] = data['threeCrownWins'] / data['battleCount']
data.drop(['Unnamed: 0_x', 'Unnamed: 0_y', 'wins', 'losses', 'threeCrownWins', 'tag'], axis = 1, inplace=True)
data.fillna(data.mean(axis = 1), inplace=True)

dummies = pd.get_dummies(data[['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8', 'role']])
data = pd.concat([data, dummies], axis = 1)
data.drop(['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8', 'role'], axis = 1, inplace=True)

# print(np.any(np.isnan(data)))
# print(data.isnull().sum())
# data.to_csv('test.csv')

# DATA VISUALIZATION


# TRAIN TEST SPLIT
# def traintest_split(data, test_ratio):
#     X = data.drop('win_ratio', axis = 1)
#     y = data['win_ratio']
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
#     return X_train, X_test, y_train, y_test
# X_train, X_test, y_train, y_test = traintest_split(data, 0.2)
# print(X_train.columns)
# print(y_train.head())

# # GRADIENT BOOSTED REGRESSOR with cross validation
# model = GradientBoostingRegressor(random_state=0)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print(mse)

# separate models, one for each y


y = data[['trophies', 'bestTrophies', 'battleCount', 'challengeCardsWon']]



# ROC curve?


# MACHINE LEARN
# What's the best deck? What's the best card? 


