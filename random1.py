import random
from colorama import Fore
from colorama import Style

print(Fore.CYAN,'Welcome to the game,Maybe today will be your day!?',Style.RESET_ALL)
white_ball = []
strong_number = []


def WhiteBall():
    while len(white_ball) < 5:
        x = random.randrange(1, 21)
        while x not in white_ball and len(white_ball) <= 6:
            white_ball.append(x)
    for i in range(1):
        strong_number.append(random.randrange(1, 11))
    print('your lucky numbers:\n', Fore.GREEN + f' {sorted(white_ball)}', Style.RESET_ALL,
          Fore.YELLOW + f'{strong_number}', Style.RESET_ALL)


win_ball = []
win_strong = []


def Ballwin():
    while len(win_ball) < 5:
        x = random.randrange(1, 21)
        while x not in win_ball and len(win_ball) <= 6:
            win_ball.append(x)
    for i in range(1):
        win_strong.append(random.randrange(1, 11))
    print('today’s Powerball winning numbers:\n', Fore.GREEN + f'{sorted(win_ball)}', Style.RESET_ALL, Fore.YELLOW,
          f'{win_strong}', Style.RESET_ALL)


WhiteBall()
Ballwin()


def Identical():
    count = 0
    for i in white_ball:
        for k in win_ball:
            if k == i:
                count += 1
    if count == 5 and strong_number != win_strong:
        print(Fore.BLUE,'5 correct numbers 1000000$',Style.RESET_ALL)
    elif count == 5 and strong_number == win_strong:
        print(Fore.BLUE,'5 correct numbers and strong number you won in: 324000000$$$$$$  $ your millionaire',Style.RESET_ALL)
    elif count == 4 and strong_number != win_strong:
        print(Fore.BLUE,'4 correct numbers 100$',Style.RESET_ALL)
    elif count == 4 and strong_number == win_strong:
        print(Fore.BLUE,'4 correct numbers and strong number you won in: 10000$',Style.RESET_ALL)
    elif count == 3 and strong_number == win_strong:
        print(Fore.BLUE,'3 correct numbers and strong number you won in: 100$',Style.RESET_ALL)
    elif count == 3 and strong_number != win_strong:
        print(Fore.RED,'3 correct numbers 7$',Style.RESET_ALL)
    elif count == 2 and strong_number == win_strong:
        print(Fore.RED,'2 correct numbers and strong number you won in: 7$',Style.RESET_ALL)
    elif count == 1 and strong_number == win_strong:
        print(Fore.RED,'1 correct numbers and strong number you won in: 4$',Style.RESET_ALL)
    elif strong_number == win_strong:
        print(Fore.RED,'only strong number you won in: 1$',Style.RESET_ALL)
    else:
        print(Fore.RED,'try again',Style.RESET_ALL)


print(Fore.BLACK,'----------------------------------',Style.RESET_ALL)
Identical()
