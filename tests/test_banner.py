from unittest import TestCase, main
from unittest.mock import patch
from blackjack.blackjack import banner
import logging
logging.basicConfig(level=logging.DEBUG, filename='blackjack.log')
logger = logging.getLogger('grateguy')  # video game reference, character from Super Mario RPG


class TestMain(TestCase):

    # want to make sure our banner is done as one object passed to print,
    # not just calling print a superfluous number of times
    @patch('builtins.print')
    def test_mock_print_count(self, mock_print):
        banner()
        self.assertEqual(1, mock_print.call_count)

    # while an auto passing test would normally be bad, this is more so during testing one can examine
    # the stylistic aspects of banner
    @patch('builtins.print')
    def test_get_banner(self, mock_print):
        banner()
        logger.debug(str(mock_print.call_args_list))
        pass


if __name__ == '__main__':
    main()
