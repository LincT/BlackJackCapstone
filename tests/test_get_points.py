from unittest import TestCase, main
from blackjack.blackjack import points


class TestMain(TestCase):
    def test_points(self):
        # hands are lists containing A,J,Q,K, and 2-10
        hand = ['A']
        print(hand)
        self.assertEqual(points(hand), 11)
        self.assertEqual(points(['A', 'A']), 12)
        self.assertEqual(points(['A', 'A', 'A']), 13)
        self.assertEqual(points(['A', '1']), 21)
        self.assertEqual(points(['A', 'J']), 21)
        self.assertEqual(points(['A', 'K']), 21)
        self.assertEqual(points(['A', 'Q']), 21)
        self.assertEqual(points([]), 0)
        self.assertEqual(points(['chips', 'pizza']), 0)
        self.assertEqual(points(['1']), 10)
        self.assertEqual(points(['10']), 10)

if __name__ == '__main__':
    main
