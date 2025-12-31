import random

CHOICES = ('ROCK', 'PAPER', 'SCISSORS')
BEATS = {
    'ROCK': 'SCISSORS',
    'PAPER': 'ROCK',
    'SCISSORS': 'PAPER',
}

INTRO = '\nI challenge you to a game of ROSHAMBO!\nBest of THREE!'
PROMPT = 'Choose: ROCK, PAPER, or SCISSORS. (Or Quit): '

def opp_throw() -> str:
    '''Return opponent's random choice.'''
    return random.choice(CHOICES)

def decide_winner(player: str, opp: str) -> str:
    '''
    Decide winner for round.
    Returns: 'TIE', 'PLAYER', or 'OPP'.
    '''
    if player == opp:
        return 'TIE'
    if BEATS[player] == opp:
        return 'PLAYER'
    return 'OPP'

def main() -> None:
    print(INTRO)

    score_opp = 0
    score_player = 0

    while score_opp < 2 and score_player < 2:
        player_choice = input(PROMPT).strip().upper()

        if player_choice == 'QUIT':
            print('You are WEAK!')
            return
        if player_choice not in CHOICES:
            print('Invalid choice!')
            continue

        opp_choice = opp_throw()
        outcome = decide_winner(player_choice, opp_choice)

        # Show both picks
        print(f'You choose: {player_choice}.\nOpponent chooses: {opp_choice}.')

        if outcome == 'TIE':
            print('\nTIE!')
        elif outcome == 'PLAYER':
            score_player += 1
            print('\nOne point for you... this time!')
        else:
            score_opp += 1
            print('\nAHAHA A point for me!')

        print(f'\nScore: Opponent {score_opp} | Player {score_player}\n')

    print('Final Results:')
    print(f'Opponent: {score_opp}\nPlayer: {score_player}')

    if score_opp > score_player:
        print('AHAHAH I WIN!!!\n')
    elif score_opp == score_player:
        print('A tie. You will not be so lucky next time!\n')
    else:
        print('You win this time.\n')

if __name__ == "__main__":
    main()