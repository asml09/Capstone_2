# Clash Royale 
In Clash Royale, a player builds a deck before they enter the game. There are 102 cards to choose from, and a player picks 8 of these to use. A player is more likely to win if they are of a high skill level and if the deck they choose is a good one. It is the assumption in the games community that certain cards on their own are not necessarily better than other cards, but combinations of cards are better than other combinations of cards. On youtube, there are many videos claiming that a given deck is the best. As an example, some cards have the advantage of being able to take a lot of hits before they die, but other cards have the advantage of being able to shoot and hit the opponents cards from a long range. A deck consisting of only cards being able to take a lot of hits, or only cards that can shoot from a long range would be a bad deck. The first regression model will, given a player and their deck, predict their win rate. The second regression model will predict the percentage a certain deck will win (regardless of player). 

# The data
Data was collected from a clash royale api and then stored in csv format. Each player is identified by a player tag. I collected the player tags of the top 100 players in the world, and 160 ordinary players. After I stored it in the csv, I read it into two dataframes. 

Dataframe 1 
<img src = "https://github.com/asml09/Capstone_2/blob/master/images/img1.png" > 

Dataframe 2
<img src = "https://github.com/asml09/Capstone_2/blob/master/images/im2.png" width="800" height="300" >

# The game 

![example game play](https://j.gifs.com/P72nYn.gif)

# Gradient Boosted Regressor 

Predicts whether a player will win with a given deck. Predictors are the players deck, level, trophies, best trophies, win rate, and three crown win rate. Response is win rate
The hyperparameters learning rate and number of estimators were explored.                                
learning_rate = [.01, .02, .04, .05, .1, .2]                                                             
n_estimators = [100, 200, 400, 500, 700]                                                                 
Using a learning rate of 0.1 and 700 estimators resulted in the lowest mse = .00425

<img src = "https://github.com/asml09/Capstone_2/blob/master/images/img3.png" >

# Monte Carlo with gradient boosted regressor

Predicts whether a given deck will win. Predictors for gradient model are the deck, response is win rate. 

Pseudocode:                                                                                              
  randomly generate a deck of 8 cards from the 102 cards available.   
  use gradient model to predict win rate of deck                                                          
  randomly choose one of the cards in the deck to exchange, and replace it with some other random card   
  if this new deck has a higher predicted win rate, keep it as the new deck                               
  if it doesn't, still accept it with some probability. This probability decreases as the number of       iterations increases
  
  <img src = "https://github.com/asml09/Capstone_2/blob/master/images/img6.png" width = "400" height = "450" >
  
 With 100,000 iterations, the best deck found was :

<img src = "https://github.com/asml09/Capstone_2/blob/master/images/img7.png" width = "500" height = "350" >
  
  
  
