# A blackjack program, Player versus dealer.
# only setup for 2 players as traditionally
# blackjack is between player and dealer.

import random
# hands as global variables since they need
# to be stored reliably and addressed by multiple
# functions
playerHand = []
dealerHand = []


def main():
    print('\tWelcome to the table.\nYour hand will '
          'be displayed for you in an abbreviated '
          'form as you play,\nSuits are  '
          'represented as such: (C)lubs, '
          '(S)pades (H)earts, (D)iamonds\n'
          'Try to get as close as you can to 21 '
          'without going over.\n')
    playerHand.clear()
    dealerHand.clear()
    # calls to draw 2 cards for each player
    i = 0
    while i < 2:
        player()
        dealer()
        i += 1

    choice = " "
    while choice.lower()[0] != 's':
        choice = str(input('Hit or stay?\n'))
        print(str(playerHand) + '\nTotal: ' +
              str(points(playerHand)))

        if choice.lower()[0] == 'h':
            player()
            dealer()
        # elif choice.lower() == 's':
        #     print(str(playerHand) + '\n' +
        #           str(points(playerHand)) +
        #           ' points in total.')
        #     get_verdict()
        else:
            # print(str(playerHand) + '\n' +
            #       str(points(playerHand)) +
            #       ' points in total.')
            get_verdict()


def get_suite():
    val = random.randint(1, 4)

    if val == 1:
        word = 'Clubs'
    elif val == 2:
        word = 'Spades'
    elif val == 3:
        word = 'Hearts'
    else:
        word = 'Diamonds'
    return word


def get_card():
    val = random.randint(0, 12)
    words = ['Ace', '2', '3', '4', '5',
             '6', '7', '8', '9',
             '10', 'Jack', 'Queen', 'King']
    return words[val]


def points(hand):
    total = 0
    aces = False
    valid = 'AKQJ1098765432'
    for card in hand:
        if card[0] in valid:

            # first 5 cases deal with
            # invalid int literals
            if card[0] == 'A':
                # special handling as aces are
                # soft 11's
                total += 11
                aces = True

            elif card[0] == '1':
                # only place a 1 appears is as
                # first character of '10'
                total += 10
            elif card[0] == 'J':
                total += 10
            elif card[0] == 'Q':
                total += 10
            elif card[0] == 'K':
                total += 10
            # anything 2-10 can become an int
            elif 2 <= int(card[0]) <= 10:
                total += int(card[0])
        else:
            total += 0

        if total > 21 and aces:
            total -= 10
    return total


def dealer():
    number = get_card()
    suite = get_suite()
    total = points(dealerHand)
    if total <= 16:
        print('Dealer draws a card.')
        if number == '10':
            dealerHand.append('10' + suite[0])
        else:
            dealerHand.append(number[0] +
                              suite[0])
    else:
        print('Dealer holds.')


def player():
    number = get_card()
    suite = get_suite()
    print('You drew the ' + str(number) +
          ' of ' + suite + '.')
    if number == '10':
        playerHand.append('10' + suite[0])
    else:
        playerHand.append(number[0] +
                          suite[0])
    if points(playerHand) >= 21:
        # 21 is an automatic endgame
        # anything higher is an automatic loss
        get_verdict()


def get_verdict():
    player_score = points(playerHand)
    house_score = points(dealerHand)
    verdict = ('You have ' + str(player_score) +
               ' points, The House has ' +
               str(house_score) + ', ')
    verdict += "\n" + get_winner(player_score, house_score).capitalize() + " wins!"

    print(verdict)
    print('Dealer reveals:\n' + str(dealerHand))
    end_game()


def get_winner(player_score, house):
    verdict = ""

    if player_score <= 21:
        while points(dealerHand) <= 16:
            dealer()
    if 21 >= player_score > house:
        verdict += 'player'
    elif house > 21 >= player_score:
        verdict += 'player'
    elif player_score > 21:
        verdict += 'dealer'
    elif house >= player_score:
        verdict += 'dealer'
    else:
        verdict += 'dealer'
    return verdict


def end_game():
    # replay option and review results.
    choice = input('Play again?\n'
                   'n or q to quit, any other key to continue ').lower()
    quit_options = ['n', 'q']
    if len(choice) > 0:
        if choice[0] in quit_options:
            exit()
        else:
            main()
    else:
        main()


if __name__ == '__main__':
    main()
