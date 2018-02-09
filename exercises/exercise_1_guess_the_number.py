import random
def process_answer(answer, number):
    if(answer == number):
        print("That's correct!")
        return 1
    else:
        print("Wrong D:")
        return 0
    
def guess_the_number(number):
    answer = input("Guess my number :D\n")
    guess_counter = 0
    for i in range(1, 5):
        guess_counter = guess_counter + process_answer(answer, str(number))
        answer = input("Try again ;D \n")
    guess_counter = guess_counter + process_answer(answer, str(number))
    print("you guessed " + str(number) + " " + str(guess_counter) + " times");
    print("Game Over\n")
        
    try_again = input("Wanna play again? (y or n)\n")
    return try_again

def main(number):
    if not "n" in guess_the_number(number):
        main(random.randrange(10))

main(random.randrange(10))
print("Bye!")
