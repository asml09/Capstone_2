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
decks.drop('Unnamed: 0', axis = 1, inplace=True)
data = pd.read_csv('data.csv')
data['tag'] = data['tag'].transform(lambda x: x[1:])
# data = decks.merge(dat, how = 'inner', on = 'tag')
data['win_ratio'] = data['wins'] / data['battleCount']
data.fillna(data.mean(axis = 1), inplace=True)

# get a list of all 102 cards
dummies = pd.get_dummies(decks[['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']])
cols = list(dummies.columns)
new_col = np.array([card[6:] for card in cols])
all_cards = np.unique(new_col)
dummy2 = pd.get_dummies(all_cards)

new_df = pd.DataFrame(np.zeros((decks.shape[0], 102)), columns = dummy2.columns)
print(new_df)

for i in range(decks.shape[0]):
    cards = decks.iloc[i, :].values.tolist()
    for col in all_cards: 
        if col in cards:
            new_df.loc[i][col] = 1

new_df = pd.concat([new_df, decks.iloc[:, 8]], axis = 1)

# end up w 145 rows
final_df = new_df.merge(data[['tag', 'win_ratio']], how = 'inner', on = 'tag')
print(final_df)


# PROBLEM - not each dummy variable will have all cards, if a card happened to not show up in slot 1 (only slot 2)
# SOLUTION - add list of cards to end of data frame , then delete these later 
# cards = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']
# arr = np.array([all_cards, all_cards, all_cards, all_cards, all_cards, all_cards, all_cards, all_cards])
# dummy_df = pd.DataFrame(arr.reshape(102, 8), 
#     columns = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8'])








# # print(dummy_df.head())
# # print(decks.iloc[:, :8].head())
# original_length = decks.shape[0]
# # decks = decks.concat(dummy_df, axis = 0)
# # temp_decks = pd.concat([decks.iloc[:, :8], dummy_df], axis = 1)

# temp_decks = decks.iloc[:, :8].append(dummy_df, ignore_index=True)
# # This will be X for machine learning

# dummies2 = pd.get_dummies(temp_decks)
# print(dummies2.shape)
# X = dummies2[:original_length]
# # print(X.head())

# # construct y from other variables 
# y = data['win_ratio']
# # print(data.shape)

# TRAIN TEST SPLIT
# def traintest_split(X, y, test_ratio):
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
#     return X_train, X_test, y_train, y_test
# X_train, X_test, y_train, y_test = traintest_split(X, y, 0.2)
# print(X_train.columns)
# print(y_train.head())

# # GRADIENT BOOSTED REGRESSOR with cross validation
# model = GradientBoostingRegressor(random_state=0)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print(mse)

# get initial 8 cards for monte carlo
# def initial_8():
#     indices = random.sample(range(101), k = 8)
#     cards = all_cards[indices]
#     return cards, indices

# # # num_replacement - how many times a card is replaced
# # # tau - temperature
# # keep track of all decks you get, keep track of how many times they appear. start w 1000, 
# # if it doesn't take forever Run > 1 million times
# # if decks are somewhat similar thats good too
# def monte_carlo(num_replacement, tau):
#     eight_cards, indices = initial_8()
#     cols = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']
#     df = pd.DataFrame(np.array(eight_cards), columns = cols)
#     X_df = pd.get_dummies(df)
#     y_prev = model.predict(X_df)
#     # 1 million timesish. 
#     for i in range(num_replacement):
#         # in eightcards, which card to omit
#         index_toreplace = random.randint(0, 7)
#         possible_index = [i for i in range(101) if i not in indices]
#         new_index = random.sample(possible_index, k = 1)
#         possible_cards = eight_cards.copy()
#         possible_cards[index_toreplace] = all_cards[new_index]
#         # dummy encode 8 cards 
#         # won't have card 1 -8 anymore, will have (1 row x 102 columns)
#         cols = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']
#         df = pd.DataFrame(np.array(possible_cards), columns = cols)
#         X_df = pd.get_dummies(df)
#         y_pred = model.predict(X_df)
#         e_A = math.exp(y_pred / tau)
#         e_B = math.exp(y_prev / tau)
#         ratio = e_A / e_B
#         prob_pred = e_A / (e_A + e_B)
#         prob_prev = e_B / (e_A + e_B)
#         # difference in probabilities of pred / prev. Accept this with probability c * (ratio) by generating a random
#         # number between 0 and 1. Adjust constant c, should be pretty small << 1
#         # lowering of tau- much less likely to accept worse option
#         # if random.rand is < ratio of those two
#         # ratio prob_pred / prob_prev
#         # andrew available anytime other than 11 - 1
#         if (y_pred > y_prev) or (prob_pred > prob_prev):
#             indices[index_toreplace] = new_index
#             eight_cards[index_toreplace] = all_cards[new_index]
#     return eight_cards
        

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

# tau = 0.5, 0.4, 0.3, 0.2, 0.1, decreases w time



