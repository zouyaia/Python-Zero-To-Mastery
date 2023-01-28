import sys, random

try:
    s, f = sys.argv[1], sys.argv[2]
    print(f'Guess a number between {s} and {f}')
    num = str(random.randint(int(s), int(f)))
    while True:
        s = input()
        if s == num:
            print(f'You guessed right. It\'s {num}')
            break
        print("Take another guess!")
except:
    print('Game is under maintainance')
