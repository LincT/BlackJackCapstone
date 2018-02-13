from unittest import TestCase,main
from blackjack.blackjack import get_suite


class TestMain(TestCase):

    def test_getSuite(self):
        suites = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        suit = get_suite()
        self.assertIn(suit, suites)


if __name__ == '__main__':
    main
