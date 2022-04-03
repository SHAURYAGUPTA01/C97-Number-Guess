import random
number = random.randint(1,9)
print('number guessing game')
print('guess a number between 1-9')
chances=0
while chances < 5:
    guess= int(input('Enter Your guess :'))
    if guess == number :
        print('Congratulations you won the game')
        break
    elif guess < number :
        print('your guess was too low : gues a noumber higher than' , guess)
    else :
        print('your guess was too high : gues a noumber lower than' , guess)
    chances+=1
if not chances < 5:
    print('you lose, the correct answer was', number)