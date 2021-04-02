# import json
# import csv
# import pandas as pd
# import requests
# headers = {
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjgxNWUwNjFlLWMzY2ItNDg2ZC05Mzc0LTRhNTU2NDNlNTk1MCIsImlhdCI6MTYxNzA0OTc3MCwic3ViIjoiZGV2ZWxvcGVyL2NiYzhkNGIyLWU1ZTAtZGVlYi1iMjE3LWQxY2MzNWNkNzlhOSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3My41My40NS4xMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.wzWI-yKyobkt7KGYx_yOIdwj2lslCzVWvapPMgDVPmkiRfhKioMpGPdUudw1gVPI1dyiNtDENFfgtEWDWJvAyA',
# }
# tags = ['PCUY9VL', 'R8J9GU8L', '220U2GV']

# response3 = requests.get('https://api.clashroyale.com/v1/players/%23R8J9GU8L', headers=headers)
# dic = json.loads(response3.text)
# def get_Series(response):
#   dic = json.loads(response.text)
#   if 'currentDeck' not in dic.keys():
#     pass
#   else:
#     a = dic['currentDeck']
#     dat = pd.DataFrame()
#     for i, card in enumerate(a):
#       del card['iconUrls']
#       if i == 0:
#         dat = pd.DataFrame(card, index = [0])
#       else:
#         dat = dat.merge(pd.DataFrame(card, index=[i]), how='outer')
#     ser = pd.Series(dat['name'])
#     ser.index = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8']
#     return ser

# df = pd.DataFrame()
# series = []
# for player in tags:
#   url = 'https://api.clashroyale.com/v1/players/%23' + player
#   response = requests.get(url, headers=headers)
#   ser = get_Series(response)
#   if isinstance(ser, pd.Series):
#     ser = ser.append(pd.Series([player], index = ['tag']))
#     series.append(ser)
# print(series)

# df = pd.concat(series, axis = 1).transpose()
# df.index = list(range(len(series)))
# print(df)

import random
for i in range(50):
  print(random.randint(0, 7))

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




def monte_carlo(num_replacement, tau_list):
    eight_cards, indices = initial_8()
    X_df = make_dummies(eight_cards)
    y_prev = model.predict(X_df) 
    tau = tau_list[0]
    j = 1
    for i in range(num_replacement):
        if i in (20000, 40000, 60000, 80000):
          tau = tau_list[j]
          j += 1
        # in eightcards, which card to omit
        index_toreplace = random.randint(0, 7)
        possible_index = [i for i in range(101) if i not in indices]
        new_index = random.sample(possible_index, k = 1)[0]
        possible_cards = eight_cards.copy()
        possible_cards[index_toreplace] = all_cards[new_index]
        X_df = make_dummies(possible_cards)
        y_pred = model.predict(X_df)
        ratio = y_prev / y_pred 
        # the case where y_pred is worse than y_prev, accept with some probability 
        if ratio > 1:
            rand = random.uniform(0, 1)
            adjusted_ratio = ratio * tau
            if rand <= adjusted_ratio:
                eight_cards = possible_cards 
                y_prev = y_pred
        else:
            eight_cards = possible_cards
            y_prev = y_pred
    return eight_cards
eight_cards = monte_carlo(100000, [0.4, 0.3, 0.2, 0.1, 0.05])