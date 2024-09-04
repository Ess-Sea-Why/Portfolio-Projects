import random

class Mastermind:
    def __init__(self, digits):
        self.digits = digits
        self.valid_digits = "1234567890"
        top_range = (10 ** digits) -1
        self.number = str(random.randint(0, top_range))
        while len(self.number) < self.digits:
            add_zero = "0" + self.number
            self.number = add_zero

    def correct_digits(self, guess):
        secret_digit_count = {}
        for digit in self.number:
            if digit in secret_digit_count:
                secret_digit_count[digit] += 1
            else:
                secret_digit_count[digit] = 1

        # Now compare with the guess
        total_right = 0
        for digit in guess:
            if digit in secret_digit_count and secret_digit_count[digit] > 0:
                total_right += 1
                secret_digit_count[digit] -= 1

        return total_right

    def correct_placement(self, guess):
        total_right = 0
        for num in range(0, self.digits):
            if guess[num] == self.number[num]:
                total_right += 1
        return total_right

    def evaluate_guess(self, guess):
        correct_digits = self.correct_digits(guess)
        correct_placement = self.correct_placement(guess)
        print(f"Correct Digits: {correct_digits} \nCorrect Placement: {correct_placement}")
        return correct_digits, correct_placement

    def is_guess_valid(self, guess):
        for character in guess:
            if character not in self.valid_digits:
                return False
        if len(guess) != self.digits:
            return False
        else:
            return True


title = """ 
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |      __      | || |    _______   | || |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |     _____    | || | ____  _____  | || |  ________    | |
| ||_   \  /   _|| || |     /  \     | || |   /  ___  |  | || | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |    |_   _|   | || ||_   \|_   _| | || | |_   ___ `.  | |
| |  |   \/   |  | || |    / /\ \    | || |  |  (__ \_|  | || | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__) |   | || |  |   \/   |  | || |      | |     | || |  |   \ | |   | || |   | |   `. \ | |
| |  | |\  /| |  | || |   / ____ \   | || |   '.___`-.   | || |     | |      | || |   |  _|  _   | || |   |  __ /    | || |  | |\  /| |  | || |      | |     | || |  | |\ \| |   | || |   | |    | | | |
| | _| |_\/_| |_ | || | _/ /    \ \_ | || |  |`\____) |  | || |    _| |_     | || |  _| |___/ |  | || |  _| |  \ \_  | || | _| |_\/_| |_ | || |     _| |_    | || | _| |_\   |_  | || |  _| |___.' / | |
| ||_____||_____|| || ||____|  |____|| || |  |_______.'  | || |   |_____|    | || | |_________|  | || | |____| |___| | || ||_____||_____|| || |    |_____|   | || ||_____|\____| | || | |________.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

continue_game = True
while continue_game:
    print(title)
    print("Welcome to the in-terminal version of my mastermind game project, see if you can work out the four digit number in less than 10 attempts")

    game_is_on = True
    guess_valid = False
    remaining_attempts = 10
    mastermind = Mastermind(4)
    while game_is_on:
        print(f"Remaining Attempts: {remaining_attempts}")
        while not guess_valid:
            guess = str(input("Input your answer: "))
            guess_valid = mastermind.is_guess_valid(guess)
            if not guess_valid:
                print("Invalid input, try again")
        guess_valid = False
        correct_dig, correct_place = mastermind.evaluate_guess(guess)
        remaining_attempts -= 1
        if correct_dig == 4 and correct_place == 4:
            game_is_on = False
            print("You successfully worked out the number!")
        if remaining_attempts == 0:
            game_is_on = False
            print(f"You ran out of attempts, the number was {mastermind.number}")

    play_again = str(input("Would you like to play again? Y/N\n"))






