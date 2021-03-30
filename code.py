# import requests
# url = "https://proxy.royaleapi.dev/v1/clans/%239PJ82CRC"
# payload = {}
# headers = {
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImYwY2QyOTI0LTExYjMtNGNhYi1iNDlkLTljM2IxMjdiYWNmMyIsImlhdCI6MTYxNjcyMzU1Mywic3ViIjoiZGV2ZWxvcGVyL2VkMDA0OTgxLThlNDMtZmMwNS03YTZjLWNlN2M3MWM3MDE2ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3My45Ny4zNy4xNjQiLCIxMjguMTI4LjEyOC4xMjgiXSwidHlwZSI6ImNsaWVudCJ9XX0.BUB_F_iDUcxNsngIMjcxmsTJU6kogEKqLyNEkDYkyj3WXTlYNoTlk6SDoAywGZjpsjPvmMaB5tIHw-c2grf-9A',
# }
# response = requests.request("GET", url, headers=headers, data = payload)
# print(response.text.encode('utf8'))
import json
import csv
import pandas as pd

import requests
url = "https://proxy.royaleapi.dev/v1/cards"
# payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjgxNWUwNjFlLWMzY2ItNDg2ZC05Mzc0LTRhNTU2NDNlNTk1MCIsImlhdCI6MTYxNzA0OTc3MCwic3ViIjoiZGV2ZWxvcGVyL2NiYzhkNGIyLWU1ZTAtZGVlYi1iMjE3LWQxY2MzNWNkNzlhOSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3My41My40NS4xMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.wzWI-yKyobkt7KGYx_yOIdwj2lslCzVWvapPMgDVPmkiRfhKioMpGPdUudw1gVPI1dyiNtDENFfgtEWDWJvAyA',
}
# response = requests.get('https://api.clashroyale.com/v1/players/%232JRLG8PUQ', headers=headers)
# player1 = b'{"tag":"#2JRLG8PUQ","name":"RemiEli","expLevel":13,"trophies":7909,"bestTrophies":8503,"wins":25105,"losses":19762,"battleCount":50743,"threeCrownWins":3665,"challengeCardsWon":62333,"challengeMaxWins":20,"tournamentCardsWon":31305,"tournamentBattleCount":7135,"role":"leader","donations":0,"donationsReceived":0,"totalDonations":169198,"warDayWins":136,"clanCardsCollected":249861,"clan":{"tag":"#Q98GV2C0","name":"YT : RemiEli CR","badgeId":16000010},"arena":{"id":54000031,"name":"Ultimate Champion"},"leagueStatistics":{"currentSeason":{"rank":1,"trophies":7909,"bestTrophies":7909},"previousSeason":{"id":"2021-02","rank":43,"trophies":8170,"bestTrophies":8367},"bestSeason":{"id":"2020-07","rank":4,"trophies":7939}},"badges":[{"name":"Classic12Wins","level":2,"maxLevel":3,"progress":18,"target":100},{"name":"Grand12Wins","level":2,"maxLevel":3,"progress":13,"target":100},{"name":"Crl20Wins","progress":20},{"name":"1000Wins","progress":25105},{"name":"Played1Year","progress":1459},{"name":"Played2Years","progress":1459},{"name":"Played3Years","progress":1459},{"name":"LadderTournamentTop1000_1","progress":45},{"name":"LadderTournamentTop1000_2","progress":29},{"name":"LadderTournamentTop1000_3","progress":35},{"name":"LadderTop1000_1","progress":11},{"name":"LadderTop1000_2","progress":9},{"name":"LadderTop1000_3","progress":4},{"name":"TopLeague","progress":8503},{"name":"ClanWarWins","level":3,"maxLevel":3,"progress":136},{"name":"Crl20Wins2019","progress":20}],"achievements":[{"name":"Team Player","stars":3,"value":4263,"target":1,"info":"Join a Clan","completionInfo":null},{"name":"Friend in Need","stars":3,"value":169198,"target":2500,"info":"Donate 2500 cards","completionInfo":null},{"name":"Road to Glory","stars":3,"value":22,"target":6,"info":"Reach Arena 6","completionInfo":null},{"name":"Gatherer","stars":3,"value":102,"target":40,"info":"Collect 40 cards","completionInfo":null},{"name":"TV Royale","stars":3,"value":1,"target":1,"info":"Watch a TV Royale Replay","completionInfo":null},{"name":"Tournament Rewards","stars":2,"value":31305,"target":500000,"info":"Win 500000 cards from tournaments","completionInfo":null},{"name":"Tournament Host","stars":1,"value":1,"target":10,"info":"Create and finish 10 tournaments","completionInfo":null},{"name":"Tournament Player","stars":3,"value":1455,"target":1,"info":"Join a tournament","completionInfo":null},{"name":"Challenge Streak","stars":3,"value":20,"target":12,"info":"Get 12 wins in a single Challenge","completionInfo":null},{"name":"Practice with Friends","stars":3,"value":5387,"target":10,"info":"Win 10 Friendly Battles","completionInfo":null},{"name":"Special Challenge","stars":3,"value":301,"target":5,"info":"Participate in 5 unique Special Event Challenges","completionInfo":null},{"name":"Friend in Need II","stars":3,"value":169198,"target":25000,"info":"Donate 25000 cards","completionInfo":null}],"cards":[{"name":"Inferno Tower","id":27000003,"level":11,"starLevel":2,"maxLevel":11,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/GSHY_wrooMMLET6bG_WJB8redtwx66c4i80ipi4gYOM.png"}},{"name":"Fisherman","id":26000061,"level":4,"maxLevel":5,"count":9,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/U2KZ3g0wyufcuA5P2Xrn3Z3lr1WiJmc5S0IWOZHgizQ.png"}},{"name":"Firecracker","id":26000064,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/c1rL3LO1U2D9-TkeFfAC18gP3AO8ztSwrcHMZplwL2Q.png"}},{"name":"Ram Rider","id":26000051,"level":5,"maxLevel":5,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/QaJyerT7f7oMyZ3Fv1glKymtLSvx7YUXisAulxl7zRI.png"}},{"name":"P.E.K.K.A","id":26000004,"level":8,"maxLevel":8,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/MlArURKhn_zWAZY-Xj1qIRKLVKquarG25BXDjUQajNs.png"}},{"name":"Clone","id":28000013,"level":6,"maxLevel":8,"count":300,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/mHVCet-1TkwWq-pxVIU2ZWY9_2z7Z7wtP25ArEUsP_g.png"}},{"name":"Barbarian Barrel","id":28000015,"level":8,"maxLevel":8,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/Gb0G1yNy0i5cIGUHin8uoFWxqntNtRPhY_jeMXg7HnA.png"}},{"name":"Three Musketeers","id":26000028,"level":9,"maxLevel":11,"count":1800,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/_J2GhbkX3vswaFk1wG-dopwiHyNc_YiPhwroiKF3Mek.png"}},{"name":"Bats","id":26000049,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/EnIcvO21hxiNpoI-zO6MDjLmzwPbq8Z4JPo2OKoVUjU.png"}},{"name":"Dark Prince","id":26000027,"level":8,"maxLevel":8,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/M7fXlrKXHu2IvpSGpk36kXVstslbR08Bbxcy0jQcln8.png"}},{"name":"Fire Spirits","id":26000031,"level":11,"maxLevel":13,"count":7000,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/16-BqusVvynIgYI8_Jci3LDC-r8AI_xaIYLgXqtlmS8.png"}},{"name":"Graveyard","id":28000010,"level":4,"maxLevel":5,"count":6,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/Icp8BIyyfBTj1ncCJS7mb82SY7TPV-MAE-J2L2R48DI.png"}},{"name":"Sparky","id":26000033,"level":3,"maxLevel":5,"count":9,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/2GKMkBrArZXgQxf2ygFjDs4VvGYPbx8F6Lj_68iVhIM.png"}},{"name":"Mortar","id":27000002,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/lPOSw6H7YOHq2miSCrf7ZDL3ANjhJdPPDYOTujdNrVE.png"}},{"name":"Bandit","id":26000046,"level":5,"maxLevel":5,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/QWDdXMKJNpv0go-HYaWQWP6p8uIOHjqn-zX7G0p3DyM.png"}},{"name":"Giant","id":26000003,"level":10,"maxLevel":11,"count":1000,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/Axr4ox5_b7edmLsoHxBX3vmgijAIibuF6RImTbqLlXE.png"}},{"name":"Furnace","id":27000010,"level":10,"maxLevel":11,"count":1000,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/iqbDiG7yYRIzvCPXdt9zPb3IvMt7F7Gi4wIPnh2x4aI.png"}},{"name":"Goblin Hut","id":27000001,"level":9,"maxLevel":11,"count":1800,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/l8ZdzzNLcwB4u7ihGgxNFQOjCT_njFuAhZr7D6PRF7E.png"}},{"name":"Bowler","id":26000034,"level":7,"maxLevel":8,"count":200,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/SU4qFXmbQXWjvASxVI6z9IJuTYolx4A0MKK90sTIE88.png"}},{"name":"Knight","id":26000000,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/jAj1Q5rclXxU9kVImGqSJxa4wEMfEhvwNQ_4jiGUuqg.png"}},{"name":"Lava Hound","id":26000029,"level":3,"maxLevel":5,"count":11,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/unicRQ975sBY2oLtfgZbAI56ZvaWz7azj-vXTLxc0r8.png"}},{"name":"Barbarian Hut","id":27000005,"level":11,"maxLevel":11,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/ho0nOG2y3Ch86elHHcocQs8Fv_QNe0cFJ2CijsxABZA.png"}},{"name":"Prince","id":26000016,"level":7,"maxLevel":8,"count":200,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/3JntJV62aY0G1Qh6LIs-ek-0ayeYFY3VItpG7cb9I60.png"}},{"name":"Battle Healer","id":26000068,"level":11,"maxLevel":11,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/KdwXcoigS2Kg-cgA7BJJIANbUJG6SNgjetRQ-MegZ08.png"}},{"name":"Royal Ghost","id":26000050,"level":4,"maxLevel":5,"count":5,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/3En2cz0ISQAaMTHY3hj3rTveFN2kJYq-H4VxvdJNvCM.png"}},{"name":"Wizard","id":26000017,"level":9,"maxLevel":11,"count":1800,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/Mej7vnv4H_3p_8qPs_N6_GKahy6HDr7pU7i9eTHS84U.png"}},{"name":"Rage","id":28000002,"level":6,"maxLevel":8,"count":233,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/bGP21OOmcpHMJ5ZA79bHVV2D-NzPtDkvBskCNJb7pg0.png"}},{"name":"Zap","id":28000008,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/7dxh2-yCBy1x44GrBaL29vjqnEEeJXHEAlsi5g6D1eY.png"}},{"name":"Mega Minion","id":26000039,"level":11,"maxLevel":11,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/-T_e4YLbuhPBKbYnBwQfXgynNpp5eOIN_0RracYwL9c.png"}},{"name":"Ice Spirit","id":26000030,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/lv1budiafU9XmSdrDkk0NYyqASAFYyZ06CPysXKZXlA.png"}},{"name":"Elite Barbarians","id":26000043,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png"}},{"name":"Poison","id":28000009,"level":8,"maxLevel":8,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/98HDkG2189yOULcVG9jz2QbJKtfuhH21DIrIjkOjxI8.png"}},{"name":"Minion Horde","id":26000022,"level":13,"starLevel":3,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/Wyjq5l0IXHTkX9Rmpap6HaH08MvjbxFp1xBO9a47YSI.png"}},{"name":"Spear Goblins","id":26000019,"level":13,"maxLevel":13,"count":0,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/FSDFotjaXidI4ku_WFpVCTWS1hKGnFh1sxX0lxM43_E.png"}},{"name":"Lightning","id":28000007,"level":7,"maxLevel":8,"count":200,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/fpnESbYqe5GyZmaVVYe-SEu7tE0Kxh_HZyVigzvLjks.png"}},{"name":"Witch","id":26000007,"level":7,"maxLevel":8,"count":200,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/cfwk1vzehVyHC-uloEIH6NOI0hOdofCutR5PyhIgO6w.png"}},{"name":"Goblin Giant","id":26000060,"level":7,"maxLevel":8,"count":200,"iconUrls":{"medium":"https://api-assets.clashroyale.com/cards/300/SoW16cY3jXBwaTDvb39DkqiVsoFVaDWbzf5QBYphJrY.png"}},{"name":"Freeze","id":28000005,"level

