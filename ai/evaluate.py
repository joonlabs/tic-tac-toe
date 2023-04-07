from tictactoe.player import RandomPlayer, AIPlayer, Player
from tictactoe.board import Board
from tictactoe.game import Game
from tqdm import tqdm

# create players
random_player = RandomPlayer(Player.O)
ai_player = AIPlayer(Player.X, "models/model.h5")

# run a number of random games against the AI and count the number of wins
number_of_games = 1000
ai_wins = 0
ai_lost = 0
ai_draw = 0
for i in tqdm(range(number_of_games)):
    game = Game(ai_player, random_player, Board())
    # game = Game(random_player, ai_player, Board())
    game.play(verbose=False)

    if game.board.winner == ai_player.name:
        ai_wins += 1
    elif game.board.winner == 0:
        ai_draw += 1
    elif game.board.winner == random_player.name:
        ai_lost += 1
        print(game.board)
        print(game.board.move_history)


# print the percentage of wins
print("AI won %d games" % ai_wins)
print("That is %d%%" % (ai_wins / number_of_games * 100), "\n")

print("AI lost %d games" % ai_lost)
print("That is %d%%" % (ai_lost / number_of_games * 100), "\n")

print("Draws: %d games" % ai_draw)
print("That is %d%%" % (ai_draw / number_of_games * 100), "\n")
