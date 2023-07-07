

from RPS_game import play, tima, mercy, dara, tim, human, random_player
from RPS import player
from unittest import main
import test_module

play(player, dara, 1000)
play(player, mercy, 1000)
play(player, tim, 1000)
play(player, tima, 1000)

# Play interactively against a bot:
play(human, mercy, 20, verbose=True)

# Play against a bot that plays randomly:
play(human, random_player, 1000)

# Run unit tests automatically:
main(module='test_module', exit=False)
