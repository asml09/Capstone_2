import json
import csv
import pandas as pd
import numpy as np 
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
# from sklearn.model_selection import kFold
import matplotlib.pyplot as plt


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
def traintest_split(data, test_ratio):
    X = data.drop('win_ratio', axis = 1)
    y = data['win_ratio']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
    return X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = traintest_split(data, 0.2)
print(X_train.columns)
print(y_train.head())

learning_rate = [.01, .02, .04, .05, .1, .2]
n_estimators = [100, 200, 400, 500, 700]
dic = {}
# number of estimators 
# GRADIENT BOOSTED REGRESSOR with cross validation
for rate in learning_rate:
    for estimator in n_estimators:
        model = GradientBoostingRegressor(random_state=0, learning_rate = rate, n_estimators = estimator)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        dic[rate, estimator] = mse
print(mse)

fig, ax = plt.subplots(2, 3, figsize = (20, 8), constrained_layout = True)
for i in range(3):
    y = []
    for item in n_estimators:
        y.append(dic[learning_rate[i], item])
    ax[0, i].plot(n_estimators, y)
    ax[0, i].set_xticks(n_estimators)
    ax[0, i].legend(['mse with learning rate ' + str(learning_rate[i])])
    plt.xticks(fontsize = 7)
    plt.legend(prop = {'size' : 7})
for i in range(3):
    y = []
    for item in n_estimators:
        y.append(dic[learning_rate[i+3], item])
    ax[1, i].plot(n_estimators, y)
    ax[1, i].set_xticks(n_estimators)
    ax[1, i].legend(['mse with learning rate ' + str(learning_rate[i+3])])
    plt.xticks(fontsize = 7)
    plt.legend(prop = {'size' : 7})

plt.xlabel('# estimators', fontsize = 7)
plt.ylabel('mse', fontsize =7)
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.tight_layout()
plt.show()
plt.savefig('img3.png')

# VISUALS


# y = data[['trophies', 'bestTrophies', 'battleCount', 'challengeCardsWon']]



# ROC curve?


# MACHINE LEARN
# What's the best deck? What's the best card? 