# # player tags of top player of all time 
# player_all_time = ['#PCUY9VL', '#R8J9GU8L', '#220U2GV', '#2CLV2RP0', '#8GQ8RY0GL', '#28VCYVRUJ', '#9JUJLQPL', '#28RCC0PG2',
#  '#929URQCL8', '#2LJ0ULYCC', '#228RR0GR', '#R09228V', '#9YPCUGQU', '#2RLP2P82P', '#28V9Q0', '#L8C0CCU', '#LPRR9P', '#2LJJ2U2QV',
#  '#2RC89GJ', '#8QQ8QJ99P', '#8L9YQRVQ', '#829QUCLRU', '#R0LR9RUQ', '#YCUQ2CUP', '#PC2PP2RP', '#U9V0VC9L', '#9LGVVV0J0', '#2GURUGVC',
#  '#LGLL8LLC', '#2PUVCRRV8', '#Y2LP0CU', '#PUP9PRGU9', '#2PJJRLR2C', '#92GVPRVL', '#G0CYJ00J', '#PCG229PC', '#88CQUJVQP', '#GVGGGPJP', 
#  '#G90RYCVQ', '#82VRLJCGR', '#YYGPQU8', '#8PGQJ8UVP', '#Q2JRCLGJ', '#P9PJUUPGY', '#8PYRVGYCL', '#QVPJRV', '#2Y90QPGLY', '#8LYVUY29', 
#  '#8QRCJQ9Y', '#9QUQGV8V', '#22Q2928GJ', '#P92LGYGU', '#8GPQUPGYP', '#Q9L902JJ', '#20RY9JJRL', '#290QP2C', '#J89JRRU', '#Y9R22RQ2', '#Y0Y9VL8U',
#  '#828JPJQU8', '#892Y20JLY', '#2J0UYGQ9R', '#2P020JY99', '#980RC809', '#2PVQJY809', '#9RLQLC208', '#PPUVRRR9', '#8CGG9LLJU', '#GVG8GCC', '#YGPU280R', 
#  '#2UJU8GRG', '#2JRLG8PUQ', '#2VQ9PRQ9Y', '#9G8Q00JVG', '#20YGVQR0R', '#8LJVG0L28', '#GUPYJ2', '#V2JGRQYJ', '#2CU8J88YV', '#QULJR90C', '#P8VUY20C', 
#  '#YQRGLLC0', '#G80UUU', '#CC0CLGUC', '#YUJY8JQU', '#88RUCCQLC', '#YR8VGYPQ', '#YRVL9U98', '#2QGYJ90G', '#RP0PGQ9V', '#8J2QU0CP', '#PY929QJ2', '#UL0JU92V', 
#  '#VUYRULP', '#22RVJGC8V', '#GGV9YLQY', '#2UVV829PR', '#CYY90CQC', '#U200V9P', '#8GG0RRUJ']

