import json
import csv
import pandas as pd
import numpy as np 
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import random
import math


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
X = dummies2

# construct y from other variables 
y = data['win_ratio']

# TRAIN TEST SPLIT
def traintest_split(X, y, test_ratio):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
    return X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = traintest_split(X, y, 0.2)
print(X_train.columns)
print(y_train.head())

# GRADIENT BOOSTED REGRESSOR with cross validation
model = GradientBoostingRegressor(random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(mse)

# get initial 8 cards for monte carlo
def initial_8():
    indices = random.sample(range(101), k = 8)
    cards = all_cards[indices]
    return cards, indices

def monte_carlo(num_replacement, tau):
    eight_cards, indices = initial_8()
    y_prev = 0
    for i in range(num_replacement):
        # in eightcards, which card to omit
        index_toreplace = random.randint(0, 7)
        possible_index = [i for i in range(101) if i not in indices]
        new_index = random.sample(possible_index, k = 1)
        possible_cards = eight_cards.copy()
        possible_cards[index_toreplace] = all_cards[new_index]
        # dummy encode 8 cards 
        cols = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']
        df = pd.DataFrame(np.array(possible_cards), columns = cols)
        X_df = pd.get_dummies(df)
        y_pred = model.predict(X_df)
        e_A = math.exp(y_pred / tau)
        e_B = math.exp(y_prev / tau)
        prob_pred = e_A / (e_A + e_B)
        prob_prev = e_B / (e_A + e_B)
        if (y_pred > y_prev) or (prob_pred > prob_prev):
            indices[index_toreplace] = new_index
            eight_cards[index_toreplace] = all_cards[new_index]
        else: #keep old deck
        

        # if something:


# markov chain monte carlo algorithm (Metropolis) - make model with one of the x predictors or combination of them. Choose 8 cards at
# random, predit how good of a job you did. Randomly switch cards with something else. If it does better, accept
# If it does worse, accept with some probability based on difference of how good you were before - now. 
# If you did a little worse, accept. if you did a lot worse, reject. 
# Formula is e^constant * difference (original - new). The reason you may accept a slightly worse one 
# is you don't want to get stuck in a minimum. Start with usually accepting steps (based on difference), 
# gradually lower this (more likely to reject step later on - simulated annealing),
# graphs of how much it jumps up and down. Restart multiple times becuase of global search problem (starting deck matters)
# use trophies, bestTrophies, threwwcrown_ratio, and win_ratio

# ASK ANDREW - what formula to use for metropolis algorithm, how much to lower accepted difference by with time 


# If it does worse, randomly accept with some probability. 
# If win rate went from 20% to 10%, ratio is 1/2, so decide to keep this new card w probability (1/2)
# Try this and jacks
# Repeat this over and over
# Simulated annealing - less likely to accept worse data. 

# tau = 0.5, 0.4, 0.3, 0.2, 0.1

