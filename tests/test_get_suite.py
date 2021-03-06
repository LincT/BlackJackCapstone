from unittest import TestCase,main
from blackjack.blackjack import get_suite


class TestMain(TestCase):
    # probably not a needed test with current structure, but
    # if we ever expand cards to be objects instead of just ascii text, this might be handy
    def test_getSuite(self):
        suites = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        suites.sort()
        tested = []
        while suites != tested:
            suit = get_suite()
            if suit not in tested:
                tested.append(suit)
                tested.sort()
            self.assertIn(suit, suites)
        print("Tested: " + str(tested))


if __name__ == '__main__':
    main
