import sys
import json
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player, RandomPlayer, HumanPlayer

# number of games to play
num_games = 500000

# create an empty dataset
dataset = []

# play games
for i in range(num_games):
    # create a new game with two players and a board
    game = Game(RandomPlayer(RandomPlayer.X), RandomPlayer(Player.O), Board())

    # play the game
    game.play(verbose=False)

    # if the game is a draw, skip it
    if game.board.winner == 0:
        continue

    # add the game to the dataset
    dataset.append(game.to_training_data(perspective_from_first_move=True))
    dataset.append(game.to_training_data(perspective_from_first_move=False))

# save the dataset to a json file
with open("dataset.json", "w") as f:
    f.write(json.dumps(dataset))

print("Successfully generated dataset with %d datapoints!" % len(dataset))