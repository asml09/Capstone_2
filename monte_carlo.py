import json
import csv
import pandas as pd
import numpy as np 
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import random


decks = pd.read_csv('decks.csv')
dat = pd.read_csv('data.csv')
dat['tag'] = dat['tag'].transform(lambda x: x[1:])
data = decks.merge(dat, how = 'inner', on = 'tag')
data['win_ratio'] = data['wins'] / data['battleCount']
data['threecrown_ratio'] = data['threeCrownWins'] / data['battleCount']
data.drop(['Unnamed: 0_x', 'Unnamed: 0_y', 'wins', 'losses', 'threeCrownWins', 'tag'], axis = 1, inplace=True)
data.fillna(data.mean(axis = 1), inplace=True)

dummies = pd.get_dummies(data[['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']])
# cards = dummies.iloc[0, 0:102]
# data = pd.concat([data, dummies], axis = 1)
# data.drop(['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8', 'role'], axis = 1, inplace=True)


cols = list(dummies.columns)
new_col = np.array([card[6:] for card in cols])
# 101 cards
all_cards = np.unique(new_col)

# get initial 8 cards for monte carlo
def initial_8():
    indices = random.sample(range(101), k = 8)
    cards = all_cards[indices]
    return cards
# print(initial_8())

# takes in first 8 cards and puts them in the same format as dummy variables, it stands for y_test
# def construct_ytest(first8)
# print(len(dummies.columns))

# PROBLEM - not each dummy variable will have all cards, if a card happened to not show up in slot 1 (only slot 2)
# SOLUTION - add list of cards to end of data frame , then delete these later 
cards = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']
arr = np.array([all_cards, all_cards, all_cards, all_cards, all_cards, all_cards, all_cards, all_cards])
arr = arr.reshape(-1, 8)
dummy_df = pd.DataFrame(arr, 
    columns = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8'])
decks = decks.append(dummy_df)

# This will be X for machine learning
dummies2 = pd.get_dummies(decks[['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']])

# construct y from other variables 




