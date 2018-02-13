from unittest import TestCase, main
from blackjack.blackjack import get_winner


class TestMain(TestCase):

    def test_winner(self):
        playPts = 19
        housePts = 23
        player = 'player'
        dealer = 'dealer'
        # get_winner(player_score, house_score)
        self.assertEqual(get_winner(19, 23), player)
        self.assertEqual(get_winner(15, 16), dealer)


if __name__ == '__main__':
    main
