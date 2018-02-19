from unittest import TestCase, main
from unittest.mock import patch
from blackjack.blackjack import get_winner


class TestMain(TestCase):
    @patch('builtins.print')
    def test_winner(self, mock_print):
        player = 'player'  # using a variable in case we extend the program to allow name entry
        dealer = 'dealer'
        # get_winner(player_score, house_score)
        self.assertEqual(get_winner(19, 23), player)  # dealer busts
        self.assertEqual(get_winner(10, 9), player)  # both have valid scores, player's favor
        self.assertEqual(get_winner(19, 21), dealer)  # dealer wins, valid scores both
        self.assertEqual(get_winner(23, 16), dealer)  # player busts
        self.assertEqual(get_winner(10, 10), dealer)  # tie, no one breaking


if __name__ == '__main__':
    main()
