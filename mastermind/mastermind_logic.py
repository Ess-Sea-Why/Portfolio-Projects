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