# response = requests.get('https://api.clashroyale.com/v1/cards?limit=2', headers=headers)
# print(response.text.encode('utf8'))

response = requests.get('https://api.clashroyale.com/v1/players/%23U200V9P', headers=headers)
#print(response.text)
# print(dict(response.text['tag']))
dic = json.loads(response.text)
a = dic['currentDeck']
for card in a:
  del card['iconUrls']
  dat = pd.DataFrame(card, index=[0])
  print(dat)

# dat = pd.DataFrame.from_dict(dic)
# print(dat)
# dic = {'name': 'Rocket', 'id': 28000003, 'level': 11, 'starLevel': 3, 'maxLevel': 11, 'count': 0}
# print(pd.DataFrame(dic, index = [0]))
#print(response.text.encode('utf8'))
# response.text.encode('utf8')


# data = {var: value.decode("utf-8") for var, value in response.text.encode('utf8') if not var.startswith('_')}
# makes it a python dicitonary, then a pandas df 


# print(json.loads(response.text)['tag'])
# convert to dictionary then to pandas csv 
# save data as a csv file 
#json.dump(dat, 'json_data.json')


ordinary_players = [#GG829JGY, #29YU089C, #2PYCGV2RR,
#YCVYYPQC,
#PC9PYY0Q,
#YUC8CQJG,
#2G9GLP,
#YUC8CQJG,
#YLLY9GVL9,
#QQQPQJ0,
#Q8QQCUR9,
#8PU8G0QG0,
#YUC8CQJG,
#99VRJL2R,
#GGJPL0,
#9PG88R2L,
#JJQJU02,
#L9JQ8229,
#U200Q0VP,
#YLGVVR8L,
#G9CL0JCC,
#PP29QQU9,
#99YCUP8L,
#UYQJQVQ,
#VG0YCG9Y,
#2900CCR2,
#YPU0GJUV,
#J08J0QQJ,
#2R0P2Y2,
#9QQVJJC8C,
#Y8PUL0R8,
#2LPCG89Y8,
#Y2Y8VC0P,
#2GG90PRCY,
#VJ89QGL,
#20VQP0RCG,
#20VJRG8PG,
#PCGPLPCQ,
#RYV8CQCU,
 #8LJJQ8JV,
#PUR822RRG,
#PP2VGGGJ,
#PPRP8QP8Q,
#PGJGLQPL,
#8UP0PJ0Y,
#J0YJ2U,
#YLYV8QY,
#8098L0G8Y,
#LGQQRL2,
#RL9YGQ8Q,
#PL20VR9PV,
#GLQ0VLG,
#QGYRJ89UJ,
#LP8R202L,
#PLG8UJPLY,
#2VCQ0RLR,
#200PQRG,
#88Y0J0G0L,
#PPYVR0RR,
#8L2C8CU0C,
#YQLLGPQJ,
#9890L2LC,
#Y28C9CQG,
#8URV9P9Y,
#YV22GRY,
#2Q2UVGU08,
#PU0CR9J8,
#2GCRY9LQU,
#PU0R0GQQ,
#9C0YULLJR,
#2QY0UPGR9,
#LV9VYJY9R,
#8LU2092LP,
#2C89UUV,
#YLQJLR8U,
#V8GYQPUR,
#LGUL0U88,
#LQJ0Y02,
#8CQY22GJ,
#PPJL0JYG,
#9U89PQG8,
#22PYPQ9CJ,
#29QLRPP8P,
#8VY2YQYQ0,
#9QCGCQG8,
#CYCYPRCJ,
#GGRC9GYC,
#Y0RCRVC0,
#8P9YY0RVJ,
#8YGY8VVVR,
#9VL8YU9J,
#2RC2Q0RCY,
#LJCY90JU,
#8R0Y2PU9,
 #YYGQUUJ,

#82C0L2GCC,
#2P2G82UVU,
#G90Y0Q,
#8UU0998U,
#PRQJQPGUP,
#2LVPQU,
 #28VPRJPR,
#9JJJY2J28,
#YQYPPRGQ,
#QVYQP0UG,
 #YP0GYR,
#LC2V29GCC,
  #YC0RVJ9L,
#LU0GLCGCV,
  #Y0VYPY9V,
#2VQL,
#L8PL9V,
#800YRCRQ0,
 #888P8P8G,
#2UY22LYVP,
#2RVRGL0U,
#89P2L2UQ,
#9VLLQGJY,
#YCVYL8JRP,
#2G9YR2GRL,
#P9090G09,
#YUCQVVLJR,
#8GV89GYJ,
#88JJY9,
#8CPV22RY,
#2R9LVQUJ,
#J9L0PJV,
#PLL9RPV8,
#Q00GLLC2J,
#PG9JCPJ,
#2LGL28GPY,
#RQPUUY,
#90J22GCQC,
#9PP0GQ2L,
#2R0Y2299G,
#9RVJJYLV,
#2YCJQ2PL,
#CULQ928,
#8L88U8RP,
#GV9CCQ,
#2CLR28QG9,
#QYCGVJYR,
#R09PJRJQ,
 #PRQJGRGJ,
#2QRR0RLQC,
#8LUR0C0Y,
#JGJUGGUU,
#2P22RPUGL,
#2C2G20YGU,
 #820G8Q,
#29GP0GQ00,
 #PCYQPQLR,
#92LYL92G,
#8PP2098C,
#LUJJ9U,
#9GJY0UY0,
#2LYP9URVY,
#90L2CJVP,
#2LPPGLQR0,
#YGY2YGGV,
#PGJUPUJY,
 #9U8URVCL,
#92L8920C,
#LQVYLLV 
]